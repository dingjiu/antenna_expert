# Antenna Expert: 基于 AutoGen 的 PyAEDT + HFSS 自动化天线仿真系统

Antenna Expert 是一个基于大语言模型 (LLM) 和 [AutoGen](https://microsoft.github.io/autogen/) 框架构建的多 Agent 协作系统。该系统能够接收用户的自然语言需求，自动完成天线的设计参数计算、HFSS 3D 建模、仿真运行、结果分析以及迭代优化，实现端到端的微波天线全自动化设计。

本系统底层通过调用 Ansys 官方的 [PyAEDT](https://aedt.docs.pyansys.com/) 库来驱动 HFSS 进行后台(无界面)的精确电磁仿真。

## 🌟 核心特性
- **自然语言驱动**：无需编写脚本或手动操作 UI，用自然语言描述需求（例如："设计一个2.4GHz的半波偶极子天线"）。
- **多 Agent 协作流**：
  - `RequirementEngineer`：解析需求，提取中心频率、带宽、VSWR等标准化指标。
  - `TheoryExpert`：基于电磁理论计算天线的初始物理尺寸和理论性能阈值。
  - `HFSSExecutor`：根据生成的参数自动编写并调用 PyAEDT 脚本，在后台执行 HFSS 建模与求解。
  - `ResultAnalyst`：解析 S 参数和方向图结果，判断是否达标。
  - `Optimizer`：如果结果未达标，根据偏差自动推导新的尺寸参数，触发下一轮迭代。
- **高阶建模封装**：内置 `Stackup3D` 微带贴片天线封装和半波偶极子天线建模能力。
- **动态技能库 (Skill Library)**：通过解析 PyAEDT 源码，提取了上千个核心 API 注入 Agent，极大降低了 LLM 生成仿真代码时的幻觉。

## 🛠️ 环境要求

### 软件依赖
1. **Python 3.8+**
2. **Ansys HFSS**：本地需安装 Ansys Electronics Desktop (AEDT)，推荐版本 2021 R1 及以上。

### Python 库安装
```bash
git clone https://github.com/dingjiu/antenna_expert.git
cd antenna_expert
pip install -r requirements.txt
```

## 🚀 快速开始

### 1. 配置大模型 API
本项目默认配置为使用 **DeepSeek** 大模型（推荐使用，其代码生成与逻辑推理能力极佳）。
在项目根目录创建或修改 `OAI_CONFIG_LIST` 文件，填入你自己的 API Key：
```json
[
    {
        "model": "deepseek-chat",
        "api_key": "YOUR_DEEPSEEK_API_KEY_HERE",
        "base_url": "https://api.deepseek.com/v1"
    }
]
```
*(也可以直接通过环境变量 `export OPENAI_API_KEY="your-key"` 进行配置)*

### 2. 运行系统
在终端中直接运行 `main.py` 并附带你的设计需求：

```bash
python main.py "设计一个工作在 2.4GHz 的半波偶极子天线，要求VSWR小于2.0"
```

系统启动后：
1. Agent 会开始互相讨论并计算出长度、半径、间隙等参数。
2. 随后自动在后台唤醒 HFSS（由于是非图形化界面，你可能看不到窗口，但能看到终端日志）。
3. 仿真完成后，Agent 会读取 S11 数据，如果不满足 VSWR < 2.0，它会自动微调长度并重新仿真，直到满足要求或达到最大迭代次数。

## 📂 项目结构
```text
antenna_expert/
├── main.py                  # AutoGen 初始化与自定义 GroupChat 调度引擎
├── core/
│   └── schemas.py           # Pydantic 核心数据结构，用于约束 Agent 输出格式
├── tools/
│   └── hfss_tool.py         # AutoGen 专属工具函数，供 LLM 通过 Function Calling 调用
├── utils/
│   └── pyaedt_helper.py     # PyAEDT 封装类，实际操作 HFSS 建立模型、求解、导出的底层代码
├── parse_pyaedt_skills.py   # AST 源码解析工具，用于从 pyaedt 提取 API
├── pyaedt_skills.json       # 自动生成的全量 PyAEDT 仿真技能字典
└── requirements.txt         # 依赖清单
```

## ⚠️ 注意事项与规则
- **HFSS 许可证**：系统运行期间会占用一个 AEDT License 席位，请确保你的机器已正确配置许可证。
- **免 UI 模式**：目前 PyAEDT 包装器 `PyAEDTWrapper` 默认开启 `non_graphical=True`，在后台静默运行。如需观察建图过程，可在代码中改为 `False`。
- **仿真时长**：天线仿真属于计算密集型任务。网格剖分和扫频可能需要几分钟到几十分钟不等。请耐心等待 `HFSSExecutor` 的返回。
- **Token 消耗**：由于采用了多 Agent 讨论及复杂的 JSON 传递，如果发生多次迭代，会消耗一定的 Token，请关注你的 API 额度。

## 🤝 扩展开发
如果你想让系统支持新的天线类型（如喇叭天线、FSS）：
1. 在 `utils/pyaedt_helper.py` 中编写相应的参数化建模函数。
2. 在 `tools/hfss_tool.py` 的分支逻辑中加入该类型的调用。
3. 修改 `main.py` 中 `TheoryExpert` 的 `system_message`，告知 LLM 新天线类型所需提供的参数字段即可。

---
*Created and maintained by [dingjiu](https://github.com/dingjiu)*
