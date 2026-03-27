import os
import sys
import autogen
from core.schemas import StandardizedAntennaSpec, AntennaTheoryParams, AnalysisReport
from tools.hfss_tool import run_hfss_simulation

def main():
    # 1. 自动读取环境变量中的配置，或者使用占位符
    # 实际运行时，需要在当前目录创建 OAI_CONFIG_LIST 文件或设置环境变量
    config_list = autogen.config_list_from_json(
        "OAI_CONFIG_LIST",
        filter_dict={"model": ["gpt-4", "gpt-4-turbo", "gpt-4o", "deepseek-chat"]},
    )
    if not config_list:
        print("警告: 未找到 OAI_CONFIG_LIST，使用默认配置占位。请配置大模型API。")
        config_list = [{"model": "gpt-4", "api_key": os.environ.get("OPENAI_API_KEY", "YOUR_API_KEY")}]

    llm_config = {
        "config_list": config_list,
        "temperature": 0.1,
        "cache_seed": 42
    }

    # 2. 初始化Agent团队
    user_proxy = autogen.UserProxyAgent(
        name="User",
        system_prompt="你代表用户，提出天线设计需求。当收到最终结果报告且满足所有指标时，输出 TERMINATE 结束流程。",
        human_input_mode="NEVER",
        code_execution_config={"use_docker": False},
        is_termination_msg=lambda x: "TERMINATE" in str(x.get("content", ""))
    )

    req_engineer = autogen.AssistantAgent(
        name="RequirementEngineer",
        system_prompt=f"""你是一个需求分析工程师。
请从用户的自然语言描述中提取天线设计参数。
严格输出JSON格式，匹配以下Pydantic Schema:
{StandardizedAntennaSpec.schema_json()}
只输出JSON，不要包含其他文字。""",
        llm_config=llm_config
    )

    theory_expert = autogen.AssistantAgent(
        name="TheoryExpert",
        system_prompt=f"""你是一个天线理论专家。
请根据需求分析工程师输出的标准化天线需求(JSON)，计算天线的理论初始尺寸和性能阈值。
严格输出JSON格式，匹配以下Pydantic Schema:
{AntennaTheoryParams.schema_json()}
微带天线计算提示：宽度 W = (c / (2 * f)) * sqrt(2 / (er + 1))；长度 L = c / (2 * f * sqrt(ereff)) - 2 * delta_L。
只输出JSON，不要包含其他文字。""",
        llm_config=llm_config
    )

    hfss_executor = autogen.AssistantAgent(
        name="HFSSExecutor",
        system_prompt="""你是一个HFSS仿真执行专家。
你需要调用已注册的工具 `run_hfss_simulation`，将前序获取的 spec_json 和 theory_json 传入。
获取到工具返回的仿真结果后，直接将结果转述出来，供ResultAnalyst分析。""",
        llm_config=llm_config
    )

    result_analyst = autogen.AssistantAgent(
        name="ResultAnalyst",
        system_prompt=f"""你是一个天线仿真结果分析专家。
根据HFSSExecutor返回的仿真结果与原始指标，判断天线是否达标，并给出优化建议。
严格输出JSON格式，匹配以下Pydantic Schema:
{AnalysisReport.schema_json()}
如果 is_passed 为 true，在JSON后面另起一行输出 "TERMINATE"。
如果 is_passed 为 false，只输出JSON。""",
        llm_config=llm_config
    )

    optimizer = autogen.AssistantAgent(
        name="Optimizer",
        system_prompt="""你是一个天线优化专家。
根据ResultAnalyst的诊断报告和当前的理论参数，计算出新的天线参数以便重新仿真。
严格输出JSON格式，格式与 AntennaTheoryParams 的JSON结构保持一致。
只输出JSON，不要包含其他文字。""",
        llm_config=llm_config
    )

    # 3. 注册工具 (Function Calling)
    autogen.agentchat.register_function(
        run_hfss_simulation,
        caller=hfss_executor,
        executor=user_proxy,
        name="run_hfss_simulation",
        description="执行HFSS自动化建模与仿真并返回结果"
    )

    # 4. 定义调度逻辑 (Scheduler Agent 等效实现)
    def custom_speaker_selection(last_speaker, groupchat):
        messages = groupchat.messages
        if not messages:
            return req_engineer

        # 获取最新一条消息内容
        last_message = messages[-1]

        if last_speaker == user_proxy:
            # 如果是初始用户提问，分配给需求工程师
            if len(messages) <= 2:
                return req_engineer
            # 如果User执行了工具，将结果传回给HFSSExecutor
            return hfss_executor
            
        elif last_speaker == req_engineer:
            return theory_expert
            
        elif last_speaker == theory_expert:
            return hfss_executor
            
        elif last_speaker == hfss_executor:
            # 如果HFSSExecutor发起了工具调用，必须由UserProxy来执行
            if "tool_calls" in last_message or "function_call" in last_message:
                return user_proxy
            # 否则，表示HFSSExecutor给出了最终结果，交给ResultAnalyst
            return result_analyst
            
        elif last_speaker == result_analyst:
            # 如果分析师判定达标并输出了 TERMINATE，结束
            if "TERMINATE" in str(last_message.get("content", "")):
                return None
            # 否则交给优化器
            return optimizer
            
        elif last_speaker == optimizer:
            # 优化完成后，回到HFSSExecutor重新仿真
            return hfss_executor

        return None # 默认结束

    # 5. 创建GroupChat与Manager
    groupchat = autogen.GroupChat(
        agents=[user_proxy, req_engineer, theory_expert, hfss_executor, result_analyst, optimizer],
        messages=[],
        max_round=20,
        speaker_selection_method=custom_speaker_selection
    )
    
    manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

    # 6. 启动任务
    idea = "设计2.4GHz全向微带天线，增益≥2dBi，VSWR≤1.5，尺寸不超过50mm×50mm，介质板用FR4"
    if len(sys.argv) > 1:
        idea = sys.argv[1]

    print(f"==================================================")
    print(f"启动天线设计任务 (基于 AutoGen): {idea}")
    print(f"==================================================")
    
    user_proxy.initiate_chat(
        manager,
        message=idea
    )

if __name__ == "__main__":
    main()
