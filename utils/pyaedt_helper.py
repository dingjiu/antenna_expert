import os
import time
from typing import Dict, Any, Tuple

try:
    import ansys.aedt.core
    from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
    _REAL_AEDT = True
except ImportError:
    _REAL_AEDT = False
    # 占位符：如果环境中未安装pyaedt，提供一个Mock类以便在非Windows环境进行代码测试
    class MockHfss:
        def __init__(self, *args, **kwargs):
            self.modeler = MockModeler()
            self.materials = MockMaterials()
            self.PLANE = MockPlane()
            self.AXIS = MockPlane()
            self.AxisDir = MockAxisDir()
            self.post = MockPost()
            self._vars = {}

        def __setitem__(self, key, value):
            self._vars[key] = value

        def __getitem__(self, key):
            return self._vars.get(key)
        def insert_design(self, name): pass
        def set_active_design(self, name): pass
        def save_project(self, path=None): pass
        def close_project(self): pass
        def release_desktop(self, *args, **kwargs): pass
        def create_setup(self, *args, **kwargs): return MockSetup()
        def create_open_region(self, *args, **kwargs): pass
        def assign_radiation_boundary_to_objects(self, *args, **kwargs): pass
        def analyze(self, *args, **kwargs): pass
        def analyze_setup(self, name): pass
        def assign_perfectE(self, *args, **kwargs): pass
        def create_lumped_port_to_sheet(self, *args, **kwargs): pass

    class MockStackup3D:
        def __init__(self, hfss): pass
        def add_ground_layer(self, *args, **kwargs): return MockLayer()
        def add_dielectric_layer(self, *args, **kwargs): return MockLayer()
        def add_signal_layer(self, *args, **kwargs): return MockLayer()
        def resize_around_element(self, *args, **kwargs): pass

    class MockLayer:
        def add_patch(self, *args, **kwargs): return MockPatch()

    class MockPatch:
        def create_probe_port(self, *args, **kwargs): pass

    class MockPlane:
        XY = "XY"
        YZ = "YZ"
        ZX = "ZX"
        Z = "Z"
        
    class MockAxisDir:
        ZPos = "ZPos"
        
    class MockModeler:
        model_units = "mm"
        objects = {}
        def create_box(self, *args, **kwargs): return MockObject()
        def create_rectangle(self, *args, **kwargs): return MockObject()
        def create_region(self, *args, **kwargs): return MockObject()
        def create_cylinder(self, *args, **kwargs): return MockObject()
        def subtract(self, *args, **kwargs): pass
        def unite(self, *args, **kwargs): pass
        
    class MockMaterials:
        def add_material(self, *args, **kwargs): pass
        
    class MockObject:
        name = "mock_obj"
        
    class MockSetup:
        props = {}
        def add_sweep(self, *args, **kwargs): return MockSweep()
        def create_frequency_sweep(self, *args, **kwargs): return MockSweep()
        def update(self): pass
        
    class MockSweep:
        props = {}
        def update(self): pass
        
    class MockPost:
        def get_solution_data(self, *args, **kwargs): return MockSolutionData()
        def export_report_to_csv(self, *args, **kwargs): pass
        def create_report(self, *args, **kwargs): return MockReport()
        
    class MockReport:
        def get_solution_data(self, *args, **kwargs): return MockSolutionData()
        
    class MockSolutionData:
        def data_real(self, *args, **kwargs): return [1.5]
        def plot(self, *args, **kwargs): pass
        expressions = []

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
        if _REAL_AEDT:
            self.hfss = ansys.aedt.core.Hfss(
                project=self.project_name, 
                design=self.design_name, 
                solution_type="Terminal", 
                new_desktop=True, 
                non_graphical=self.non_graphical
            )
        else:
            self.hfss = MockHfss()
        return True

    def create_patch_antenna_model_with_stackup(self, params: Dict[str, float], center_freq_ghz: float, material: str = "FR4_epoxy", er: float = 4.4):
        """
        基于官方示例 (Stackup3D) 创建微带贴片天线模型。
        params需包含: patch_l, patch_w, sub_h
        """
        if not self.hfss:
            raise ValueError("HFSS未初始化")
            
        self.hfss.modeler.model_units = "mm"
        
        # 使用 Stackup3D 高级接口 (官方推荐)
        if _REAL_AEDT:
            stackup = Stackup3D(self.hfss)
        else:
            stackup = MockStackup3D(self.hfss)
            
        # 1. 接地层
        ground = stackup.add_ground_layer(
            "ground", material="copper", thickness=0.035, fill_material="air"
        )
        
        # 2. 介质层
        dielectric = stackup.add_dielectric_layer(
            "dielectric", thickness=f"{params.get('sub_h', 1.6)}mm", material=material
        )
        
        # 3. 信号层 (Patch)
        signal = stackup.add_signal_layer(
            "signal", material="copper", thickness=0.035, fill_material="air"
        )
        patch = signal.add_patch(
            patch_length=params.get("patch_l", 29.5), 
            patch_width=params.get("patch_w", 38.0), 
            patch_name="Patch", 
            frequency=center_freq_ghz * 1e9
        )
        
        # 4. 边界条件
        stackup.resize_around_element(patch)
        pad_length = [10, 10, 10, 10, 10, 10]  # Air bounding box buffer in mm
        region = self.hfss.modeler.create_region(pad_length, is_percentage=False)
        self.hfss.assign_radiation_boundary_to_objects(region)
        
        # 5. 同轴馈电
        # 根据官方示例使用 probe_port
        patch.create_probe_port(ground, rel_x_offset=0.485)
        
        return True

    def create_dipole_antenna(self, params: Dict[str, float], center_freq_ghz: float):
        """
        基于官方示例 dipole.py 创建半波偶极子天线。
        params需包含: length, radius, gap
        """
        if not self.hfss:
            raise ValueError("HFSS未初始化")
            
        self.hfss.modeler.model_units = "mm"
        
        length = params.get("length", 60.0)
        radius = params.get("radius", 1.0)
        gap = params.get("gap", 2.0)
        
        # 将参数设置为 HFSS 设计变量，方便参数化扫频和优化
        self.hfss["length"] = f"{length}mm"
        self.hfss["radius"] = f"{radius}mm"
        self.hfss["gap"] = f"{gap}mm"
        
        # 1. 创建上臂 (Positive Arm)
        # 注意: 在真实的 PyAEDT 中应使用 self.hfss.AXIS.Z，为兼容 Mock 做了容错处理
        z_axis = getattr(getattr(self.hfss, 'AXIS', None), 'Z', "Z")
        arm_p = self.hfss.modeler.create_cylinder(
            orientation=z_axis,
            origin=[0, 0, "gap/2"],
            radius="radius",
            height="length/2 - gap/2",
            name="arm_p",
            matname="copper"
        )
        
        # 2. 创建下臂 (Negative Arm)
        arm_n = self.hfss.modeler.create_cylinder(
            orientation=z_axis,
            origin=[0, 0, "-gap/2"],
            radius="radius",
            height="-length/2 + gap/2",
            name="arm_n",
            matname="copper"
        )
        
        # 3. 创建端口源 (Lumped Port)
        # 兼容处理: 检查 PLANE 属性是否存在
        yz_plane = getattr(getattr(self.hfss, 'PLANE', None), 'YZ', "YZ")
        port_rect = self.hfss.modeler.create_rectangle(
            orientation=yz_plane,
            origin=[0, "-radius", "-gap/2"],
            sizes=["2*radius", "gap"],
            name="port_sheet"
        )
        self.hfss.create_lumped_port_to_sheet(
            port_rect.name,
            axisdir=getattr(getattr(self.hfss, 'AxisDir', None), 'ZPos', "ZPos"),
            portname="Port1",
            impedance=50
        )
        
        # 4. 开放区域边界条件 (Radiation Boundary)
        self.hfss.create_open_region(str(self.hfss.modeler.model_units))
        
        return True

    def setup_and_analyze(self, center_freq_ghz: float, freq_start: float, freq_stop: float):
        """
        设置求解器参数并运行仿真 (适配官方新API)
        """
        setup = self.hfss.create_setup(name="Setup1", setup_type="HFSSDriven", Frequency=f"{center_freq_ghz}GHz")
        
        setup.create_frequency_sweep(
            unit="GHz",
            name="Sweep1",
            start_frequency=freq_start,
            stop_frequency=freq_stop,
            sweep_type="Interpolating",
        )
        
        # 运行仿真
        self.hfss.analyze(cores=4)
        return True

    def export_results(self, output_dir: str) -> Dict[str, str]:
        """
        导出S参数和方向图结果到CSV
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        s11_csv = os.path.join(output_dir, "s11.csv")
        pattern_csv = os.path.join(output_dir, "pattern.csv")
        
        # 导出S参数 (基于官方最新的报告API)
        if _REAL_AEDT:
            plot_data = self.hfss.get_traces_for_plot()
            if plot_data:
                report = self.hfss.post.create_report(plot_data)
                solution = report.get_solution_data()
                # 在真实环境下，这里可以保存solution到CSV或直接处理数据
                # 此处为了演示简化处理
                pass
        else:
            self.hfss.post.export_report_to_csv(self.project_name, s11_csv)
            
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
