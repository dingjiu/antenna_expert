import os
import ast
import json
from collections import defaultdict

# 目标模块：只抽取 3D 电磁 / HFSS 核心模块
TARGET_MODULES = [
    "ansys.aedt.core.hfss",
    "ansys.aedt.core.modeler.cad.objects3d",
    "ansys.aedt.core.modules.boundary.hfss_boundary",
    "ansys.aedt.core.modules.solve_setup",
    "ansys.aedt.core.visualization.post.post_processor",
    "ansys.aedt.core.application.parameters",
    "ansys.aedt.core.modeler.cad.components_3d",
    # 由于pyaedt内部重构，路径可能不完全一致，这里做容错映射
]

# 技能分类
SKILL_CATEGORIES = {
    "environment": "环境与工程管理",
    "parameters": "参数与变量管理",
    "modeling": "3D 建模与几何体",
    "boundaries": "边界条件与材料",
    "excitations": "激励与端口设置",
    "setup": "求解与网格设置",
    "post": "仿真执行与后处理",
    "uncategorized": "未分类 (需人工审核)"
}

# 高频关键词匹配
CATEGORY_KEYWORDS = {
    "environment": ["hfss", "desktop", "project", "design", "save", "close", "insert"],
    "parameters": ["variable", "parameter", "parametric", "set_variable", "expression"],
    "modeling": ["create_box", "create_cylinder", "create_sphere", "array", "rotate", "move", "material", "subtract", "unite", "create_rectangle"],
    "boundaries": ["radiation", "pec", "pmc", "boundary", "pml", "assign_material", "assign_perfect_e", "assign_perfect_e"],
    "excitations": ["port", "wave_port", "lumped_port", "excitation", "floquet", "probe"],
    "setup": ["solution", "sweep", "mesh", "adaptive", "frequency", "setup", "analyze"],
    "post": ["s_param", "z_param", "gain", "farfield", "nearfield", "report", "export", "plot", "solution_data"]
}

def determine_category(func_name: str) -> str:
    """根据函数名中的关键词进行分类"""
    func_name_lower = func_name.lower()
    for cat, keywords in CATEGORY_KEYWORDS.items():
        if any(kw in func_name_lower for kw in keywords):
            return cat
    return "uncategorized"

def parse_python_file(filepath: str, module_name: str) -> list:
    """解析单个 Python 文件，提取类和方法的文档"""
    skills = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())
            
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_name = node.name
                for item in node.body:
                    if isinstance(item, ast.FunctionDef) and not item.name.startswith('_'):
                        func_name = item.name
                        # 提取参数
                        args = [a.arg for a in item.args.args if a.arg != 'self']
                        
                        # 提取文档字符串
                        docstring = ast.get_docstring(item)
                        if not docstring:
                            docstring = "No description provided."
                            
                        # 取 docstring 的第一句话作为简短描述
                        short_desc = docstring.strip().split('\n')[0]
                        
                        cat = determine_category(func_name)
                        
                        skills.append({
                            "module": module_name,
                            "class": class_name,
                            "method": func_name,
                            "arguments": args,
                            "description": short_desc,
                            "category": cat
                        })
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        
    return skills

def find_target_files(base_dir: str):
    """递归遍历源码目录，匹配可能的目标模块文件"""
    file_map = {}
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.py'):
                full_path = os.path.join(root, file)
                # 将路径转为模块名格式，例如 ansys/aedt/core/hfss.py -> ansys.aedt.core.hfss
                rel_path = os.path.relpath(full_path, base_dir)
                mod_name = rel_path.replace(os.sep, '.').replace('.py', '')
                
                # 模糊匹配我们关注的模块
                if "hfss" in mod_name or "modeler" in mod_name or "boundary" in mod_name or "setup" in mod_name or "post" in mod_name or "parameters" in mod_name:
                    file_map[mod_name] = full_path
    return file_map

def main():
    base_src_dir = "/home/dorji/pyaedt/src"
    
    print(f"正在扫描 {base_src_dir} 目录下的 PyAEDT 源码...")
    files_to_parse = find_target_files(base_src_dir)
    
    all_skills = []
    for mod_name, filepath in files_to_parse.items():
        skills = parse_python_file(filepath, mod_name)
        all_skills.extend(skills)
        
    print(f"总计提取了 {len(all_skills)} 个公开方法/技能。")
    
    # 按分类聚合
    categorized_skills = defaultdict(list)
    for s in all_skills:
        categorized_skills[s["category"]].append(s)
        
    # 生成 Markdown 文档
    md_content = "# PyAEDT 仿真专家技能库 (Skill Library)\n\n"
    md_content += "> 本文档由源码自动生成，用于指导 AutoGen Agent 调用 PyAEDT 接口进行 HFSS 天线仿真。\n\n"
    
    for cat_key, cat_name in SKILL_CATEGORIES.items():
        skills = categorized_skills.get(cat_key, [])
        if not skills:
            continue
            
        md_content += f"## {cat_name} ({cat_key})\n"
        for s in skills:
            # 过滤掉一些内部的、或者过于底层的冗余方法以保持清晰
            if "get" in s["method"] and "uncategorized" in s["category"]:
                continue
            md_content += f"### `{s['class']}.{s['method']}`\n"
            md_content += f"- **参数**: `{', '.join(s['arguments'])}`\n"
            md_content += f"- **模块**: `{s['module']}`\n"
            md_content += f"- **描述**: {s['description']}\n\n"
            
    # 输出结果
    output_json = "/home/dorji/hffs_agent/antenna_expert/pyaedt_skills.json"
    output_md = "/home/dorji/hffs_agent/antenna_expert/pyaedt_skills.md"
    
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(categorized_skills, f, ensure_ascii=False, indent=4)
        
    with open(output_md, "w", encoding="utf-8") as f:
        f.write(md_content)
        
    print(f"解析完成！\n数据已保存至:\n- {output_json}\n- {output_md}")

if __name__ == "__main__":
    main()
