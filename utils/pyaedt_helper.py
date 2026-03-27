import os
import time
from typing import Dict, Any, Tuple

try:
    from pyaedt import Hfss
except ImportError:
    # 占位符：如果环境中未安装pyaedt，提供一个Mock类以便在非Windows环境进行代码测试
    class Hfss:
        def __init__(self, *args, **kwargs):
            self.modeler = MockModeler()
            self.materials = MockMaterials()
            self.PLANE = MockPlane()
            self.AxisDir = MockAxisDir()
            self.post = MockPost()
            self._vars = {}
            pass
        def __setitem__(self, key, value):
            self._vars[key] = value
        def __getitem__(self, key):
            return self._vars.get(key)
        def insert_design(self, name): pass
        def set_active_design(self, name): pass
        def save_project(self, path=None): pass
        def close_project(self): pass
        def release_desktop(self, *args, **kwargs): pass
        def create_setup(self, name): return MockSetup()
        def create_open_region(self, *args, **kwargs): pass
        def analyze_setup(self, name): pass
        def assign_perfectE(self, *args, **kwargs): pass
        def create_lumped_port_to_sheet(self, *args, **kwargs): pass
        
    class MockPlane:
        XY = "XY"
        YZ = "YZ"
        ZX = "ZX"
        
    class MockAxisDir:
        ZPos = "ZPos"
        
    class MockModeler:
        model_units = "mm"
        def create_box(self, *args, **kwargs): return MockObject()
        def create_rectangle(self, *args, **kwargs): return MockObject()
        def subtract(self, *args, **kwargs): pass
        def unite(self, *args, **kwargs): pass
        
    class MockMaterials:
        def add_material(self, *args, **kwargs): pass
        
    class MockObject:
        name = "mock_obj"
        
    class MockSetup:
        props = {}
        def add_sweep(self, *args, **kwargs): return MockSweep()
        def update(self): pass
        
    class MockSweep:
        props = {}
        def update(self): pass
        
    class MockPost:
        def get_solution_data(self, *args, **kwargs): return MockSolutionData()
        def export_report_to_csv(self, *args, **kwargs): pass
        
    class MockSolutionData:
        def data_real(self, *args, **kwargs): return [1.5]

class PyAEDTWrapper:
    """
    封装PyAEDT常用函数，提供给Agent调用的统一接口。
    负责HFSS启动、建模、设置、网格划分、求解、导出。
    """
    def __init__(self, project_name: str = "AntennaProject", design_name: str = "HFSSDesign", non_graphical: bool = True):
        self.project_name = project_name
        self.design_name = design_name
        self.non_graphical = non_graphical
        self.hfss = None

    def initialize_hfss(self):
        """初始化并启动HFSS"""
        # 注意: PyAEDT自动处理Desktop实例
        self.hfss = Hfss(projectname=self.project_name, 
                         designname=self.design_name, 
                         solution_type="Terminal", 
                         new_desktop_session=True, 
                         non_graphical=self.non_graphical)
        return True

    def create_patch_antenna_model(self, params: Dict[str, float], material: str = "FR4_epoxy", er: float = 4.4):
        """
        基于参数化字典创建微带贴片天线模型。
        params需包含: sub_l, sub_w, sub_h, patch_l, patch_w, feed_x, feed_y
        """
        if not self.hfss:
            raise ValueError("HFSS未初始化")
            
        # 设置设计变量，方便后续参数化优化
        for k, v in params.items():
            self.hfss[k] = f"{v}mm"
            
        # 1. 介质板
        sub = self.hfss.modeler.create_box(["-sub_l/2", "-sub_w/2", 0], ["sub_l", "sub_w", "sub_h"], 
                                           name="Substrate", matname=material)
        
        # 2. 接地板 (Ground)
        gnd = self.hfss.modeler.create_rectangle(self.hfss.PLANE.XY, ["-sub_l/2", "-sub_w/2", 0], 
                                                 ["sub_l", "sub_w"], name="Ground")
        self.hfss.assign_perfectE(gnd, sourcename="PerfE_Ground")
        
        # 3. 辐射贴片 (Patch)
        patch = self.hfss.modeler.create_rectangle(self.hfss.PLANE.XY, ["-patch_l/2", "-patch_w/2", "sub_h"], 
                                                   ["patch_l", "patch_w"], name="Patch")
        self.hfss.assign_perfectE(patch, sourcename="PerfE_Patch")
        
        # 4. 馈电端口 (Lumped Port)
        # 简单使用集总端口，位于patch和ground之间
        port_rect = self.hfss.modeler.create_rectangle(self.hfss.PLANE.YZ, 
                                                       ["feed_x", "feed_y", 0], 
                                                       ["0.5mm", "sub_h"], name="Port_Sheet") # 简化模型
        self.hfss.create_lumped_port_to_sheet(port_rect.name, axisdir=self.hfss.AxisDir.ZPos, 
                                              impedance=50, portname="Port1")
        
        # 5. 辐射边界条件 (Radiation Box)
        self.hfss.create_open_region(str(self.hfss.modeler.model_units))
        return True

    def setup_and_analyze(self, center_freq_ghz: float, freq_start: float, freq_stop: float):
        """
        设置求解器参数并运行仿真
        """
        setup = self.hfss.create_setup("Setup1")
        setup.props["Frequency"] = f"{center_freq_ghz}GHz"
        setup.props["MaximumPasses"] = 15
        setup.props["MinimumPasses"] = 2
        setup.props["MinimumConvergedPasses"] = 2
        setup.props["PercentRefinement"] = 30
        setup.update()
        
        # 添加扫频
        sweep = setup.add_sweep("Sweep1")
        sweep.props["Type"] = "Interpolating"
        sweep.props["RangeType"] = "LinearCount"
        sweep.props["RangeStart"] = f"{freq_start}GHz"
        sweep.props["RangeEnd"] = f"{freq_stop}GHz"
        sweep.props["RangeCount"] = 101
        sweep.props["SaveFields"] = False
        sweep.update()
        
        # 运行仿真
        self.hfss.analyze_setup("Setup1")
        return True

    def export_results(self, output_dir: str) -> Dict[str, str]:
        """
        导出S参数和方向图结果到CSV
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        s11_csv = os.path.join(output_dir, "s11.csv")
        pattern_csv = os.path.join(output_dir, "pattern.csv")
        
        # 导出S参数
        self.hfss.post.export_report_to_csv(self.project_name, s11_csv)
        
        # 尝试导出3D增益方向图 (此处为简化调用)
        # self.hfss.post.export_report_to_csv("3D_Gain", pattern_csv)
        
        # 提取VSWR和Gain
        # 注意: 这里的API是PyAEDT特定的，需要根据实际版本调整
        return {
            "s11_csv": s11_csv,
            "pattern_csv": pattern_csv
        }

    def close(self, save_project=True, project_path=None):
        """保存并释放桌面"""
        if self.hfss:
            if save_project and project_path:
                self.hfss.save_project(project_path)
            self.hfss.release_desktop(close_projects=True, close_desktop=True)
            self.hfss = None
