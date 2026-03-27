import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.schemas import StandardizedAntennaSpec, AntennaTheoryParams
from utils.pyaedt_helper import PyAEDTWrapper

def test_pyaedt_wrapper_mock():
    """
    测试PyAEDT封装类（在没有真实HFSS环境时使用Mock对象）
    """
    wrapper = PyAEDTWrapper(project_name="TestProject", non_graphical=True)
    wrapper.initialize_hfss()
    
    # 测试参数
    params = {
        "patch_l": 29.5,
        "patch_w": 38.0,
        "feed_x": 0.0,
        "feed_y": 10.0,
        "sub_l": 50.0,
        "sub_w": 50.0,
        "sub_h": 1.6
    }
    
    print("开始测试创建模型...")
    wrapper.create_patch_antenna_model(params)
    print("模型创建测试通过。")
    
    print("开始测试仿真设置...")
    wrapper.setup_and_analyze(2.4, 2.3, 2.5)
    print("仿真设置测试通过。")
    
    print("开始测试结果导出...")
    output_dir = os.path.join(os.getcwd(), "simulation_results")
    files = wrapper.export_results(output_dir)
    print(f"结果导出测试通过: {files}")
    
    wrapper.close(save_project=False)

if __name__ == "__main__":
    test_pyaedt_wrapper_mock()
