from pydantic import BaseModel, Field
from typing import Optional, Dict, List

class StandardizedAntennaSpec(BaseModel):
    """
    标准化天线指标文档（由需求分析工程师Agent输出）
    """
    center_freq_ghz: float = Field(..., description="中心频率，单位GHz")
    freq_range_ghz: tuple[float, float] = Field(..., description="频率范围，单位GHz，例如 (2.3, 2.5)")
    gain_min_dbi: float = Field(default=0.0, description="最小增益要求，单位dBi")
    vswr_max: float = Field(default=2.0, description="最大电压驻波比(VSWR)")
    polarization: str = Field(default="linear", description="极化方式，如 linear, circular")
    size_limit_mm: Optional[tuple[float, float, float]] = Field(None, description="尺寸限制 (长, 宽, 高) 单位mm")
    
    # 介质板参数
    substrate_material: str = Field(default="FR4_epoxy", description="介质板材料")
    substrate_er: float = Field(default=4.4, description="介质板相对介电常数")
    substrate_thickness_mm: float = Field(default=1.6, description="介质板厚度，单位mm")
    
    port_type: str = Field(default="lumped", description="端口类型：lumped (集总端口) 或 wave (波端口)")
    simulation_accuracy: str = Field(default="normal", description="仿真精度要求：fast, normal, high")

class AntennaTheoryParams(BaseModel):
    """
    天线理论参数初值（由天线理论专家Agent输出）
    """
    antenna_type: str = Field(..., description="天线类型，如 'Microstrip Patch', 'Dipole'")
    initial_params_mm: Dict[str, float] = Field(..., description="天线结构初始参数，单位mm。例如 {'patch_length': 29.5, 'patch_width': 38.0}")
    theoretical_max_gain_dbi: float = Field(..., description="理论上的最大增益参考值")
    theoretical_vswr_range: tuple[float, float] = Field(..., description="合理的VSWR范围参考值")
    ground_size_mm: Optional[tuple[float, float]] = Field(None, description="接地板尺寸 (长, 宽)")
    feed_position_mm: Optional[tuple[float, float]] = Field(None, description="馈电点位置 (x, y)")

class SimulationResult(BaseModel):
    """
    仿真原始数据反馈（由HFSS建模仿真执行Agent输出）
    """
    success: bool = Field(..., description="仿真是否成功执行完毕")
    project_path: Optional[str] = Field(None, description="HFSS工程文件(.aedt)路径")
    error_message: Optional[str] = Field(None, description="如果失败，记录报错信息")
    
    # 仿真提取的数据
    center_freq_vswr: Optional[float] = Field(None, description="中心频率处的VSWR")
    max_gain_dbi: Optional[float] = Field(None, description="仿真的最大增益")
    radiation_efficiency: Optional[float] = Field(None, description="辐射效率")
    bandwidth_mhz: Optional[float] = Field(None, description="符合VSWR要求的阻抗带宽")
    
    # 原始数据文件路径
    s11_csv_path: Optional[str] = Field(None, description="S11参数导出的CSV路径")
    pattern_csv_path: Optional[str] = Field(None, description="方向图导出的CSV路径")

class AnalysisReport(BaseModel):
    """
    结果分析与仿真报告（由仿真结果分析与报告生成Agent输出）
    """
    is_passed: bool = Field(..., description="是否满足所有标准化指标")
    performance_summary: str = Field(..., description="性能总结")
    bottleneck: Optional[str] = Field(None, description="未达标的性能瓶颈分析")
    optimization_suggestions: Optional[Dict[str, str]] = Field(None, description="给优化Agent的参数调整建议")
    report_file_path: Optional[str] = Field(None, description="生成的PDF/Word报告路径")
