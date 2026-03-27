# PyAEDT 仿真专家技能库 (Skill Library)

> 本文档由源码自动生成，用于指导 AutoGen Agent 调用 PyAEDT 接口进行 HFSS 天线仿真。

## 环境与工程管理 (environment)
### `Hfss.validate_full_design`
- **参数**: `design, output_dir, ports`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Validate a design based on an expected value and save information to the log file.

### `Hfss.insert_infinite_sphere`
- **参数**: `definition, phi_start, phi_stop, phi_step, theta_start, theta_stop, theta_step, units, custom_radiation_faces, custom_coordinate_system, use_slant_polarization, polarization_angle, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create an infinite sphere.

### `Hfss.insert_near_field_sphere`
- **参数**: `radius, radius_units, phi_start, phi_stop, phi_step, theta_start, theta_stop, theta_step, angle_units, custom_radiation_faces, custom_coordinate_system, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a near field sphere.

### `Hfss.insert_near_field_box`
- **参数**: `u_length, u_samples, v_length, v_samples, w_length, w_samples, units, custom_radiation_faces, custom_coordinate_system, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a near field box.

### `Hfss.insert_near_field_rectangle`
- **参数**: `u_length, u_samples, v_length, v_samples, units, custom_radiation_faces, custom_coordinate_system, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a near field rectangle.

### `Hfss.insert_near_field_line`
- **参数**: `assignment, points, custom_radiation_faces, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a near field line.

### `Hfss.insert_near_field_points`
- **参数**: `input_file, coordinate_system, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a near field line.

### `Hfss3dLayout.validate_full_design`
- **参数**: `name, output_dir, ports`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Validate the design based on the expected value and save the information in the log file.

### `Hfss3dLayout.save_diff_pairs_to_file`
- **参数**: `output_file`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Save differtential pairs definition to a file.

### `Hfss3dLayout.edit_hfss_extents`
- **参数**: `diel_extent_type, diel_extent_horizontal_padding, diel_honor_primitives_on_diel_layers, air_extent_type, air_truncate_model_at_ground_layer, air_vertical_positive_padding, air_vertical_negative_padding, airbox_values_as_dim, air_horizontal_padding`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Edit HFSS 3D Layout extents.

### `Setup3DLayout.export_to_hfss`
- **参数**: `output_file, keep_net_name, unite`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Export the HFSS 3D Layout design to an HFSS 3D design.

### `SetupMaxwell.set_save_fields`
- **参数**: `enable, range_type, subrange_type, start, stop, count, units`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Enable the save fields option in the setup.

### `Monitor.insert_monitor_object_from_dict`
- **参数**: `monitor_dict, mode`
- **模块**: `ansys.aedt.core.visualization.post.monitor_icepak`
- **描述**: Insert a monitor.

### `CommonTemplate.project_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Project name.

### `CommonTemplate.project_name`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: No description provided.

### `CommonTemplate.project`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Project path.

### `CommonTemplate.project`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: No description provided.

### `CommonTemplate.design_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Design name in AEDT.

### `CommonTemplate.design_name`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: No description provided.

### `VirtualComplianceGenerator.project_file`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Project file.

### `VirtualComplianceGenerator.project_file`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: No description provided.

### `VirtualComplianceGenerator.save_configuration`
- **参数**: `output_file`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Save the configuration to a json file.

### `VirtualCompliance.load_project`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Open the aedt project in Electronics Desktop.

### `VirtualCompliance.add_project_info`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Add project information.

### `VirtualCompliance.add_project_info`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: No description provided.

### `VirtualCompliance.project_file`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Project file.

### `VirtualCompliance.project_file`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: No description provided.

### `VirtualCompliance.project_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Project name.

### `ViaDesignExtension.create_design`
- **参数**: `create_design_path`
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.via_design`
- **描述**: Create via design in AEDT

### `ViaDesignExtension.create_design_path`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.via_design`
- **描述**: No description provided.

### `ConfigureLayoutExtension.load_edb_into_hfss3dlayout`
- **参数**: `edb_path`
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.resources.configure_layout.master_ui`
- **描述**: No description provided.

### `ChokeDesignerExtension.save_configuration`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss.choke_designer`
- **描述**: Save choke configuration to JSON file.

### `Modeler3DLayout.merge_design`
- **参数**: `merged_design, x, y, z, rotation`
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Merge a design into another.

### `GeometryOperators.is_projection_inside`
- **参数**: `a1, a2, b1, b2`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Project a segment onto another segment and check if the projected segment is inside it.

### `GeometryOperators.is_point_projection_in_segment`
- **参数**: `p, a, b`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Check if a point projection lies on the segment defined by two points.

### `GeometryOperators.find_closest_points`
- **参数**: `points_list, reference_point, tol`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Given a list of points, finds the closest points to a reference point.

### `Geometries3DLayout.is_closed`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Either if the Geometry is closed or not.

### `Polygons3DLayout.is_closed`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Either if the Geometry is closed or not.

### `Part.insert`
- **参数**: `app`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.parts`
- **描述**: Insert 3D component in AEDT.

### `Antenna.insert`
- **参数**: `app, units`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.parts`
- **描述**: Insert antenna in HFSS SBR+.

### `Person.insert`
- **参数**: `app, motion`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.actors`
- **描述**: Insert the person in HFSS SBR+.

### `Bird.insert`
- **参数**: `app, motion`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.actors`
- **描述**: Insert the bird in HFSS SBR+.

### `Vehicle.insert`
- **参数**: `app, motion`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.actors`
- **描述**: Insert the vehicle in HFSS SBR+.

### `Radar.insert`
- **参数**: `app, motion`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.actors`
- **描述**: Insert radar in the HFSS application instance.

### `MultiPartComponent.insert`
- **参数**: `app, motion`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: Insert the object in HFSS SBR+.

### `MaxwellCircuitComponents.design_libray`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_maxwell_circuit`
- **描述**: Design Library.

### `CircuitComponents.design_type`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Design type.

### `TwinBuilderComponents.design_libray`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_twin_builder`
- **描述**: Design Library.

### `EmitComponents.odesign`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Odesign module.

### `EmitComponents.design_type`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Design type.

### `EmitComponents.design_libray`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Design library.

### `NexximComponents.design_libray`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Design library.

### `NexximComponents.set_sim_option_on_hfss_subcircuit`
- **参数**: `component, option`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Set the simulation option on the HFSS subscircuit.

### `NexximComponents.set_sim_solution_on_hfss_subcircuit`
- **参数**: `component, solution_name`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Set the simulation solution on the HFSS subcircuit.

### `Object3d.face_closest_to_bounding_box`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Return only the face ids of the face closest to the bounding box.

### `Object3d.insert_segment`
- **参数**: `points, segment`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Add a segment to an existing polyline.

### `LayoutComponent.close_edb_object`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Close EDB object.

### `Primitives3D.insert_3d_component`
- **参数**: `input_file, geometry_parameters, material_parameters, design_parameters, coordinate_system, name, password, auxiliary_parameters`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_3d`
- **描述**: Insert a new 3D component.

### `Primitives3D.insert_layout_component`
- **参数**: `input_file, coordinate_system, name, parameter_mapping, layout_coordinate_systems, reference_coordinate_system`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_3d`
- **描述**: Insert a new layout component.

### `GeometryModeler.design_type`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Design type.

### `GeometryModeler.imprint_normal_projection`
- **参数**: `assignment, keep_originals`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Imprint the normal projection of objects over a sheet.

### `GeometryModeler.imprint_vector_projection`
- **参数**: `assignment, vector_points, distance, keep_originals`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Imprint the projection of objects over a sheet with a specified vector and distance.

### `GeometryModeler.load_scdm_in_hfss`
- **参数**: `input_file`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Load a SpaceClaim file in HFSS.

### `GeometryModeler.project_sheet`
- **参数**: `sheet, object, thickness, draft_angle, angle_unit, keep_originals`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Project sheet on an object.

### `GeometryModeler.find_closest_edges`
- **参数**: `start_object, end_object, direction`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Retrieve the two closest edges that are not perpendicular for two objects.

### `GeometryModeler.get_closest_edgeid_to_position`
- **参数**: `position, units`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Get the edge ID closest to a given position.

## 参数与变量管理 (parameters)
### `Setup.enable_expression_cache`
- **参数**: `expressions, report_type, intrinsics, isconvergence, isrelativeconvergence, conv_criteria, use_cache_for_pass, use_cache_for_freq`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Enable an expression cache.

### `SetupCircuit.enable_expression_cache`
- **参数**: `expressions, report_type, intrinsics, isconvergence, isrelativeconvergence, conv_criteria`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Enable a setup expression cache.

### `SetupHFSS.get_derivative_variables`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Return Derivative Enabled variables.

### `SetupHFSSAuto.get_derivative_variables`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Return Derivative Enabled variables.

### `FieldsCalculator.expression_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.fields_calculator`
- **描述**: List of available expressions.

### `FieldsCalculator.add_expression`
- **参数**: `calculation, assignment, name`
- **模块**: `ansys.aedt.core.visualization.post.fields_calculator`
- **描述**: Add named expression.

### `FieldsCalculator.create_expression_file`
- **参数**: `name, operations`
- **模块**: `ansys.aedt.core.visualization.post.fields_calculator`
- **描述**: Create a calculator expression file.

### `FieldsCalculator.expression_plot`
- **参数**: `calculation, assignment, names, setup`
- **模块**: `ansys.aedt.core.visualization.post.fields_calculator`
- **描述**: Create plots defined in the expression catalog.

### `FieldsCalculator.delete_expression`
- **参数**: `name`
- **模块**: `ansys.aedt.core.visualization.post.fields_calculator`
- **描述**: Delete a named expression.

### `FieldsCalculator.is_expression_defined`
- **参数**: `name`
- **模块**: `ansys.aedt.core.visualization.post.fields_calculator`
- **描述**: Check if a named expression exists.

### `FieldsCalculator.is_general_expression`
- **参数**: `name`
- **模块**: `ansys.aedt.core.visualization.post.fields_calculator`
- **描述**: Check if a named expression is general.

### `FieldsCalculator.load_expression_file`
- **参数**: `input_file`
- **模块**: `ansys.aedt.core.visualization.post.fields_calculator`
- **描述**: Load expressions from an external TOML file.

### `FieldsCalculator.validate_expression`
- **参数**: `expression`
- **模块**: `ansys.aedt.core.visualization.post.fields_calculator`
- **描述**: Validate expression file against the schema.

### `FieldsCalculator.get_expressions`
- **参数**: `field_type`
- **模块**: `ansys.aedt.core.visualization.post.fields_calculator`
- **描述**: Get dictionary of available Field Calculator expressions.

### `ReportParametersTemplate.parameter_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Parameter name.

### `ReportParametersTemplate.parameter_name`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: No description provided.

### `VirtualComplianceGenerator.add_erl_parameters`
- **参数**: `design_name, config_file, traces, pins, pass_fail, pass_fail_criteria, name, project`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Add Com parameters computed by SpiSim into the configuration.

### `VirtualComplianceGenerator.add_report_derived_parameter`
- **参数**: `design_name, config_file, parameter, traces, report_type, pass_fail_criteria, name, project`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Add report derived parameters computed by AEDT and python into the configuration.

### `VirtualCompliance.parameters`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Parameters available in the Virtual compliance.

### `VirtualCompliance.parameters`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: No description provided.

### `PostProcessorMaxwell.modify_inception_parameters`
- **参数**: `plot_name, gas_type, gas_pressure, use_inception, potential_u0, potential_k, potential_a, critical_value, streamer_constant, ionization_check, ionization_equation, ionization_dataset`
- **模块**: `ansys.aedt.core.visualization.post.post_maxwell`
- **描述**: Modify inception voltage evaluation parameters.

### `Reports.antenna_parameters`
- **参数**: `expressions, setup, infinite_sphere`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Create an Antenna Parameters Report object.

### `SolutionData.expressions`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: Expressions.

### `SolutionData.get_expression_data`
- **参数**: `expression, formula, convert_to_SI, use_quantity, sweeps`
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: Retrieve the real part of the data for an expression.

### `COMParameters.parameters`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.spisim_com_configuration_files.com_parameters`
- **描述**: All parameters.

### `COMParameters.set_parameter`
- **参数**: `keyword, value`
- **模块**: `ansys.aedt.core.visualization.post.spisim_com_configuration_files.com_parameters`
- **描述**: Set a COM parameter.

### `ChokeDesignerExtension.update_parameter_config`
- **参数**: `attr_name, field, entry_widget`
- **模块**: `ansys.aedt.core.extensions.hfss.choke_designer`
- **描述**: Update parameter configuration from entry widget.

### `ChokeDesignerExtension.create_parameter_inputs`
- **参数**: `parent, category_name`
- **模块**: `ansys.aedt.core.extensions.hfss.choke_designer`
- **描述**: Create parameter input widgets for a category.

### `Modeler3DLayout.modeler_variable`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Retrieve a modeler variable.

### `GeometryOperators.cs_xy_pointing_expression`
- **参数**: `yaw, pitch, roll`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Return x_pointing and y_pointing vectors as expressions from the yaw, pitch, and roll input (as strings).

### `Choke.choke_parameters`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.choke`
- **描述**: Get the choke parameters as a dictionary

### `NamedVariable.expression`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Expression of the variable as a string.

### `NamedVariable.expression`
- **参数**: `expression`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Set the expression of the variable.

### `NamedVariable.hide_variable`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Set the variable to a hidden variable.

### `NamedVariable.read_only_variable`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Set the variable to a read-only variable.

### `Radar.speed_expression`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.actors`
- **描述**: Speed variable expression.

### `Radar.speed_expression`
- **参数**: `s`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.actors`
- **描述**: No description provided.

### `Actor.speed_expression`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: Speed variable expression.

### `Actor.speed_expression`
- **参数**: `s`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: No description provided.

### `CircuitComponent.parameters`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Circuit Parameters.

### `UserDefinedComponent.parameters`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Component parameters.

### `GeometryModeler.modeler_variable`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Modeler variable.

## 3D 建模与几何体 (modeling)
### `Hfss.create_sbr_custom_array_file`
- **参数**: `output_file, frequencies, element_number, state_number, position, x_axis, y_axis, weight`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create custom array file with sarr format.

### `Hfss.create_3d_component_array`
- **参数**: `input_data, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a 3D component array from a dictionary.

### `Hfss.set_material_threshold`
- **参数**: `threshold`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Set the material conductivity threshold.

### `NativeComponentPCB.board_cutout_material`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Material applied to cutout regions.

### `NativeComponentPCB.via_holes_material`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Material applied to via hole regions.

### `NativeComponentPCB.board_cutout_material`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Set material to apply to cutout regions.

### `NativeComponentPCB.via_holes_material`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Set material to apply to via hole regions.

### `PCBSettingsDeviceParts.surface_material`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Surface material to apply to parts.

### `PCBSettingsDeviceParts.surface_material`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Set surface material to apply to parts.

### `ModelerNexxim.move`
- **参数**: `assignment, offset, units`
- **模块**: `ansys.aedt.core.modeler.schematic`
- **描述**: Move the selections by the specified ``[x, y]`` coordinates.

### `ModelerNexxim.rotate`
- **参数**: `assignment, degrees`
- **模块**: `ansys.aedt.core.modeler.schematic`
- **描述**: Rotate the selections by degrees.

### `Modeler3DLayout.subtract`
- **参数**: `blank, tool`
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Subtract objects from one or more names.

### `Modeler3DLayout.unite`
- **参数**: `assignment`
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Unite objects from names.

### `GeometryOperators.v_rotate_about_axis`
- **参数**: `vector, angle, radians, axis`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Evaluate rotation of a vector around an axis.

### `GeometryOperators.arrays_positions_sum`
- **参数**: `vertlist1, vertlist2`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Return the sum of two vertices lists.

### `Primitives3DLayout.defaultmaterial`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Default materials.

### `Primitives3DLayout.create_rectangle`
- **参数**: `layer, origin, sizes, corner_radius, angle, name, net`
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Create a rectangle on a layer.

### `Line3dLayout.remove`
- **参数**: `point`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Remove one or more points from the center line.

### `Points3dLayout.move`
- **参数**: `location`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Move actual point to new location.

### `Padstack.remove`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Remove the padstack in AEDT.

### `Part.rotate_origin`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.parts`
- **描述**: Origin rotation list.

### `Part.do_rotate`
- **参数**: `app, aedt_object`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.parts`
- **描述**: Set the rotation coordinate system relative to the parent coordinate system.

### `DuplicatedParametrizedMaterial.material`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: No description provided.

### `DuplicatedParametrizedMaterial.material_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: No description provided.

### `Layer3D.material_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Material name.

### `Layer3D.material`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Material.

### `Layer3D.duplicated_material`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Duplicated material.

### `Layer3D.filling_material`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Fill material.

### `Layer3D.filling_material_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Fill material name.

### `Layer3D.duplicate_parametrize_material`
- **参数**: `material_name, cloned_material_name, list_of_properties`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Duplicate a material and parametrize all properties.

### `Stackup3D.duplicated_material_list`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: List of all duplicated material.

### `CommonObject.material_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Material name.

### `EmitComponent.move_and_connect_to`
- **参数**: `component`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Move and connect this component to another component.

### `Object3d.surface_material_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Surface material name of the object.

### `Object3d.material_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Material name of the object.

### `Object3d.material_name`
- **参数**: `mat`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: No description provided.

### `Object3d.surface_material_name`
- **参数**: `mat`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: No description provided.

### `Object3d.material_appearance`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Material appearance property of the part.

### `Object3d.material_appearance`
- **参数**: `material_appearance`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: No description provided.

### `Object3d.unite`
- **参数**: `assignment`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Unite a list of objects with this object.

### `Object3d.rotate`
- **参数**: `axis, angle, units`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Rotate the selection.

### `Object3d.move`
- **参数**: `vector`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Move objects from a list.

### `Object3d.subtract`
- **参数**: `tool_list, keep_originals`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Subtract one or more parts from the object.

### `Object3d.remove_point`
- **参数**: `position, tolerance`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Remove a point from an existing polyline by position.

### `Object3d.remove_segments`
- **参数**: `assignment`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Remove a segment from an existing polyline by segment id.

### `UserDefinedComponent.rotate`
- **参数**: `axis, angle, units`
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Rotate the selection.

### `UserDefinedComponent.move`
- **参数**: `vector`
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Move component from a list.

### `Primitives2D.create_rectangle`
- **参数**: `origin, sizes, is_covered, name, material, non_model`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_2d`
- **描述**: Create a rectangle.

### `Primitives3D.create_box`
- **参数**: `origin, sizes, name, material`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_3d`
- **描述**: Create a box.

### `Primitives3D.create_cylinder`
- **参数**: `orientation, origin, radius, height, num_sides, name, material`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_3d`
- **描述**: Create a cylinder.

### `Primitives3D.create_sphere`
- **参数**: `origin, radius, name, material`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_3d`
- **描述**: Create a sphere.

### `Primitives3D.create_rectangle`
- **参数**: `orientation, origin, sizes, name, material, is_covered`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_3d`
- **描述**: Create a rectangle.

### `EdgePrimitive.move_along_normal`
- **参数**: `offset`
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Move this edge.

### `FacePrimitive.move_with_offset`
- **参数**: `offset`
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Move the face along the normal.

### `FacePrimitive.move_with_vector`
- **参数**: `vector`
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Move the face along a vector.

### `GeometryModeler.materials`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Material library used in the project.

### `GeometryModeler.defaultmaterial`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Default material.

### `GeometryModeler.get_objects_by_material`
- **参数**: `material`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Get a list of objects either of a specified material or classified by material.

### `GeometryModeler.move`
- **参数**: `assignment, vector`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Move objects from a list.

### `GeometryModeler.rotate`
- **参数**: `assignment, axis, angle, units`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Rotate the selection.

### `GeometryModeler.subtract`
- **参数**: `blank_list, tool_list, keep_originals`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Subtract objects.

### `GeometryModeler.unite`
- **参数**: `assignment, purge, keep_originals`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Unite objects from a list.

### `GeometryModeler.chassis_subtraction`
- **参数**: `chassis_part`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Subtract all non-vacuum objects from the main chassis object.

### `GeometryModeler.explicitly_subtract`
- **参数**: `tool_parts, blank_parts`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Explicitly subtract all elements in a SolveInside list and a SolveSurface list.

### `GeometryModeler.get_faces_from_materials`
- **参数**: `filter_materials`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Select all outer faces given a list of materials.

### `GeometryModeler.move_face`
- **参数**: `assignment, offset`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Move an input face or a list of input faces of a specific object.

### `GeometryModeler.move_edge`
- **参数**: `assignment, offset`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Move an input edge or a list of input edges of a specific object.

### `ComponentArray.export_array_info`
- **参数**: `output_file`
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: Export array information to a CSV file.

### `ComponentArray.parse_array_info_from_csv`
- **参数**: `input_file`
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: Parse component array information from the CSV file.

### `ComponentArray.edit_array`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: Edit component array.

## 边界条件与材料 (boundaries)
### `Hfss.assign_perfect_e`
- **参数**: `assignment, is_infinite_ground, height_deviation, roughness, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Assign perfect electric boundary to one or more objects or faces.

### `Hfss.create_boundary`
- **参数**: `boundary_type, assignment, name, is_inifinite_ground`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Assign a boundary condition to a sheet or surface.

### `Hfss.assign_radiation_boundary_to_objects`
- **参数**: `assignment, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Assign a radiation boundary to one or more objects (usually airbox objects).

### `Hfss.assign_radiation_boundary_to_faces`
- **参数**: `assignment, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Assign a radiation boundary to one or more faces.

### `Hfss3dLayout.create_pec_on_component_by_nets`
- **参数**: `component, nets`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Create a PEC connection on a component for a list of nets.

### `NetworkObject.boundary_nodes`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Get boundary nodes.

### `NetworkObject.add_boundary_node`
- **参数**: `name, assignment_type, value`
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Add a boundary node to the network.

### `NativeComponentPCB.set_high_side_radiation`
- **参数**: `enabled, surface_material, radiate_to_ref_temperature, view_factor, ref_temperature`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Set high side radiation properties.

### `NativeComponentPCB.set_low_side_radiation`
- **参数**: `enabled, surface_material, radiate_to_ref_temperature, view_factor, ref_temperature`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Set low side radiation properties.

### `FarFieldSetup.use_custom_radiation_surface`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: Set/Get the Far Field Radiation Surface Enable.

### `FarFieldSetup.use_custom_radiation_surface`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: No description provided.

### `FarFieldSetup.custom_radiation_surface`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: Set/Get the Far Field Radiation Surface FaceList.

### `FarFieldSetup.custom_radiation_surface`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: No description provided.

### `VirtualCompliance.add_specs_info`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Add specification information.

### `VirtualCompliance.add_specs_info`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: No description provided.

### `VirtualCompliance.specs_folder`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Add specification folder.

### `VirtualCompliance.specs_folder`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: No description provided.

### `VirtualCompliance.add_specs_to_report`
- **参数**: `folder`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Add specs to the report from a given folder.

### `Reports.spectral`
- **参数**: `expressions, setup`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Create a Spectral Report object.

### `PostProcessorIcepak.evaluate_boundary_quantity`
- **参数**: `boundary, quantity, side, volume, setup_name, variations, ref_temperature, time`
- **模块**: `ansys.aedt.core.visualization.post.post_icepak`
- **描述**: Export the field output on a boundary.

## 激励与端口设置 (excitations)
### `Hfss.create_spiral_lumped_port`
- **参数**: `assignment, reference, width, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a spiral lumped port between two adjacent objects.

### `Hfss.create_source_excitation`
- **参数**: `assignment, point1, point2, name, source_type`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a source excitation.

### `Hfss.create_floquet_port`
- **参数**: `assignment, lattice_origin, lattice_a_end, lattice_b_end, modes, name, renormalize, deembed_distance, reporter_filter, lattice_cs`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a floquet port on a face.

### `Hfss.thicken_port_sheets`
- **参数**: `assignment, value, extrude_internally, internal_extrusion`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create thickened sheets over a list of input port sheets.

### `Hfss.create_qfactor_report`
- **参数**: `project_dir, output, setup, name, x_axis`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Export a CSV file of the EigenQ plot.

### `Hfss.set_phase_center_per_port`
- **参数**: `coordinate_system`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Set phase center per port.

### `Hfss.circuit_port`
- **参数**: `assignment, reference, port_location, impedance, name, renormalize, renorm_impedance, deembed`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a circuit port from two objects.

### `Hfss.lumped_port`
- **参数**: `assignment, reference, create_port_sheet, port_on_plane, integration_line, impedance, name, renormalize, deembed, terminals_rename`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a waveport taking the closest edges of two objects.

### `Hfss.wave_port`
- **参数**: `assignment, reference, create_port_sheet, create_pec_cap, integration_line, port_on_plane, modes, impedance, name, renormalize, deembed, is_microstrip, vfactor, hfactor, terminals_rename, characteristic_impedance`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a waveport from a sheet (``start_object``) or taking the closest edges of two objects.

### `Hfss.export_element_pattern`
- **参数**: `frequencies, setup, sphere, variations, element_name, output_dir`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Export the element pattern.

### `Hfss.export_antenna_metadata`
- **参数**: `frequencies, setup, sphere, variations, output_dir, export_element_pattern, export_objects, export_touchstone, export_power`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Export the element pattern.

### `Hfss.export_touchstone_on_completion`
- **参数**: `export, output_dir`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Enable or disable the automatic export of the touchstone file after completing frequency sweep.

### `Hfss.set_export_touchstone`
- **参数**: `file_format, enforce_passivity, enforce_causality, use_common_ground, show_gamma_comments, renormalize, impedance, fitting_error, maximum_poles, passivity_type, column_fitting_type, state_space_fitting, relative_error_tolerance, ensure_accurate_fit, touchstone_output, units, precision`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Set or disable the automatic export of the touchstone file after completing frequency sweep.

### `Hfss.import_table`
- **参数**: `input_file, name, is_real_imag, is_field, column_names, independent_columns`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Import a data table.

### `Hfss3dLayout.create_edge_port`
- **参数**: `assignment, edge_number, is_circuit_port, is_wave_port, wave_horizontal_extension, wave_vertical_extension, wave_launcher, reference_primitive, reference_edge_number`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Create an edge port.

### `Hfss3dLayout.create_wave_port`
- **参数**: `assignment, edge_number, wave_horizontal_extension, wave_vertical_extension, wave_launcher`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Create a single-ended wave port.

### `Hfss3dLayout.create_wave_port_from_two_conductors`
- **参数**: `assignment, edge_numbers`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Create a wave port.

### `Hfss3dLayout.create_ports_by_nets`
- **参数**: `nets`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Create the ports for a list of nets.

### `Hfss3dLayout.create_ports_on_component_by_nets`
- **参数**: `component, nets`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Create the ports on a component for a list of nets.

### `Hfss3dLayout.create_differential_port`
- **参数**: `via_signal, via_reference, name, deembed`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Create a differential port.

### `Hfss3dLayout.create_coax_port`
- **参数**: `via, radial_extent, layer, alignment`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Create a coax port.

### `Hfss3dLayout.create_pin_port`
- **参数**: `name, x, y, rotation, top_layer, bottom_layer`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Create a pin port.

### `Hfss3dLayout.delete_port`
- **参数**: `name, remove_geometry`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Delete a port.

### `Hfss3dLayout.import_edb`
- **参数**: `input_folder`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Import EDB.

### `Hfss3dLayout.set_export_touchstone`
- **参数**: `file_format, enforce_passivity, enforce_causality, use_common_ground, show_gamma_comments, renormalize, impedance, fitting_error, maximum_poles, passivity_type, column_fitting_type, state_space_fitting, relative_error_tolerance, ensure_accurate_fit, touchstone_output, units, precision`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Set or disable the automatic export of the touchstone file after completing frequency sweep.

### `Hfss3dLayout.import_gds`
- **参数**: `input_file, output_dir, control_file, set_as_active, close_active_project`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Import a GDS file into HFSS 3D Layout and assign the stackup from an XML file if present.

### `Hfss3dLayout.import_dxf`
- **参数**: `input_file, output_dir, control_file, set_as_active, close_active_project`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Import a DXF file into HFSS 3D Layout and assign the stackup from an XML file if present.

### `Hfss3dLayout.import_gerber`
- **参数**: `input_file, output_dir, control_file, set_as_active, close_active_project`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Import a Gerber zip file into HFSS 3D Layout and assign the stackup from an XML file if present.

### `Hfss3dLayout.import_brd`
- **参数**: `input_file, output_dir, set_as_active, close_active_project, control_file`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Import a board file into HFSS 3D Layout and assign the stackup from an XML file if present.

### `Hfss3dLayout.import_awr`
- **参数**: `input_file, output_dir, control_file, set_as_active, close_active_project`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Import an AWR Microwave Office file into HFSS 3D Layout and assign the stackup from an XML file if present.

### `Hfss3dLayout.import_ipc2581`
- **参数**: `input_file, output_dir, control_file, set_as_active, close_active_project`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Import an IPC2581 file into HFSS 3D Layout and assign the stackup from an XML file if present.

### `Hfss3dLayout.import_odb`
- **参数**: `input_file, output_dir, control_file, set_as_active, close_active_project`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Import an ODB++ file into HFSS 3D Layout and assign the stackup from an XML file if present.

### `Hfss3dLayout.export_3d_model`
- **参数**: `output_file`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Export the Ecad model to a 3D file.

### `Hfss3dLayout.export_touchstone_on_completion`
- **参数**: `export, output_dir`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Enable or disable the automatic export of the touchstone file after completing frequency sweep.

### `Hfss3dLayout.import_table`
- **参数**: `input_file, link, header_rows, rows_to_read, column_separator, data_type, sweep_columns, total_columns, real_columns`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Import a data table as a solution.

### `Hfss3dLayout.delete_imported_data`
- **参数**: `name`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Delete imported data.

### `CommonSetup.create_report`
- **参数**: `expressions, domain, variations, primary_sweep_variable, secondary_sweep_variable, report_category, plot_type, context, subdesign_id, polyline_points, name, sweep`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Create a report in AEDT. It can be a 2D plot, 3D plot, polar plot, or data table.

### `SetupCircuit.create_report`
- **参数**: `expressions, domain, variations, primary_sweep_variable, secondary_sweep_variable, report_category, plot_type, context, subdesign_id, polyline_points, name`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Create a report in AEDT. It can be a 2D plot, 3D plot, polar plots or data tables.

### `Setup3DLayout.export_to_q3d`
- **参数**: `output_file, keep_net_name, unite`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Export the HFSS 3D Layout design to a Q3D design.

### `Setup3DLayout.import_from_json`
- **参数**: `file_path`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Import setup properties from a json file.

### `Setup3DLayout.export_to_json`
- **参数**: `file_path, overwrite`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Export all setup properties into a json file.

### `SetupMaxwell.export_matrix`
- **参数**: `matrix_type, matrix_name, output_file, is_format_default, width, precision, is_exponential, setup, default_adaptive, is_post_processed`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Export R/L or Capacitance matrix after solving.

### `SpiSim.export_com_configure_file`
- **参数**: `file_path, standard`
- **模块**: `ansys.aedt.core.visualization.post.spisim`
- **描述**: Generate a configuration file for SpiSim.

### `FieldsCalculator.export`
- **参数**: `quantity, solution, variations, output_file, intrinsics, phase, sample_points, export_with_sample_points, reference_coordinate_system, export_in_si_system, export_field_in_reference, grid_type, grid_center, grid_start, grid_stop, grid_step, is_vector, assignment, objects_type`
- **模块**: `ansys.aedt.core.visualization.post.fields_calculator`
- **描述**: Export the field quantity at the top of the register to a file, mapping it to a grid of points.

### `FieldPlot.export_image`
- **参数**: `full_path, width, height, orientation, display_wireframe, selections, show_region, show_axis, show_grid, show_ruler`
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Export the active plot to an image file.

### `FieldPlot.export_image_from_aedtplt`
- **参数**: `export_path, view, plot_mesh, scale_min, scale_max`
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Save an image of the active plot using PyVista.

### `FfdSolutionDataExporter.export_farfield`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.farfield_exporter`
- **描述**: Export far field solution data of each element.

### `FieldSummary.export_csv`
- **参数**: `output_file, setup, variations, intrinsics`
- **模块**: `ansys.aedt.core.visualization.post.field_summary`
- **描述**: Get the field summary output computation.

### `PostProcessorCircuit.export_model_picture`
- **参数**: `output_file, page, width, height`
- **模块**: `ansys.aedt.core.visualization.post.post_circuit`
- **描述**: Export a snapshot of the schematic to a ``JPG`` file.

### `MonostaticRCSExporter.export_rcs`
- **参数**: `name, metadata_name, only_geometry`
- **模块**: `ansys.aedt.core.visualization.post.rcs_exporter`
- **描述**: Export RCS solution data.

### `VRTFieldPlot.export`
- **参数**: `path`
- **模块**: `ansys.aedt.core.visualization.post.vrt_data`
- **描述**: Export the Visual Ray Tracing to ``hdm`` file.

### `CommonTemplate.report_type`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Report type.

### `CommonTemplate.report_type`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: No description provided.

### `VirtualComplianceGenerator.add_report`
- **参数**: `design_name, config_file, traces, report_type, pass_fail, group_plots, name, project`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Add Com parameters computed by SpiSim into the configuration.

### `VirtualComplianceGenerator.add_report_from_folder`
- **参数**: `input_folder, design_name, group_plots, project`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Add multiple reports from a folder.

### `VirtualCompliance.reports`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Reports available in the virtual compliance.

### `VirtualCompliance.reports`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: No description provided.

### `VirtualCompliance.use_portrait`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Use portrait.

### `VirtualCompliance.use_portrait`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: No description provided.

### `VirtualCompliance.add_aedt_report`
- **参数**: `name, report_type, config_file, design_name, traces, setup_name, pass_fail, pass_fail_criteria`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Add a new custom aedt report to the compliance.

### `VirtualCompliance.create_compliance_report`
- **参数**: `file_name, close_project`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Create the Virtual Compliance report.

### `VirtualCompliance.compute_report_data`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Compute the report data and exports all the images and table without creating the pdf.

### `PostProcessorMaxwell.export_inception_voltage`
- **参数**: `plot_name, output_file, field_line_number`
- **模块**: `ansys.aedt.core.visualization.post.post_maxwell`
- **描述**: Export inception voltage evaluation results to a TXT file.

### `PostProcessorCommon.available_report_types`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Report types.

### `PostProcessorCommon.update_report_dynamically`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Get/Set the boolean to automatically update reports on edits.

### `PostProcessorCommon.update_report_dynamically`
- **参数**: `value`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: No description provided.

### `PostProcessorCommon.available_report_quantities`
- **参数**: `report_category, display_type, solution, quantities_category, context, is_siwave_dc, differential_pairs`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Compute the list of all available report quantities of a given report quantity category.

### `PostProcessorCommon.get_all_report_quantities`
- **参数**: `solution, context, is_siwave_dc`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Return all the possible report categories organized by report types, solution and categories.

### `PostProcessorCommon.available_report_solutions`
- **参数**: `report_category`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Get the list of available solutions that can be used for the reports.

### `PostProcessorCommon.oreportsetup`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Report setup.

### `PostProcessorCommon.all_report_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: List of all report names.

### `PostProcessorCommon.copy_report_data`
- **参数**: `plot_name, paste`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Copy report data as static data.

### `PostProcessorCommon.paste_report_data`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Paste report data as static data.

### `PostProcessorCommon.delete_report`
- **参数**: `plot_name`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Delete all reports or specific report.

### `PostProcessorCommon.rename_report`
- **参数**: `plot_name, new_name`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Rename a plot.

### `PostProcessorCommon.export_report_to_file`
- **参数**: `output_dir, plot_name, extension, unique_file, uniform, start, end, step, use_trace_number_format`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Export a 2D Plot data to a file.

### `PostProcessorCommon.export_report_to_csv`
- **参数**: `project_dir, plot_name, uniform, start, end, step, use_trace_number_format`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Export the 2D Plot data to a CSV file.

### `PostProcessorCommon.export_report_to_jpg`
- **参数**: `project_path, plot_name, width, height, image_format`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Export plot to an image file.

### `PostProcessorCommon.create_report`
- **参数**: `expressions, setup_sweep_name, domain, variations, primary_sweep_variable, secondary_sweep_variable, report_category, plot_type, context, subdesign_id, polyline_points, plot_name`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Create a report in AEDT. It can be a 2D plot, 3D plot, polar plot, or a data table.

### `PostProcessorCommon.create_report_from_configuration`
- **参数**: `input_file, report_settings, solution_name, name, matplotlib, show`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Create a report based on a JSON file, TOML file, RPT file, or dictionary of properties.

### `PostProcessor3D.ofieldsreporter`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Fields reporter.

### `PostProcessor3D.export_field_file_on_grid`
- **参数**: `quantity, solution, variations, file_name, grid_type, grid_center, grid_start, grid_stop, grid_step, is_vector, intrinsics, phase, export_with_sample_points, reference_coordinate_system, export_in_si_system, export_field_in_reference`
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Use the field calculator to create a field file on a grid based on a solution and variation.

### `PostProcessor3D.export_field_file`
- **参数**: `quantity, solution, variations, output_file, assignment, objects_type, intrinsics, phase, sample_points_file, sample_points, export_with_sample_points, reference_coordinate_system, export_in_si_system, export_field_in_reference`
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Use the field calculator to create a field file based on a solution and variation.

### `PostProcessor3D.export_field_plot`
- **参数**: `plot_name, output_dir, file_name, file_format`
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Export a field plot.

### `PostProcessor3D.export_field_jpg`
- **参数**: `file_name, plot_name, folder_name, orientation, width, height, display_wireframe, selections, show_axis, show_grid, show_ruler, show_region`
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Export a field plot and coordinate system to a JPG file.

### `PostProcessor3D.export_model_picture`
- **参数**: `full_name, show_axis, show_grid, show_ruler, show_region, selections, field_selections, orientation, width, height`
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Export a snapshot of the model to a ``JPG`` file.

### `PostProcessor3D.export_model_obj`
- **参数**: `assignment, export_path, export_as_multiple_objects, air_objects`
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Export the model.

### `PostProcessor3D.export_mesh_obj`
- **参数**: `setup, intrinsics, export_air_objects, on_surfaces`
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Export the mesh in AEDTPLT format.

### `SolutionData.export_data_to_csv`
- **参数**: `output, delimiter`
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: Save to output csv file the Solution Data.

### `SolutionData.get_report_plotter`
- **参数**: `curves, formula, to_radians, props`
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: Get the `ReportPlotter` on the specified curves.

### `COMParameters.export`
- **参数**: `file_path`
- **模块**: `ansys.aedt.core.visualization.post.spisim_com_configuration_files.com_parameters`
- **描述**: Export COM parameter to a JSON file.

### `COMParameters.export_spisim_cfg`
- **参数**: `file_path`
- **模块**: `ansys.aedt.core.visualization.post.spisim_com_configuration_files.com_parameters`
- **描述**: Export COM parameter to a SPISim cfg file.

### `ViaDesignExtension.export_examples`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.via_design`
- **描述**: No description provided.

### `ConfigureLayoutExtension.export_config_from_edb`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.resources.configure_layout.master_ui`
- **描述**: No description provided.

### `Modeler3DLayout.import_cadence_brd`
- **参数**: `input_file, output_dir, name`
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Import a cadence board.

### `Modeler3DLayout.import_ipc2581`
- **参数**: `input_file, output_dir, name`
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Import an IPC file.

### `Modeler3D.import_nastran`
- **参数**: `file_path, import_lines, lines_thickness, import_as_light_weight, decimation, group_parts, enable_planar_merge, save_only_stl, preview, merge_angle, remove_multiple_connections`
- **模块**: `ansys.aedt.core.modeler.modeler_3d`
- **描述**: Import Nastran file into 3D Modeler by converting the faces to stl and reading it.

### `Modeler3D.import_from_openstreet_map`
- **参数**: `latitude_longitude, env_name, terrain_radius, include_osm_buildings, including_osm_roads, import_in_aedt, plot_before_importing, z_offset, road_step, road_width, create_lightweight_part`
- **模块**: `ansys.aedt.core.modeler.modeler_3d`
- **描述**: Import OpenStreet Maps into AEDT.

### `Components3DLayout.port_properties`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Get port properties from component.

### `Components3DLayout.port_properties`
- **参数**: `values`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `Choke.export_to_json`
- **参数**: `file_path`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.choke`
- **描述**: Export choke configuration to JSON file.

### `Choke.create_ports`
- **参数**: `ground, app`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.choke`
- **描述**: Create the ports.

### `Patch.create_probe_port`
- **参数**: `reference_layer, rel_x_offset, rel_y_offset, r, name`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Create a coaxial probe port for the patch.

### `Patch.create_lumped_port`
- **参数**: `reference_layer, opposite_side, port_name, axisdir`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Create a parametrized lumped port.

### `Trace.create_lumped_port`
- **参数**: `reference_layer, opposite_side, port_name, axisdir`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Create a parametrized lumped port.

### `CircuitComponents.add_pin_iports`
- **参数**: `name, id_num`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Add ports on pins.

### `CircuitComponents.create_interface_port`
- **参数**: `name, location, angle, page`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Create an interface port.

### `CircuitComponents.create_page_port`
- **参数**: `name, location, angle, label_position, page`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Create a page port.

### `EmitComponent.port_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Get the names of the component's ports.

### `EmitComponent.port_connection`
- **参数**: `port_name`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Get the name component and port connected to the given port.

### `NexximComponents.create_voltage_probe`
- **参数**: `name, location, angle, use_instance_id_netlist, page`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Create a voltage probe.

### `NexximComponents.create_current_probe`
- **参数**: `name, location, angle, use_instance_id_netlist, page`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Create a current probe.

### `Object3d.export_image`
- **参数**: `output_file`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Export the current object to a specified file path.

### `GeometryModeler.model_consistency_report`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Summary of detected inconsistencies between the AEDT modeler and PyAEDT structures.

### `GeometryModeler.find_port_faces`
- **参数**: `assignment`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Find the vacuums given a list of input sheets.

### `GeometryModeler.export_3d_model`
- **参数**: `file_name, file_path, file_format, assignment_to_export, assignment_to_remove, major_version, minor_version`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Export the 3D model.

### `GeometryModeler.import_3d_cad`
- **参数**: `input_file, healing, refresh_all_ids, import_materials, create_lightweight_part, group_by_assembly, create_group, separate_disjoints_lumped_object, import_free_surfaces, point_coincidence_tolerance, reduce_stl, reduce_percentage, reduce_error, merge_planar_faces, merge_angle, input_file_unit`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Import a CAD model.

### `GeometryModeler.import_spaceclaim_document`
- **参数**: `input_file`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Import a SpaceClaim document.

### `GeometryModeler.import_discovery_model`
- **参数**: `input_file`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Import a Discovery file.

### `GeometryModeler.import_primitives_from_file`
- **参数**: `input_file, primitives`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Import and create primitives from a JSON file or dictionary of properties.

### `GeometryModeler.get_edges_for_circuit_port_from_sheet`
- **参数**: `assignment, xy_plane, yz_plane, xz_plane, allow_perpendicular, tolerance`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Retrieve two edge IDs that are suitable for a circuit port from a sheet.

### `GeometryModeler.get_edges_for_circuit_port`
- **参数**: `assignment, xy_plane, yz_plane, xz_plane, allow_perpendicular, tolerance`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Retrieve two edge IDs suitable for the circuit port.

## 求解与网格设置 (setup)
### `Hfss.field_setups`
- **参数**: ``
- **模块**: `ansys.aedt.core.hfss`
- **描述**: List of AEDT radiation fields.

### `Hfss.field_setup_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.hfss`
- **描述**: List of AEDT radiation field names.

### `Hfss.create_setup`
- **参数**: `name, setup_type`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create an analysis setup for HFSS.

### `Hfss.create_linear_count_sweep`
- **参数**: `setup, unit, start_frequency, stop_frequency, num_of_freq_points, name, save_fields, save_rad_fields, sweep_type, interpolation_tol, interpolation_max_solutions`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a sweep with a specified number of points.

### `Hfss.create_linear_step_sweep`
- **参数**: `setup, unit, start_frequency, stop_frequency, step_size, name, save_fields, save_rad_fields, sweep_type`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a sweep with a specified frequency step.

### `Hfss.create_single_point_sweep`
- **参数**: `setup, unit, freq, name, save_single_field, save_fields, save_rad_fields`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a sweep with a single frequency point.

### `Hfss.sar_setup`
- **参数**: `assignment, tissue_mass, material_density, voxel_size, average_sar_method`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Define SAR settings.

### `Hfss.create_sbr_chirp_i_doppler_setup`
- **参数**: `time_variable, sweep_time_duration, center_freq, resolution, period, velocity_resolution, min_velocity, max_velocity, ray_density_per_wavelength, max_bounces, include_coupling_effects, doppler_ad_sampling_rate, setup`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create an SBR+ Chirp I setup.

### `Hfss.create_sbr_chirp_iq_doppler_setup`
- **参数**: `time_variable, sweep_time_duration, center_freq, resolution, period, velocity_resolution, min_velocity, max_velocity, ray_density_per_wavelength, max_bounces, include_coupling_effects, doppler_ad_sampling_rate, setup`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create an SBR+ Chirp IQ setup.

### `Hfss.create_sbr_pulse_doppler_setup`
- **参数**: `time_variable, sweep_time_duration, frequency, resolution, period, velocity_resolution, min_velocity, max_velocity, ray_density_per_wavelength, max_bounces, setup`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create an SBR+ pulse Doppler setup.

### `Hfss.set_mesh_fusion_settings`
- **参数**: `assignment, volume_padding, priority`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Set mesh fusion settings in HFSS.

### `Hfss3dLayout.set_meshing_settings`
- **参数**: `mesh_method, enable_intersections_check, use_alternative_fallback`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Define the settings of the mesh.

### `Hfss3dLayout.create_linear_count_sweep`
- **参数**: `setup, unit, start_frequency, stop_frequency, num_of_freq_points, name, save_fields, save_rad_fields_only, sweep_type, interpolation_tol_percent, interpolation_max_solutions, use_q3d_for_dc`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Create a sweep with the specified number of points.

### `Hfss3dLayout.create_linear_step_sweep`
- **参数**: `setup, unit, start_frequency, stop_frequency, step_size, name, save_fields, save_rad_fields_only, sweep_type, interpolation_tol_percent, interpolation_max_solutions, use_q3d_for_dc`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Create a sweep with the specified frequency step.

### `Hfss3dLayout.create_single_point_sweep`
- **参数**: `setup, unit, freq, name, save_fields, save_rad_fields_only`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Create a sweep with a single frequency point.

### `Hfss3dLayout.get_model_from_mesh_results`
- **参数**: `binary`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Get the path for the parasolid file in the result folder.

### `Hfss3dLayout.get_dcir_solution_data`
- **参数**: `setup, show, category`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Retrieve dcir solution data. Available element_names are dependent on element_type as below.

### `SetupKeys.get_setup_templates`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.setup_templates`
- **描述**: No description provided.

### `CommonSetup.sweeps`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: No description provided.

### `CommonSetup.analyze`
- **参数**: `cores, tasks, gpus, acf_file, use_auto_settings, solve_in_batch, machine, run_in_thread, revert_to_initial_mesh, blocking`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Solve the active design.

### `CommonSetup.get_solution_data`
- **参数**: `expressions, domain, variations, primary_sweep_variable, report_category, context, polyline_points, math_formula, sweep`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Get a simulation result from a solved setup and cast it in a ``SolutionData`` object.

### `Setup.add_mesh_link`
- **参数**: `design, solution, parameters, project, force_source_to_solve, preserve_partner_solution, apply_mesh_operations, adapt_port`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Import mesh from a source design solution to the target design.

### `Setup.start_continue_from_previous_setup`
- **参数**: `design, solution, map_variables_by_name, parameters, project, force_source_to_solve, preserve_partner_solution`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Start or continue from a previously solved setup.

### `SetupCircuit.add_sweep_points`
- **参数**: `sweep_variable, sweep_points, units, override_existing_sweep`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Add a linear count sweep to existing Circuit Setup.

### `SetupCircuit.add_sweep_count`
- **参数**: `sweep_variable, start, stop, count, units, count_type, override_existing_sweep`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Add a step sweep to existing Circuit Setup. It can be ``"Linear"``, ``"Decade"`` or ``"Octave"``.

### `SetupCircuit.add_sweep_step`
- **参数**: `sweep_variable, start, stop, step_size, units, override_existing_sweep`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Add a linear count sweep to existing Circuit Setup.

### `SetupCircuit.get_solution_data`
- **参数**: `expressions, domain, variations, primary_sweep_variable, report_category, context, polyline_points, math_formula, sweep`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Get a simulation result from a solved setup and cast it in a ``SolutionData`` object.

### `Setup3DLayout.sweeps`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: No description provided.

### `Setup3DLayout.add_sweep`
- **参数**: `name, sweep_type`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Add a frequency sweep.

### `Setup3DLayout.get_sweep`
- **参数**: `name`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Return frequency sweep object of a given sweep.

### `SetupHFSS.create_frequency_sweep`
- **参数**: `unit, start_frequency, stop_frequency, num_of_freq_points, name, save_fields, save_rad_fields, sweep_type, interpolation_tol, interpolation_max_solutions`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Create a sweep with the specified number of points.

### `SetupHFSS.create_linear_step_sweep`
- **参数**: `unit, start_frequency, stop_frequency, step_size, name, save_fields, save_rad_fields, sweep_type`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Create a Sweep with a specified frequency step.

### `SetupHFSS.create_single_point_sweep`
- **参数**: `unit, freq, name, save_single_field, save_fields, save_rad_fields`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Create a Sweep with a single frequency point.

### `SetupHFSS.add_sweep`
- **参数**: `name, sweep_type`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Add a sweep to the project.

### `SetupHFSS.get_sweep`
- **参数**: `name`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Return frequency sweep object of a given sweep.

### `SetupHFSS.get_sweep_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Get the names of all sweeps in a given analysis setup.

### `SetupHFSS.delete_sweep`
- **参数**: `name`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Delete a sweep.

### `SetupHFSS.enable_adaptive_setup_single`
- **参数**: `freq, max_passes, max_delta_s`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Enable HFSS single frequency setup.

### `SetupHFSS.enable_adaptive_setup_broadband`
- **参数**: `low_frequency, high_frequency, max_passes, max_delta_s`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Enable HFSS broadband setup.

### `SetupHFSS.enable_adaptive_setup_multifrequency`
- **参数**: `frequencies, max_delta_s`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Enable HFSS multi-frequency setup.

### `SetupHFSSAuto.enable_adaptive_setup_single`
- **参数**: `frequency, max_passes, max_delta_s`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Enable HFSS single frequency setup.

### `SetupHFSSAuto.enable_adaptive_setup_broadband`
- **参数**: `low_frequency, high_frequency, max_passes, max_delta_s`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Enable HFSS broadband setup.

### `SetupHFSSAuto.enable_adaptive_setup_multifrequency`
- **参数**: `frequencies, max_delta_s`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Enable HFSS multi-frequency setup.

### `SetupMaxwell.add_eddy_current_sweep`
- **参数**: `sweep_type, start_frequency, stop_frequency, step_size, units, clear, save_all_fields`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Create a Maxwell Eddy Current Sweep.

### `SetupMaxwell.delete_all_eddy_current_sweeps`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Delete all Maxwell Eddy Current sweeps.

### `SetupQ3D.create_frequency_sweep`
- **参数**: `unit, start_frequency, stop_frequency, num_of_freq_points, name, save_fields, sweep_type, interpolation_tol, interpolation_max_solutions`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Create a sweep with the specified number of points.

### `SetupQ3D.create_linear_step_sweep`
- **参数**: `unit, start_frequency, stop_frequency, step_size, name, save_fields, sweep_type`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Create a sweep with a specified frequency step.

### `SetupQ3D.create_single_point_sweep`
- **参数**: `unit, freq, name, save_single_field, save_fields`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Create a sweep with a single frequency point.

### `SetupQ3D.add_sweep`
- **参数**: `name, sweep_type`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Add a sweep to the project.

### `SetupQ3D.get_sweep`
- **参数**: `name`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Get the frequency sweep object of a given sweep.

### `SetupIcepak.start_continue_from_previous_setup`
- **参数**: `design, solution, map_variables_by_name, parameters, project, force_source_to_solve, preserve_partner_solution, frozen_flow`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Start or continue from a previously solved setup.

### `PowerSinSource.frequency`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Frequency.

### `PowerSinSource.frequency`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `PowerIQSource.carrier_frequency`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Carrier frequency value.

### `PowerIQSource.carrier_frequency`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `VoltageSinSource.frequency`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Frequency.

### `VoltageSinSource.frequency`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `CurrentSinSource.frequency`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Frequency.

### `CurrentSinSource.frequency`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `NativeComponentPCB.set_resolution`
- **参数**: `resolution`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Set metal fraction mapping resolution.

### `NativeComponentPCB.set_custom_resolution`
- **参数**: `row, col`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Set custom metal fraction mapping resolution.

### `NativeComponentPCB.preserve_partner_solution`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Preserve parner solution option.

### `NativeComponentPCB.preserve_partner_solution`
- **参数**: `val`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Set Whether to preserve partner solution.

### `NativeComponentPCB.preserve_partner_solution`
- **参数**: `val`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Set Whether to preserve partner solution.

### `PostProcessorCommon.post_solution_type`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Design solution type.

### `PostProcessorCommon.get_solution_data_per_variation`
- **参数**: `solution_type, setup_sweep_name, context, sweeps, expressions`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Retrieve solution data for each variation.

### `PostProcessorCommon.get_solution_data`
- **参数**: `expressions, setup_sweep_name, domain, variations, primary_sweep_variable, report_category, context, subdesign_id, polyline_points, math_formula`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Get a simulation result from a solved setup and cast it in a ``SolutionData`` object.

### `Reports.modal_solution`
- **参数**: `expressions, setup`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Create a Standard or Default Report object.

### `Reports.terminal_solution`
- **参数**: `expressions, setup`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Create a Standard or Default Report object.

### `PostProcessor3D.post_osolution`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Solution.

### `SolutionData.primary_sweep`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: Primary sweep.

### `SolutionData.primary_sweep`
- **参数**: `ps`
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: No description provided.

### `SolutionData.update_sweeps`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: Update sweeps.

### `SolutionData.init_solutions_data`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: Initialize the database and store info in variables.

### `SolutionData.primary_sweep_values`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: Retrieve the primary sweep for a given data and primary variable.

### `GraphSetup.minimum_frequency`
- **参数**: ``
- **模块**: `ansys.aedt.core.filtersolutions_core.graph_setup`
- **描述**: Minimum frequency value for exporting frequency and S parameter responses. The default is ``200 MHz``.

### `GraphSetup.minimum_frequency`
- **参数**: `min_freq_string`
- **模块**: `ansys.aedt.core.filtersolutions_core.graph_setup`
- **描述**: No description provided.

### `GraphSetup.maximum_frequency`
- **参数**: ``
- **模块**: `ansys.aedt.core.filtersolutions_core.graph_setup`
- **描述**: Maximum frequency value for exporting frequency and S parameters responses. The default is ``5 GHz``.

### `GraphSetup.maximum_frequency`
- **参数**: `max_freq_string`
- **模块**: `ansys.aedt.core.filtersolutions_core.graph_setup`
- **描述**: No description provided.

### `Choke.create_mesh`
- **参数**: `app`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.choke`
- **描述**: Create the mesh.

### `Layer3D.frequency`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Frequency variable.

### `Stackup3D.frequency`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Frequency variable.

### `Patch.frequency`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Model frequency.

### `Trace.frequency`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Frequency.

### `Coil.create_sweep_profile`
- **参数**: `start_point, polyline`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.coil`
- **描述**: No description provided.

### `EmitRadioComponent.band_start_frequency`
- **参数**: `band_node, units`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Get the start frequency of the band node.

### `EmitRadioComponent.band_stop_frequency`
- **参数**: `band_node, units`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Get the stop frequency of the band node.

### `EmitRadioComponent.set_band_start_frequency`
- **参数**: `band_node, band_start_freq, units`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Set start frequency of the band.

### `EmitRadioComponent.set_band_stop_frequency`
- **参数**: `band_node, band_stop_freq, units`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Set stop frequency of the band.

### `Object3d.sweep_along_vector`
- **参数**: `sweep_vector, draft_angle, draft_type`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Sweep the selection along a vector.

### `Object3d.sweep_along_path`
- **参数**: `sweep_object, draft_angle, draft_type, is_check_face_intersection, twist_angle`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Sweep the selection along a vector.

### `Object3d.sweep_around_axis`
- **参数**: `axis, sweep_angle, draft_angle`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Sweep around an axis.

### `UserDefinedComponent.mesh_assembly`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Mesh assembly flag.

### `UserDefinedComponent.mesh_assembly`
- **参数**: `ma`
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: No description provided.

### `GeometryModeler.sweep_along_normal`
- **参数**: `assignment, faces, sweep_value`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Sweep the selection along the vector.

### `GeometryModeler.sweep_along_vector`
- **参数**: `assignment, sweep_vector, draft_angle, draft_type`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Sweep the selection along a vector.

### `GeometryModeler.sweep_along_path`
- **参数**: `assignment, sweep_object, draft_angle, draft_type, is_check_face_intersection, twist_angle`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Sweep the selection along a path.

### `GeometryModeler.sweep_around_axis`
- **参数**: `assignment, axis, sweep_angle, draft_angle, number_of_segments`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Sweep the selection around the axis.

## 仿真执行与后处理 (post)
### `Hfss.get_hdm_plotter`
- **参数**: `file_name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Get the HDM plotter.

### `Matrix.get_sources_for_plot`
- **参数**: `get_self_terms, get_mutual_terms, first_element_filter, second_element_filter, category`
- **模块**: `ansys.aedt.core.modules.boundary.q3d_boundary`
- **描述**: Return a list of source of specified matrix ready to be used in plot reports.

### `FieldPlot.plotGeomInfo`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Plot geometry information.

### `FieldPlot.plotsettings`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Plot settings.

### `FieldPlot.surfacePlotInstruction`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Surface plot settings.

### `FieldPlot.surfacePlotInstructionLineTraces`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Surface plot settings for field line traces.

### `FieldPlot.field_plot_settings`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Field Plot Settings.

### `FieldPlot.field_line_trace_plot_settings`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Settings for the field line traces in the plot.

### `FieldPlot.update_field_plot_settings`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Modify the field plot settings.

### `FfdSolutionDataExporter.farfield_data`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.farfield_exporter`
- **描述**: Farfield data.

### `PostProcessor3DLayout.create_fieldplot_layers`
- **参数**: `layers, quantity, setup, nets, plot_on_surface, intrinsics, name`
- **模块**: `ansys.aedt.core.visualization.post.post_3dlayout`
- **描述**: Create a field plot of stacked layer plot.

### `PostProcessor3DLayout.create_fieldplot_nets`
- **参数**: `nets, quantity, setup, layers, plot_on_surface, intrinsics, name`
- **模块**: `ansys.aedt.core.visualization.post.post_3dlayout`
- **描述**: Create a field plot of stacked layer plot based on a net selections.

### `PostProcessor3DLayout.create_fieldplot_layers_nets`
- **参数**: `layers_nets, quantity, setup, intrinsics, plot_on_surface, plot_name`
- **模块**: `ansys.aedt.core.visualization.post.post_3dlayout`
- **描述**: Create a field plot of stacked layer plot on specified matrix of layers and nets.

### `PostProcessorHFSS.create_fieldplot_layers`
- **参数**: `layers, quantity, setup, nets, plot_on_surface, intrinsics, name`
- **模块**: `ansys.aedt.core.visualization.post.post_hfss`
- **描述**: Create a field plot of stacked layer plot.

### `PostProcessorHFSS.create_fieldplot_layers_nets`
- **参数**: `layers_nets, quantity, setup, intrinsics, plot_on_surface, plot_name`
- **模块**: `ansys.aedt.core.visualization.post.post_hfss`
- **描述**: Create a field plot of stacked layer plot on specified matrix of layers and nets.

### `PostProcessorCircuit.create_ami_initial_response_plot`
- **参数**: `setup, ami_name, variation_list_w_value, plot_type, plot_initial_response, plot_intermediate_response, plot_final_response, plot_name`
- **模块**: `ansys.aedt.core.visualization.post.post_circuit`
- **描述**: Create an AMI initial response plot.

### `PostProcessorCircuit.create_ami_statistical_eye_plot`
- **参数**: `setup, ami_name, variation_list_w_value, ami_plot_type, plot_name`
- **模块**: `ansys.aedt.core.visualization.post.post_circuit`
- **描述**: Create an AMI statistical eye plot.

### `PostProcessorCircuit.create_statistical_eye_plot`
- **参数**: `setup, probe_names, variation_list_w_value, plot_name`
- **模块**: `ansys.aedt.core.visualization.post.post_circuit`
- **描述**: Create a statistical QuickEye, VerifEye, and/or Statistical Eye plot.

### `ReportTemplate.group_plots`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Flag indicating if plots are grouped into a single chart or kept independent.

### `ReportTemplate.group_plots`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: No description provided.

### `PostProcessorMaxwell.create_fieldplot_line_traces`
- **参数**: `seeding_faces, in_volume_tracing_objs, surface_tracing_objs, setup, intrinsics, plot_name, field_type`
- **模块**: `ansys.aedt.core.visualization.post.post_maxwell`
- **描述**: Create a field plot of the line.

### `PostProcessorMaxwell.create_fieldplot_layers`
- **参数**: `layers, quantity, setup, nets, plot_on_surface, intrinsics, name`
- **模块**: `ansys.aedt.core.visualization.post.post_maxwell`
- **描述**: Create a field plot of stacked layer plot.

### `PostProcessorMaxwell.create_fieldplot_layers_nets`
- **参数**: `layers_nets, quantity, setup, intrinsics, plot_on_surface, plot_name`
- **模块**: `ansys.aedt.core.visualization.post.post_maxwell`
- **描述**: Create a field plot of stacked layer plot on specified matrix of layers and nets.

### `PostProcessorCommon.plots`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Plot list.

### `PostProcessorCommon.plots`
- **参数**: `value`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: No description provided.

### `PostProcessor3D.field_plot_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Fields plot names.

### `PostProcessor3D.create_fieldplot_line`
- **参数**: `assignment, quantity, setup, intrinsics, plot_name, field_type`
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Create a field plot of the line.

### `PostProcessor3D.create_fieldplot_surface`
- **参数**: `assignment, quantity, setup, intrinsics, plot_name, field_type`
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Create a field plot of surfaces.

### `PostProcessor3D.create_fieldplot_cutplane`
- **参数**: `assignment, quantity, setup, intrinsics, plot_name, filter_objects, field_type`
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Create a field plot of cut planes.

### `PostProcessor3D.create_fieldplot_volume`
- **参数**: `assignment, quantity, setup, intrinsics, plot_name, field_type`
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Create a field plot of volumes.

### `PostProcessor3D.delete_field_plot`
- **参数**: `name`
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Delete a field plot.

### `PostProcessor3D.get_model_plotter_geometries`
- **参数**: `objects, plot_as_separate_objects, plot_air_objects, force_opacity_value, array_coordinates, generate_mesh, get_objects_from_aedt`
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Initialize the Model Plotter object with actual modeler objects and return it.

### `PostProcessor3D.plot_model_obj`
- **参数**: `objects, show, export_path, plot_as_separate_objects, plot_air_objects, force_opacity_value, clean_files, array_coordinates, view, show_legend, dark_mode, show_bounding, show_grid`
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Plot the model or a substet of objects.

### `PostProcessor3D.plot_field_from_fieldplot`
- **参数**: `plot_name, project_path, mesh_plot, image_format, view, plot_label, plot_folder, show, scale_min, scale_max, plot_cad_objs, log_scale, dark_mode, show_grid, show_bounding, show_legend, plot_as_separate_objects, file_format`
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Export a field plot to an image file (JPG or PNG) using Python PyVista.

### `PostProcessor3D.plot_field`
- **参数**: `quantity, assignment, plot_type, setup, intrinsics, mesh_on_fields, view, plot_label, show, scale_min, scale_max, plot_cad_objs, log_scale, export_path, image_format, keep_plot_after_generation, dark_mode, show_bounding, show_grid, show_legend, filter_objects, plot_as_separate_objects, file_format`
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Create a field plot  using Python PyVista and export to an image file (JPG or PNG).

### `PostProcessor3D.plot_animated_field`
- **参数**: `quantity, assignment, plot_type, setup, intrinsics, variation_variable, variations, view, show, scale_min, scale_max, plot_cad_objs, log_scale, zoom, export_gif, export_path, force_opacity_value, dark_mode, show_grid, show_bounding, show_legend, filter_objects, file_format`
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Create an animated field plot using Python PyVista and export to a gif file.

### `PostProcessor3D.create_3d_plot`
- **参数**: `solution_data, nominal_sweep, nominal_value, primary_sweep, secondary_sweep, snapshot_path, show`
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Create a 3D plot using Matplotlib.

### `PostProcessor3D.plot_scene`
- **参数**: `frames, gif_path, norm_index, dy_rng, fps, show, view, zoom, convert_fields_in_db, log_multiplier`
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Plot the current model 3D scene with overlapping animation coming from a file list and save the gif.

### `SolutionData.plot`
- **参数**: `curves, formula, size, show_legend, x_label, y_label, title, snapshot_path, is_polar, show`
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: Create a matplotlib figure based on a list of data.

### `SolutionData.plot_3d`
- **参数**: `curve, primary_sweep, secondary_sweep, x_label, y_label, title, formula, size, snapshot_path, show`
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: Create a matplotlib 3D figure based on a list of data.

### `Nets3DLayout.plot`
- **参数**: `layers, show_legend, save_plot, outline, size, plot_components_on_top, plot_components_on_bottom, show`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Plot a Net to Matplotlib 2D Chart.

### `Object3d.plot`
- **参数**: `show`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Plot model with PyVista.

## 未分类 (需人工审核) (uncategorized)
### `Hfss.hybrid`
- **参数**: ``
- **模块**: `ansys.aedt.core.hfss`
- **描述**: HFSS hybrid mode for the active solution.

### `Hfss.hybrid`
- **参数**: `value`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: No description provided.

### `Hfss.composite`
- **参数**: ``
- **模块**: `ansys.aedt.core.hfss`
- **描述**: HFSS composite mode for the active solution.

### `Hfss.composite`
- **参数**: `value`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: No description provided.

### `Hfss.table_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Imported table names.

### `Hfss.set_auto_open`
- **参数**: `enable, opening_type`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Set the HFSS auto open type.

### `Hfss.assign_finite_conductivity`
- **参数**: `assignment, material, conductivity, permittivity, use_thickness, thickness, roughness, is_infinite_ground, is_two_side, is_internal, is_shell_element, use_huray, radius, ratio, height_deviation, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Assign finite conductivity to one or more objects or faces of a given material.

### `Hfss.assign_perfect_h`
- **参数**: `assignment, height_deviation, roughness, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Assign perfect magnetic boundary to one or more objects or faces.

### `Hfss.assign_layered_impedance`
- **参数**: `assignment, is_two_side, material, thickness, is_infinite_ground, is_shell_element, roughness, height_deviation, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Assign finite conductivity to one or more objects or faces of a given material.

### `Hfss.create_perfecte_from_objects`
- **参数**: `assignment, reference, start_direction, name, is_infinite_ground, is_boundary_on_plane`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a Perfect E taking the closest edges of two objects.

### `Hfss.create_perfecth_from_objects`
- **参数**: `assignment, reference, start_direction, name, is_boundary_on_plane`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a Perfect H taking the closest edges of two objects.

### `Hfss.assign_perfecte_to_sheets`
- **参数**: `assignment, name, is_infinite_ground`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a Perfect E taking one sheet.

### `Hfss.assign_perfecth_to_sheets`
- **参数**: `assignment, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Assign a Perfect H to sheets.

### `Hfss.create_impedance_between_objects`
- **参数**: `start_assignment, end_assignment, start_direction, source_name, resistance, reactance, is_infinite_ground, bound_on_plane`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create an impedance taking the closest edges of two objects.

### `Hfss.assign_hybrid_region`
- **参数**: `assignment, name, hybrid_region`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Assign a hybrid region to one or more objects.

### `Hfss.assign_febi`
- **参数**: `assignment, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Assign an FE-BI region to one or more objects.

### `Hfss.create_sbr_antenna`
- **参数**: `antenna_type, target_cs, units, parameters, use_current_source_representation, is_array, custom_array, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a parametric beam antennas in SBR+.

### `Hfss.create_sbr_file_based_antenna`
- **参数**: `far_field_data, antenna_size, antenna_impedance, representation_type, target_cs, units, is_array, custom_array, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a linked antenna.

### `Hfss.create_sbr_linked_antenna`
- **参数**: `assignment, target_cs, setup, field_type, use_composite_ports, use_global_current, current_conformance, thin_sources, power_fraction, visible, is_array, custom_array, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a linked antennas.

### `Hfss.set_sbr_txrx_settings`
- **参数**: `txrx_settings`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Set SBR+ TX RX antennas settings.

### `Hfss.create_voltage_source_from_objects`
- **参数**: `assignment, reference, start_direction, name, source_on_plane`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a voltage source taking the closest edges of two objects.

### `Hfss.create_current_source_from_objects`
- **参数**: `assignment, reference, start_direction, name, source_on_plane`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a current source taking the closest edges of two objects.

### `Hfss.assign_lattice_pair`
- **参数**: `assignment, reverse_v, phase_delay, phase_delay_param1, phase_delay_param2, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Assign a lattice pair to a couple of faces.

### `Hfss.auto_assign_lattice_pairs`
- **参数**: `assignment, coordinate_system, coordinate_plane`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Assign lattice pairs to a geometry automatically.

### `Hfss.assign_secondary`
- **参数**: `assignment, primary, u_start, u_end, reverse_v, phase_delay, phase_delay_param1, phase_delay_param2, coordinate_system, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Assign the secondary boundary condition.

### `Hfss.assign_primary`
- **参数**: `assignment, u_start, u_end, reverse_v, coordinate_system, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Assign the primary boundary condition.

### `Hfss.create_open_region`
- **参数**: `frequency, boundary, apply_infinite_ground, gp_axis`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create an open region on the active editor.

### `Hfss.create_lumped_rlc_between_objects`
- **参数**: `assignment, reference, start_direction, name, rlc_type, resistance, inductance, capacitance, is_boundary_on_plane`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a lumped RLC taking the closest edges of two objects.

### `Hfss.assign_voltage_source_to_sheet`
- **参数**: `assignment, start_direction, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a voltage source taking one sheet.

### `Hfss.assign_current_source_to_sheet`
- **参数**: `assignment, start_direction, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a current source taking one sheet.

### `Hfss.assign_lumped_rlc_to_sheet`
- **参数**: `assignment, start_direction, name, rlc_type, resistance, inductance, capacitance`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a lumped RLC taking one sheet.

### `Hfss.assign_impedance_to_sheet`
- **参数**: `assignment, name, resistance, reactance, is_infinite_ground, coordinate_system`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create an impedance taking one sheet.

### `Hfss.edit_sources`
- **参数**: `assignment, include_port_post_processing, max_available_power, use_incident_voltage, eigenmode_stored_energy`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Set up the power loaded for HFSS postprocessing in multiple sources simultaneously.

### `Hfss.edit_source_from_file`
- **参数**: `input_file, assignment, is_time_domain, x_scale, y_scale, impedance, data_format, encoding, window`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Edit a source from file data.

### `Hfss.create_scattering`
- **参数**: `plot, sweep, ports, ports_excited, variations`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create an S-parameter report.

### `Hfss.create_sbr_radar_from_json`
- **参数**: `radar_file, name, offset, speed, use_relative_cs, relative_cs_name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create an SBR+ radar setup from a JSON file.

### `Hfss.set_sbr_current_sources_options`
- **参数**: `conformance, thin_sources, power_fraction`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Set SBR+ setup options for the current source.

### `Hfss.set_differential_pair`
- **参数**: `assignment, reference, common_mode, differential_mode, common_reference, differential_reference, active, matched`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Add a differential pair definition.

### `Hfss.assign_symmetry`
- **参数**: `assignment, name, is_perfect_e`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Assign symmetry to planar entities.

### `Hfss.set_impedance_multiplier`
- **参数**: `multiplier`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Set impedance multiplier.

### `Hfss.parse_hdm_file`
- **参数**: `file_name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Parse an HFSS SBR+ or Creeping Waves ``hdm`` file.

### `Hfss.plane_wave`
- **参数**: `assignment, vector_format, origin, polarization, propagation_vector, wave_type, wave_type_properties, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a plane wave excitation.

### `Hfss.far_field_wave`
- **参数**: `assignment, setup, simulate_source, preserve_source_solution, coordinate_system, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a far field wave excitation.

### `Hfss.hertzian_dipole_wave`
- **参数**: `assignment, origin, polarization, is_electric, radius, name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Create a hertzian dipole wave excitation.

### `Hfss.set_radiated_power_calc_method`
- **参数**: `method`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Set the radiated power calculation method in Hfss.

### `Hfss.delete_table`
- **参数**: `name`
- **模块**: `ansys.aedt.core.hfss`
- **描述**: Delete data table.

### `Hfss3dLayout.ic_mode`
- **参数**: ``
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: IC mode of current design.

### `Hfss3dLayout.ic_mode`
- **参数**: `value`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: No description provided.

### `Hfss3dLayout.dissolve_component`
- **参数**: `component`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Dissolve a component and remove it from 3D Layout.

### `Hfss3dLayout.create_scattering`
- **参数**: `plot, sweep_name, port_names, port_excited, variations`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Create a scattering report.

### `Hfss3dLayout.edit_cosim_options`
- **参数**: `simulate_missing_solution, align_ports, renormalize_ports, renorm_impedance, setup_override_name, sweep_override_name, use_interpolating_sweep, use_y_matrix, interpolation_algorithm`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Edit cosimulation options.

### `Hfss3dLayout.set_differential_pair`
- **参数**: `assignment, reference, common_mode, differential_mode, common_reference, differential_reference, active, matched`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Add a differential pair definition.

### `Hfss3dLayout.load_diff_pairs_from_file`
- **参数**: `input_file`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Load differential pairs definition from a file.

### `Hfss3dLayout.enable_rigid_flex`
- **参数**: ``
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Turn on or off the rigid flex of a board with bending if available.

### `Hfss3dLayout.edit_source_from_file`
- **参数**: `source, input_file, is_time_domain, x_scale, y_scale, impedance, data_format, encoding, include_post_effects, incident_voltage, window`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Edit a source from file data.

### `Hfss3dLayout.show_extent`
- **参数**: `show`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Show or hide extent in a HFSS3dLayout design.

### `Hfss3dLayout.change_options`
- **参数**: `color_by_net`
- **模块**: `ansys.aedt.core.hfss3dlayout`
- **描述**: Change options for an existing layout.

### `CommonSetup.default_intrinsics`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Retrieve default intrinsic for actual setup.

### `CommonSetup.props`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Properties of the setup.

### `CommonSetup.props`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: No description provided.

### `CommonSetup.is_solved`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Verify if solutions are available for given setup.

### `CommonSetup.omodule`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Analysis module.

### `CommonSetup.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Name.

### `CommonSetup.name`
- **参数**: `name`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: No description provided.

### `Setup.create`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Add a new setup based on class settings in AEDT.

### `Setup.update`
- **参数**: `properties`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Update the setup based on either the class argument or a dictionary.

### `Setup.delete`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Delete actual Setup.

### `Setup.enable`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Enable a setup.

### `Setup.disable`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Disable a setup.

### `SetupCircuit.props`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: No description provided.

### `SetupCircuit.create`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Add a new setup based on class settings in AEDT.

### `SetupCircuit.update`
- **参数**: `properties`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Update the setup based on the class arguments or a dictionary.

### `SetupCircuit.enable`
- **参数**: `name`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Enable a setup.

### `SetupCircuit.disable`
- **参数**: `name`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Disable a setup.

### `Setup3DLayout.props`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: No description provided.

### `Setup3DLayout.props`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: No description provided.

### `Setup3DLayout.is_solved`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Verify if solutions are available for a given setup.

### `Setup3DLayout.solver_type`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Setup type.

### `Setup3DLayout.create`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Add a new setup based on class settings in AEDT.

### `Setup3DLayout.update`
- **参数**: `properties`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Update the setup based on the class arguments or a dictionary.

### `Setup3DLayout.enable`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Enable a setup.

### `Setup3DLayout.disable`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Disable a setup.

### `Setup3DLayout.use_matrix_convergence`
- **参数**: `entry_selection, ignore_phase_when_mag_is_less_than, all_diagonal_entries, max_delta, max_delta_phase, all_offdiagonal_entries, off_diagonal_mag, off_diagonal_phase, custom_entries`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Enable Matrix Convergence criteria.

### `SetupHFSS.add_derivatives`
- **参数**: `derivative_list`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Add derivatives to the setup.

### `SetupHFSS.set_tuning_offset`
- **参数**: `offsets`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Set derivative variable to a specific offset value.

### `SetupHFSS.use_matrix_convergence`
- **参数**: `entry_selection, ignore_phase_when_mag_is_less_than, all_diagonal_entries, max_delta, max_delta_phase, all_offdiagonal_entries, off_diagonal_mag, off_diagonal_phase, custom_entries`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Enable Matrix Convergence criteria.

### `SetupHFSSAuto.add_derivatives`
- **参数**: `derivative_list`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Add derivatives to the setup.

### `SetupHFSSAuto.set_tuning_offset`
- **参数**: `offsets`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Set derivative variable to a specific offset value.

### `SetupHFSSAuto.add_subrange`
- **参数**: `range_type, start, end, count, unit, clear`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Add a subrange to the sweep.

### `SetupSBR.add_subrange`
- **参数**: `range_type, start, end, count, unit, clear`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Add a subrange to the sweep.

### `SetupMaxwell.enable_control_program`
- **参数**: `control_program_path, control_program_args, call_after_last_step`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Enable control program option is solution setup.

### `SetupQ3D.ac_rl_enabled`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Get/Set the AC RL solution in active Q3D setup.

### `SetupQ3D.ac_rl_enabled`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: No description provided.

### `SetupQ3D.capacitance_enabled`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Get/Set the Capacitance solution in active Q3D setup.

### `SetupQ3D.capacitance_enabled`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: No description provided.

### `SetupQ3D.dc_enabled`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Get/Set the DC solution in active Q3D setup.

### `SetupQ3D.dc_enabled`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: No description provided.

### `SetupQ3D.dc_resistance_only`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Get/Set the DC Resistance Only or Resistance/Inductance calculatio in active Q3D setup.

### `SetupQ3D.dc_resistance_only`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: No description provided.

### `SetupQ3D.update`
- **参数**: `properties`
- **模块**: `ansys.aedt.core.modules.solve_setup`
- **描述**: Update the setup based on either the class argument or a dictionary.

### `BoundaryDictionary.props`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Dictionary that defines all the boundary condition properties.

### `PieceWiseLinearDictionary.dataset_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Dataset name that defines the piecewise assignment.

### `NetworkObject.create`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Create network in AEDT.

### `NetworkObject.auto_update`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Get if auto-update is enabled.

### `NetworkObject.auto_update`
- **参数**: `b`
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Set auto-update on or off.

### `NetworkObject.links`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Get links of the network.

### `NetworkObject.r_links`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Get r-links of the network.

### `NetworkObject.c_links`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Get c-links of the network.

### `NetworkObject.nodes`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Get nodes of the network.

### `NetworkObject.face_nodes`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Get face nodes of the network.

### `NetworkObject.faces_ids_in_network`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Get ID of faces included in the network.

### `NetworkObject.objects_in_network`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Get objects included in the network.

### `NetworkObject.internal_nodes`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Get internal nodes.

### `NetworkObject.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Get network name.

### `NetworkObject.name`
- **参数**: `new_network_name`
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Set new name of the network.

### `NetworkObject.add_internal_node`
- **参数**: `name, power, mass, specific_heat`
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Add an internal node to the network.

### `NetworkObject.add_face_node`
- **参数**: `assignment, name, thermal_resistance, material, thickness, resistance`
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Create a face node in the network.

### `NetworkObject.add_nodes_from_dictionaries`
- **参数**: `nodes`
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Add nodes to the network from dictionary.

### `NetworkObject.add_link`
- **参数**: `node1, node2, value, name`
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Create links in the network object.

### `NetworkObject.add_links_from_dictionaries`
- **参数**: `connections`
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Create links in the network object.

### `NetworkObject.update`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Update the network in AEDT.

### `NetworkObject.update_assignment`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Update assignments of the network.

### `_Link.props`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Get link properties.

### `_Link.delete_link`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Delete link from network.

### `_Node.delete_node`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Delete node from network.

### `_Node.node_type`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Get node type.

### `_Node.props`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Get properties of the node.

### `_Node.props`
- **参数**: `props`
- **模块**: `ansys.aedt.core.modules.boundary.icepak_boundary`
- **描述**: Set properties of the node.

### `Sources.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Source name.

### `Sources.name`
- **参数**: `source_name`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `Sources.update`
- **参数**: `original_name, new_source`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Update the source in AEDT.

### `Sources.delete`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Delete the source in AEDT.

### `Sources.create`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Create a new source in AEDT.

### `PowerSinSource.ac_magnitude`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: AC magnitude value.

### `PowerSinSource.ac_magnitude`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `PowerSinSource.ac_phase`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: AC phase value.

### `PowerSinSource.ac_phase`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `PowerSinSource.dc_magnitude`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: DC voltage value.

### `PowerSinSource.dc_magnitude`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `PowerSinSource.power_offset`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Power offset from zero watts.

### `PowerSinSource.power_offset`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `PowerSinSource.power_magnitude`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Available power of the source above power offset.

### `PowerSinSource.power_magnitude`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `PowerSinSource.delay`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Delay to start of sine wave.

### `PowerSinSource.delay`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `PowerSinSource.damping_factor`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Damping factor.

### `PowerSinSource.damping_factor`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `PowerSinSource.phase_delay`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Phase delay.

### `PowerSinSource.phase_delay`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `PowerSinSource.tone`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Frequency to use for harmonic balance.

### `PowerSinSource.tone`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `PowerIQSource.sampling_time`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Sampling time value.

### `PowerIQSource.sampling_time`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `PowerIQSource.dc_magnitude`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: DC voltage value.

### `PowerIQSource.dc_magnitude`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `PowerIQSource.repeat_from`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Repeat from time.

### `PowerIQSource.repeat_from`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `PowerIQSource.delay`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Delay to start of sine wave.

### `PowerIQSource.delay`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `PowerIQSource.carrier_amplitude_voltage`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Carrier amplitude value, voltage-based.

### `PowerIQSource.carrier_amplitude_voltage`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `PowerIQSource.carrier_amplitude_power`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Carrier amplitude value, power-based.

### `PowerIQSource.carrier_amplitude_power`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `PowerIQSource.carrier_offset`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Carrier offset.

### `PowerIQSource.carrier_offset`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `PowerIQSource.real_impedance`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Real carrier impedance.

### `PowerIQSource.real_impedance`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `PowerIQSource.imaginary_impedance`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Imaginary carrier impedance.

### `PowerIQSource.imaginary_impedance`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `PowerIQSource.damping_factor`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Damping factor.

### `PowerIQSource.damping_factor`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `PowerIQSource.phase_delay`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Phase delay.

### `PowerIQSource.phase_delay`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `PowerIQSource.tone`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Frequency to use for harmonic balance.

### `PowerIQSource.tone`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `PowerIQSource.i_q_values`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: I and Q value at each timepoint.

### `PowerIQSource.i_q_values`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `PowerIQSource.file`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: File path with I and Q values.

### `PowerIQSource.file`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `VoltageFrequencyDependentSource.frequencies`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: List of frequencies in ``Hz``.

### `VoltageFrequencyDependentSource.frequencies`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `VoltageFrequencyDependentSource.vmag`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: List of magnitudes in ``V``.

### `VoltageFrequencyDependentSource.vmag`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `VoltageFrequencyDependentSource.vang`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: List of angles in ``rad``.

### `VoltageFrequencyDependentSource.vang`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `VoltageFrequencyDependentSource.vreal`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: List of real values in ``V``.

### `VoltageFrequencyDependentSource.vreal`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `VoltageFrequencyDependentSource.vimag`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: List of imaginary values in ``V``.

### `VoltageFrequencyDependentSource.vimag`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `VoltageFrequencyDependentSource.magnitude_angle`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Enable magnitude and angle data.

### `VoltageFrequencyDependentSource.magnitude_angle`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `VoltageFrequencyDependentSource.fds_filename`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: FDS file path.

### `VoltageFrequencyDependentSource.fds_filename`
- **参数**: `name`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `VoltageDCSource.ac_magnitude`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: AC magnitude value.

### `VoltageDCSource.ac_magnitude`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `VoltageDCSource.ac_phase`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: AC phase value.

### `VoltageDCSource.ac_phase`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `VoltageDCSource.dc_magnitude`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: DC voltage value.

### `VoltageDCSource.dc_magnitude`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `VoltageSinSource.ac_magnitude`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: AC magnitude value.

### `VoltageSinSource.ac_magnitude`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `VoltageSinSource.ac_phase`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: AC phase value.

### `VoltageSinSource.ac_phase`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `VoltageSinSource.dc_magnitude`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: DC voltage value.

### `VoltageSinSource.dc_magnitude`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `VoltageSinSource.voltage_amplitude`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Voltage amplitude.

### `VoltageSinSource.voltage_amplitude`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `VoltageSinSource.voltage_offset`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Voltage offset from zero watts.

### `VoltageSinSource.voltage_offset`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `VoltageSinSource.delay`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Delay to start of sine wave.

### `VoltageSinSource.delay`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `VoltageSinSource.damping_factor`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Damping factor.

### `VoltageSinSource.damping_factor`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `VoltageSinSource.phase_delay`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Phase delay.

### `VoltageSinSource.phase_delay`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `VoltageSinSource.tone`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Frequency to use for harmonic balance.

### `VoltageSinSource.tone`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `CurrentSinSource.ac_magnitude`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: AC magnitude value.

### `CurrentSinSource.ac_magnitude`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `CurrentSinSource.ac_phase`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: AC phase value.

### `CurrentSinSource.ac_phase`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `CurrentSinSource.dc_magnitude`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: DC current value.

### `CurrentSinSource.dc_magnitude`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `CurrentSinSource.current_amplitude`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Current amplitude.

### `CurrentSinSource.current_amplitude`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `CurrentSinSource.current_offset`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Current offset.

### `CurrentSinSource.current_offset`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `CurrentSinSource.delay`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Delay to start of sine wave.

### `CurrentSinSource.delay`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `CurrentSinSource.damping_factor`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Damping factor.

### `CurrentSinSource.damping_factor`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `CurrentSinSource.phase_delay`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Phase delay.

### `CurrentSinSource.phase_delay`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `CurrentSinSource.multiplier`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Multiplier for simulating multiple parallel current sources.

### `CurrentSinSource.multiplier`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `CurrentSinSource.tone`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: Frequency to use for harmonic balance.

### `CurrentSinSource.tone`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.circuit_boundary`
- **描述**: No description provided.

### `NativeComponentObject.props`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: No description provided.

### `NativeComponentObject.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Boundary Name.

### `NativeComponentObject.name`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: No description provided.

### `NativeComponentObject.definition_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Definition name of the native component.

### `NativeComponentObject.create`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Create a Native Component in AEDT.

### `NativeComponentObject.update`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Update the Native Component in AEDT.

### `NativeComponentObject.delete`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Delete the Native Component in AEDT.

### `BoundaryObject3dLayout.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Boundary Name.

### `BoundaryObject3dLayout.name`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: No description provided.

### `BoundaryObject3dLayout.props`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Excitation data.

### `BoundaryObject3dLayout.update`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Update the boundary.

### `NativeComponentPCB.power`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Power dissipation assigned to the PCB.

### `NativeComponentPCB.power`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Assign power dissipation to the PCB.

### `NativeComponentPCB.force_source_solve`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Force source solution option.

### `NativeComponentPCB.force_source_solve`
- **参数**: `val`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Set Whether to force source solution.

### `NativeComponentPCB.included_parts`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Parts options.

### `NativeComponentPCB.included_parts`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Set PCB parts incusion option.

### `NativeComponentPCB.power`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Assign power dissipation to the PCB.

### `NativeComponentPCB.force_source_solve`
- **参数**: `val`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Set Whether to force source solution.

### `NativeComponentPCB.included_parts`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Set PCB parts incusion option.

### `NativeComponentPCB.identify_extent_poly`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Get polygon that defines board extent.

### `NativeComponentPCB.set_board_extents`
- **参数**: `extent_type, extent_polygon`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Set board extent.

### `PCBSettingsPackageParts.set_solderballs_modeling`
- **参数**: `modeling`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Set how to model solderballs.

### `PCBSettingsPackageParts.set_connectors_modeling`
- **参数**: `modeling, solderbumps_modeling, bondwire_material, bondwire_diameter`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Set how to model connectors.

### `PCBSettingsDeviceParts.simplify_parts`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Get whether parts are simplified as cuboid.

### `PCBSettingsDeviceParts.simplify_parts`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Set whether parts are simplified as cuboid.

### `PCBSettingsDeviceParts.footprint_filter`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Minimum component footprint for filtering.

### `PCBSettingsDeviceParts.footprint_filter`
- **参数**: `minimum_footprint`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Set minimum component footprint for filtering.

### `PCBSettingsDeviceParts.power_filter`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Minimum component power for filtering.

### `PCBSettingsDeviceParts.power_filter`
- **参数**: `minimum_power`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Set minimum component power for filtering.

### `PCBSettingsDeviceParts.type_filters`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Types of component that are filtered.

### `PCBSettingsDeviceParts.type_filters`
- **参数**: `object_type`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Set types of component to filter.

### `PCBSettingsDeviceParts.height_filter`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Minimum component height for filtering.

### `PCBSettingsDeviceParts.height_filter`
- **参数**: `minimum_height`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Set minimum component height for filtering and whether to filter 2D objects.

### `PCBSettingsDeviceParts.objects_2d_filter`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Whether 2d objects are filtered.

### `PCBSettingsDeviceParts.objects_2d_filter`
- **参数**: `enable`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Set whether 2d objects are filtered.

### `PCBSettingsDeviceParts.filters`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: All active filters.

### `PCBSettingsDeviceParts.overridden_components`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: All overridden components.

### `PCBSettingsDeviceParts.override_definition`
- **参数**: `package, part, filter_component, power, r_jb, r_jc, height`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Set component override.

### `PCBSettingsDeviceParts.override_instance`
- **参数**: `reference_designator, filter_component, power, r_jb, r_jc, height`
- **模块**: `ansys.aedt.core.modules.boundary.layout_boundary`
- **描述**: Set instance override.

### `FieldSetup.props`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: Field Properties.

### `FieldSetup.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: Boundary Name.

### `FieldSetup.name`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: No description provided.

### `FieldSetup.create`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: Create a Field Setup Component in HFSS.

### `FieldSetup.update`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: Update the Field Setup in AEDT.

### `FieldSetup.delete`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: Delete the Field Setup in AEDT.

### `FarFieldSetup.definition`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: Set/Get the Far Field Angle Definition.

### `FarFieldSetup.definition`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: No description provided.

### `FarFieldSetup.use_local_coordinate_system`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: Set/Get the usage of a custom Coordinate System.

### `FarFieldSetup.use_local_coordinate_system`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: No description provided.

### `FarFieldSetup.local_coordinate_system`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: Set/Get the custom Coordinate System name.

### `FarFieldSetup.local_coordinate_system`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: No description provided.

### `FarFieldSetup.polarization`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: Set/Get the Far Field Polarization.

### `FarFieldSetup.polarization`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: No description provided.

### `FarFieldSetup.slant_angle`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: Set/Get the Far Field Slant Angle if Polarization is Set to `Slant`.

### `FarFieldSetup.slant_angle`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: No description provided.

### `FarFieldSetup.theta_start`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: Set/Get the Far Field Theta Start Angle if Definition is Set to `Theta-Phi`.

### `FarFieldSetup.theta_stop`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: Set/Get the Far Field Theta Stop Angle if Definition is Set to `Theta-Phi`.

### `FarFieldSetup.theta_step`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: Set/Get the Far Field Theta Step Angle if Definition is Set to `Theta-Phi`.

### `FarFieldSetup.phi_start`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: Set/Get the Far Field Phi Start Angle if Definition is Set to `Theta-Phi`.

### `FarFieldSetup.phi_stop`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: Set/Get the Far Field Phi Stop Angle if Definition is Set to `Theta-Phi`.

### `FarFieldSetup.phi_step`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: Set/Get the Far Field Phi Step Angle if Definition is Set to `Theta-Phi`.

### `FarFieldSetup.azimuth_start`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: Set/Get the Far Field Azimuth Start Angle if Definition is Set to `Az Over El` or `El Over Az`.

### `FarFieldSetup.azimuth_stop`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: Set/Get the Far Field Azimuth Stop Angle if Definition is Set to `Az Over El` or `El Over Az`.

### `FarFieldSetup.azimuth_step`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: Set/Get the Far Field Azimuth Step Angle if Definition is Set to `Az Over El` or `El Over Az`.

### `FarFieldSetup.elevation_start`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: Set/Get the Far Field Elevation Start Angle if Definition is Set to `Az Over El` or `El Over Az`.

### `FarFieldSetup.elevation_stop`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: Set/Get the Far Field Elevation Stop Angle if Definition is Set to `Az Over El` or `El Over Az`.

### `FarFieldSetup.elevation_step`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: Set/Get the Far Field Elevation Step Angle if Definition is Set to `Az Over El` or `El Over Az`.

### `FarFieldSetup.theta_start`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: No description provided.

### `FarFieldSetup.theta_stop`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: No description provided.

### `FarFieldSetup.theta_step`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: No description provided.

### `FarFieldSetup.phi_start`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: No description provided.

### `FarFieldSetup.phi_stop`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: No description provided.

### `FarFieldSetup.phi_step`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: No description provided.

### `FarFieldSetup.azimuth_start`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: No description provided.

### `FarFieldSetup.azimuth_stop`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: No description provided.

### `FarFieldSetup.azimuth_step`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: No description provided.

### `FarFieldSetup.elevation_start`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: No description provided.

### `FarFieldSetup.elevation_stop`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: No description provided.

### `FarFieldSetup.elevation_step`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.hfss_boundary`
- **描述**: No description provided.

### `Matrix.sources`
- **参数**: `is_gc_sources`
- **模块**: `ansys.aedt.core.modules.boundary.q3d_boundary`
- **描述**: List of matrix sources.

### `Matrix.operations`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.q3d_boundary`
- **描述**: List of matrix operations.

### `Matrix.create`
- **参数**: `source_names, new_net_name, new_source_name, new_sink_name`
- **模块**: `ansys.aedt.core.modules.boundary.q3d_boundary`
- **描述**: Create a new matrix.

### `Matrix.delete`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.q3d_boundary`
- **描述**: Delete current matrix.

### `Matrix.add_operation`
- **参数**: `operation_type, source_names, new_net_name, new_source_name, new_sink_name`
- **模块**: `ansys.aedt.core.modules.boundary.q3d_boundary`
- **描述**: Add a new operation to existing matrix.

### `MaxwellParameters.props`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.maxwell_boundary`
- **描述**: Maxwell parameter data.

### `MaxwellParameters.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.maxwell_boundary`
- **描述**: Boundary Name.

### `MaxwellParameters.name`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.maxwell_boundary`
- **描述**: No description provided.

### `MaxwellParameters.create`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.maxwell_boundary`
- **描述**: Create a boundary.

### `MaxwellParameters.update`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.maxwell_boundary`
- **描述**: Update the boundary.

### `MaxwellMatrix.signal_sources`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.maxwell_boundary`
- **描述**: No description provided.

### `MaxwellMatrix.ground_sources`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.maxwell_boundary`
- **描述**: No description provided.

### `MaxwellMatrix.group_sources`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.maxwell_boundary`
- **描述**: No description provided.

### `MaxwellMatrix.rl_sources`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.maxwell_boundary`
- **描述**: No description provided.

### `MaxwellMatrix.gc_sources`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.maxwell_boundary`
- **描述**: No description provided.

### `MaxwellMatrix.reduced_matrices`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.maxwell_boundary`
- **描述**: List of reduced matrix groups for the parent matrix.

### `MaxwellMatrix.join_series`
- **参数**: `sources, matrix_name, join_name`
- **模块**: `ansys.aedt.core.modules.boundary.maxwell_boundary`
- **描述**: Create matrix reduction by joining sources in series.

### `MaxwellMatrix.join_parallel`
- **参数**: `sources, matrix_name, join_name`
- **模块**: `ansys.aedt.core.modules.boundary.maxwell_boundary`
- **描述**: Create matrix reduction by joining sources in parallel.

### `MaxwellReducedMatrix.update`
- **参数**: `name, operation_type, new_name, new_sources`
- **模块**: `ansys.aedt.core.modules.boundary.maxwell_boundary`
- **描述**: Update the reduced matrix.

### `MaxwellReducedMatrix.delete`
- **参数**: `name`
- **模块**: `ansys.aedt.core.modules.boundary.maxwell_boundary`
- **描述**: Delete a specific reduction operation.

### `BoundaryCommon.delete`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.common`
- **描述**: Delete the boundary.

### `BoundaryObject.props`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.common`
- **描述**: Boundary data.

### `BoundaryObject.type`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.common`
- **描述**: Boundary type.

### `BoundaryObject.type`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.common`
- **描述**: No description provided.

### `BoundaryObject.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.common`
- **描述**: Boundary Name.

### `BoundaryObject.name`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modules.boundary.common`
- **描述**: No description provided.

### `BoundaryObject.create`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.common`
- **描述**: Create a boundary.

### `BoundaryObject.update`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.common`
- **描述**: Update the boundary.

### `BoundaryObject.update_assignment`
- **参数**: ``
- **模块**: `ansys.aedt.core.modules.boundary.common`
- **描述**: Update the boundary assignment.

### `Monitor.face_monitors`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.monitor_icepak`
- **描述**: Get point monitor objects.

### `Monitor.point_monitors`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.monitor_icepak`
- **描述**: Get face monitor objects.

### `Monitor.all_monitors`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.monitor_icepak`
- **描述**: Get all monitor objects.

### `Monitor.assign_point_monitor`
- **参数**: `point_position, monitor_quantity, monitor_name`
- **模块**: `ansys.aedt.core.visualization.post.monitor_icepak`
- **描述**: Create and assign a point monitor.

### `Monitor.assign_point_monitor_to_vertex`
- **参数**: `vertex_id, monitor_quantity, monitor_name`
- **模块**: `ansys.aedt.core.visualization.post.monitor_icepak`
- **描述**: Create and assign a point monitor to a vertex.

### `Monitor.assign_surface_monitor`
- **参数**: `surface_name, monitor_quantity, monitor_name`
- **模块**: `ansys.aedt.core.visualization.post.monitor_icepak`
- **描述**: Assign a surface monitor.

### `Monitor.assign_face_monitor`
- **参数**: `face_id, monitor_quantity, monitor_name`
- **模块**: `ansys.aedt.core.visualization.post.monitor_icepak`
- **描述**: Assign a face monitor.

### `Monitor.assign_point_monitor_in_object`
- **参数**: `name, monitor_quantity, monitor_name`
- **模块**: `ansys.aedt.core.visualization.post.monitor_icepak`
- **描述**: Assign a point monitor in the centroid of a specific object.

### `Monitor.delete_monitor`
- **参数**: `monitor_name`
- **模块**: `ansys.aedt.core.visualization.post.monitor_icepak`
- **描述**: Delete monitor object.

### `ObjectMonitor.geometry_assignment`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.monitor_icepak`
- **描述**: Get the geometry assignment for the monitor object.

### `ObjectMonitor.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.monitor_icepak`
- **描述**: Get the name of the monitor object.

### `ObjectMonitor.id`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.monitor_icepak`
- **描述**: Get the name, or id of geometry assignment.

### `ObjectMonitor.properties`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.monitor_icepak`
- **描述**: Get a dictionary of properties.

### `ObjectMonitor.delete`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.monitor_icepak`
- **描述**: Delete a monitor object.

### `ObjectMonitor.quantities`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.monitor_icepak`
- **描述**: Get the quantities being monitored.

### `ObjectMonitor.type`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.monitor_icepak`
- **描述**: Get the monitor type.

### `ObjectMonitor.value`
- **参数**: `quantity, setup, design_variation_dict, si_out`
- **模块**: `ansys.aedt.core.visualization.post.monitor_icepak`
- **描述**: Get a list of values obtained from the monitor object.

### `PointMonitor.location`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.monitor_icepak`
- **描述**: Get the monitor point location.

### `FaceMonitor.location`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.monitor_icepak`
- **描述**: Get the monitor location in terms of face or surface center.

### `AdvancedReport.from_spisim_cfg`
- **参数**: `cls, file_path`
- **模块**: `ansys.aedt.core.visualization.post.spisim`
- **描述**: Load SPIsim configuration file.

### `AdvancedReport.dump_spisim_cfg`
- **参数**: `file_path`
- **模块**: `ansys.aedt.core.visualization.post.spisim`
- **描述**: Create a SPIsim configuration file.

### `SpiSim.working_directory`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.spisim`
- **描述**: Working directory.

### `SpiSim.working_directory`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.spisim`
- **描述**: No description provided.

### `SpiSim.compute_erl`
- **参数**: `config_file, port_order, specify_through_ports, bandwidth, tdr_duration, z_terminations, transition_time, fixture_delay, input_amplitude, ber, pdf_bin_size, signal_loss_factor, permitted_reflection, reflections_length, modulation_type`
- **模块**: `ansys.aedt.core.visualization.post.spisim`
- **描述**: Compute effective return loss (ERL) using Ansys SPISIM from S-parameter file.

### `SpiSim.compute_com`
- **参数**: `standard, config_file, port_order, fext_s4p, next_s4p, out_folder`
- **模块**: `ansys.aedt.core.visualization.post.spisim`
- **描述**: Compute Channel Operating Margin. Only COM ver3.4 is supported.

### `SpiSim.compute_ucie`
- **参数**: `tx_ports, rx_ports, victim_ports, tx_resistance, tx_capacitance, rx_resistance, rx_capacitance, packaging_type, data_rate, report_directory`
- **模块**: `ansys.aedt.core.visualization.post.spisim`
- **描述**: Universal Chiplet Interface Express (UCIe) Compliance support.

### `DataSet.wave`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.spisim`
- **描述**: Retrieves the trace data.

### `SpiSimRawRead.read_float64`
- **参数**: `f`
- **模块**: `ansys.aedt.core.visualization.post.spisim`
- **描述**: No description provided.

### `SpiSimRawRead.read_float32`
- **参数**: `f`
- **模块**: `ansys.aedt.core.visualization.post.spisim`
- **描述**: No description provided.

### `SpiSimRawRead.trace_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.spisim`
- **描述**: Returns a list of exiting trace names of the RAW file.

### `Ucie.to_var_list`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.spisim`
- **描述**: No description provided.

### `FieldsCalculator.write`
- **参数**: `expression, output_file, setup, intrinsics`
- **模块**: `ansys.aedt.core.visualization.post.fields_calculator`
- **描述**: Save the content of the stack register for future reuse in a later Field Calculator session.

### `FieldsCalculator.evaluate`
- **参数**: `expression, setup, intrinsics`
- **模块**: `ansys.aedt.core.visualization.post.fields_calculator`
- **描述**: Evaluate an expression and return the value.

### `BaseFolderPlot.to_dict`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Convert the settings to a dictionary.

### `BaseFolderPlot.from_dict`
- **参数**: `dictionary`
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Initialize the settings from a dictionary.

### `ColorMapSettings.map_type`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Get the color map type for the field plot.

### `ColorMapSettings.map_type`
- **参数**: `value`
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Set the type of color mapping for the field plot.

### `ColorMapSettings.color`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Get the color based on the map type.

### `ColorMapSettings.color`
- **参数**: `v`
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Set the colormap based on the map type.

### `ColorMapSettings.to_dict`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Convert the color map settings to a dictionary.

### `ColorMapSettings.from_dict`
- **参数**: `settings`
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Initialize the number format settings of the colormap settings from a dictionary.

### `AutoScale.to_dict`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Convert the auto-scale settings to a dictionary.

### `AutoScale.from_dict`
- **参数**: `dictionary`
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Initialize the auto-scale settings from a dictionary.

### `MinMaxScale.to_dict`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Convert the min-max scale settings to a dictionary.

### `MinMaxScale.from_dict`
- **参数**: `dictionary`
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Initialize the min-max scale settings from a dictionary.

### `SpecifiedScale.to_dict`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Convert the specified scale settings to a dictionary.

### `SpecifiedScale.from_dict`
- **参数**: `dictionary`
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Initialize the specified scale settings from a dictionary.

### `NumberFormat.format_type`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Get the current number format type.

### `NumberFormat.format_type`
- **参数**: `v`
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Set the numeric format type of the scale.

### `NumberFormat.to_dict`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Convert the number format settings to a dictionary.

### `NumberFormat.from_dict`
- **参数**: `dictionary`
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Initialize the number format settings of the field plot settings from a dictionary.

### `Scale3DSettings.unit`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Get unit used in the plot.

### `Scale3DSettings.unit`
- **参数**: `v`
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Set unit used in the plot.

### `Scale3DSettings.scale_type`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Get type of scale used for the field plot.

### `Scale3DSettings.scale_type`
- **参数**: `value`
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Set the scale type used for the field plot.

### `Scale3DSettings.scale_settings`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Get the current scale settings based on the scale type.

### `Scale3DSettings.scale_settings`
- **参数**: `value`
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Set the current scale settings based on the scale type.

### `Scale3DSettings.to_dict`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Convert the scale settings to a dictionary.

### `Scale3DSettings.from_dict`
- **参数**: `dictionary`
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Initialize the scale settings of the field plot settings from a dictionary.

### `MarkerSettings.marker_type`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Get the type of maker to use.

### `MarkerSettings.marker_type`
- **参数**: `v`
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Set the type of maker to use.

### `MarkerSettings.to_dict`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Convert the marker settings to a dictionary.

### `MarkerSettings.from_dict`
- **参数**: `dictionary`
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Initialize the marker settings of the field plot settings from a dictionary.

### `ArrowSettings.arrow_type`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Get the type of arrows used in the field plot.

### `ArrowSettings.arrow_type`
- **参数**: `v`
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Set the type of arrows for the field plot.

### `ArrowSettings.to_dict`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Convert the arrow settings to a dictionary.

### `ArrowSettings.from_dict`
- **参数**: `dictionary`
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Initialize the arrow settings of the field plot settings from a dictionary.

### `FolderPlotSettings.update`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Update folder plot settings.

### `FolderPlotSettings.to_dict`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Convert the field plot settings to a dictionary.

### `FolderPlotSettings.from_dict`
- **参数**: `dictionary`
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Initialize the field plot settings from a dictionary.

### `FieldPlot.folder_settings`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Get the folder settings.

### `FieldPlot.folder_settings`
- **参数**: `v`
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Set the fieldplot folder settings.

### `FieldPlot.filter_boxes`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Volumes on which filter the plot.

### `FieldPlot.filter_boxes`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: No description provided.

### `FieldPlot.intrinsicVar`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Intrinsic variable.

### `FieldPlot.create`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Create a field plot.

### `FieldPlot.update`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Update the field plot.

### `FieldPlot.delete`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.field_data`
- **描述**: Delete the field plot.

### `FfdSolutionDataExporter.model_info`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.farfield_exporter`
- **描述**: List of models.

### `FfdSolutionDataExporter.metadata_file`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.farfield_exporter`
- **描述**: Metadata file.

### `FieldSummary.add_calculation`
- **参数**: `entity, geometry, geometry_name, quantity, normal, side, mesh, ref_temperature, time`
- **模块**: `ansys.aedt.core.visualization.post.field_summary`
- **描述**: Add an entry in the field summary calculation requests.

### `PostProcessor3DLayout.compute_power_by_layer`
- **参数**: `layers, solution`
- **模块**: `ansys.aedt.core.visualization.post.post_3dlayout`
- **描述**: Compute the power by layer.

### `PostProcessor3DLayout.compute_power_by_net`
- **参数**: `nets, solution`
- **模块**: `ansys.aedt.core.visualization.post.post_3dlayout`
- **描述**: Compute the power by nets. This applies only to SIwave DC Analysis.

### `PostProcessorHFSS.create_creeping_plane_visual_ray_tracing`
- **参数**: `max_frequency, ray_density, sample_density, ray_cutoff, irregular_surface_tolerance, incident_theta, incident_phi, is_vertical_polarization`
- **模块**: `ansys.aedt.core.visualization.post.post_hfss`
- **描述**: Create a Creeping Wave Plane Wave Visual Ray Tracing and return the class object.

### `PostProcessorHFSS.create_creeping_point_visual_ray_tracing`
- **参数**: `max_frequency, ray_density, sample_density, ray_cutoff, irregular_surface_tolerance, custom_location`
- **模块**: `ansys.aedt.core.visualization.post.post_hfss`
- **描述**: Create a Creeping Wave Point Source Visual Ray Tracing and return the class object.

### `PostProcessorHFSS.create_sbr_plane_visual_ray_tracing`
- **参数**: `max_frequency, ray_density, number_of_bounces, multi_bounce, mbrd_max_sub_division, shoot_utd, incident_theta, incident_phi, is_vertical_polarization, shoot_filter_type, ray_index_start, ray_index_stop, ray_index_step, ray_box`
- **模块**: `ansys.aedt.core.visualization.post.post_hfss`
- **描述**: Create an SBR Plane Wave Visual Ray Tracing and return the class object.

### `PostProcessorHFSS.create_sbr_point_visual_ray_tracing`
- **参数**: `max_frequency, ray_density, number_of_bounces, multi_bounce, mbrd_max_sub_division, shoot_utd, custom_location, shoot_filter_type, ray_index_start, ray_index_stop, ray_index_step, ray_box`
- **模块**: `ansys.aedt.core.visualization.post.post_hfss`
- **描述**: Create an SBR Point Source Visual Ray Tracing and return the class object.

### `PostProcessorHFSS.set_tuning_offset`
- **参数**: `setup, offsets`
- **模块**: `ansys.aedt.core.visualization.post.post_hfss`
- **描述**: Set derivative variable to a specific offset value.

### `PostProcessorCircuit.sample_waveform`
- **参数**: `waveform_data, waveform_sweep, waveform_unit, waveform_sweep_unit, unit_interval, clock_tics, pandas_enabled`
- **模块**: `ansys.aedt.core.visualization.post.post_circuit`
- **描述**: Sampling a waveform at clock times plus half unit interval.

### `PostProcessorCircuit.sample_ami_waveform`
- **参数**: `setup, probe, source, variation_list_w_value, unit_interval, ignore_bits, plot_type, clock_tics`
- **模块**: `ansys.aedt.core.visualization.post.post_circuit`
- **描述**: Sampling a waveform at clock times plus half unit interval.

### `MonostaticRCSExporter.model_info`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.rcs_exporter`
- **描述**: List of models.

### `MonostaticRCSExporter.metadata_file`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.rcs_exporter`
- **描述**: Metadata file.

### `MonostaticRCSExporter.column_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.rcs_exporter`
- **描述**: Column name.

### `MonostaticRCSExporter.column_name`
- **参数**: `value`
- **模块**: `ansys.aedt.core.visualization.post.rcs_exporter`
- **描述**: Column name.

### `VRTFieldPlot.intrinsicVar`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.vrt_data`
- **描述**: Intrinsic variable.

### `VRTFieldPlot.create`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.vrt_data`
- **描述**: Create a field plot.

### `VRTFieldPlot.update`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.vrt_data`
- **描述**: Update the field plot.

### `VRTFieldPlot.delete`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.vrt_data`
- **描述**: Delete the field plot.

### `CommonTemplate.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Report name.

### `CommonTemplate.config_file`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Configuration file.

### `CommonTemplate.config_file`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: No description provided.

### `CommonTemplate.traces`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Trace list.

### `CommonTemplate.traces`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: No description provided.

### `CommonTemplate.pass_fail`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Flag indicating if pass/fail criteria is applied.

### `CommonTemplate.pass_fail`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: No description provided.

### `CommonTemplate.pass_fail_criteria`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Pass/fail criteria.

### `CommonTemplate.pass_fail_criteria`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: No description provided.

### `ParametersTemplate.trace_pins`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Trace pin coupling list.

### `ParametersTemplate.trace_pins`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: No description provided.

### `VirtualComplianceChaptersData.add_content`
- **参数**: `content, content_type`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Add content to the chapter.

### `VirtualComplianceChaptersData.add_section`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Add a section to the chapter.

### `VirtualComplianceChaptersData.add_subchapter`
- **参数**: `text`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Add a subchapter to the chapter.

### `VirtualComplianceChaptersData.add_text`
- **参数**: `text`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Add text to the chapter.

### `VirtualComplianceChaptersData.add_image`
- **参数**: `image_data`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Add image to the chapter.

### `VirtualComplianceChaptersData.add_table`
- **参数**: `table_data`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Add table to the chapter.

### `VirtualComplianceData.chapters`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Chapters list.

### `VirtualComplianceData.chapters`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: No description provided.

### `VirtualComplianceData.add_chapter`
- **参数**: `chapter, position`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Add a new chapter to the compliance data.

### `VirtualCompliance.image_width`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Image width resolution during export.

### `VirtualCompliance.image_width`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: No description provided.

### `VirtualCompliance.image_height`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Image height resolution during export.

### `VirtualCompliance.image_height`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: No description provided.

### `VirtualCompliance.dut_image`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: DUT image.

### `VirtualCompliance.dut_image`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: No description provided.

### `VirtualCompliance.template_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Template name.

### `VirtualCompliance.template_name`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: No description provided.

### `VirtualCompliance.points_in_polygon`
- **参数**: `points, polygon`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: No description provided.

### `VirtualCompliance.create_pdf`
- **参数**: `file_name, close_project`
- **模块**: `ansys.aedt.core.visualization.post.compliance`
- **描述**: Create the PDF report after the method ``compute_report_data`` is called.

### `PostProcessorMaxwell.evaluate_inception_voltage`
- **参数**: `plot_name, field_line_number`
- **模块**: `ansys.aedt.core.visualization.post.post_maxwell`
- **描述**: Perform Inception voltage evaluation on selected field line traces.

### `PostProcessorCommon.available_display_types`
- **参数**: `report_category`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Retrieve display types for a report categories.

### `PostProcessorCommon.available_quantities_categories`
- **参数**: `report_category, display_type, solution, context, is_siwave_dc`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Compute the list of all available report categories.

### `PostProcessorCommon.logger`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Logger.

### `PostProcessorCommon.oeditor`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: No description provided.

### `PostProcessorCommon.steal_focus_oneditor`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Remove the selection of an object that would prevent the image from exporting correctly.

### `Reports.standard`
- **参数**: `expressions, setup`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Create a standard or default report object.

### `Reports.monitor`
- **参数**: `expressions, setup`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Create an Icepak Monitor Report object.

### `Reports.fields`
- **参数**: `expressions, setup, polyline`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Create a Field Report object.

### `Reports.cg_fields`
- **参数**: `expressions, setup, polyline`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Create a CG Field Report object in Q3D and Q2D.

### `Reports.dc_fields`
- **参数**: `expressions, setup, polyline`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Create a DC Field Report object in Q3D.

### `Reports.rl_fields`
- **参数**: `expressions, setup, polyline`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Create an AC RL Field Report object in Q3D and Q2D.

### `Reports.far_field`
- **参数**: `expressions, setup, sphere_name, source_context`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Create a Far Field Report object.

### `Reports.near_field`
- **参数**: `expressions, setup`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Create a Field Report object.

### `Reports.eigenmode`
- **参数**: `expressions, setup`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Create a Standard or Default Report object.

### `Reports.statistical_eye_contour`
- **参数**: `expressions, setup, quantity_type`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Create a standard statistical AMI contour plot.

### `Reports.eye_diagram`
- **参数**: `expressions, setup, quantity_type, statistical_analysis, unit_interval`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Create a Standard or Default Report object.

### `Reports.emi_receiver`
- **参数**: `expressions, setup_name`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Create an EMI receiver report.

### `Reports.circuit_netlist`
- **参数**: `setup, expressions, domain`
- **模块**: `ansys.aedt.core.visualization.post.common`
- **描述**: Create a Circuit Netlist Report object.

### `PostProcessorIcepak.create_field_summary`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.post_icepak`
- **描述**: Create field summary object.

### `PostProcessorIcepak.evaluate_faces_quantity`
- **参数**: `faces, quantity, side, setup_name, variations, ref_temperature, time`
- **模块**: `ansys.aedt.core.visualization.post.post_icepak`
- **描述**: Export the field surface output.

### `PostProcessorIcepak.evaluate_monitor_quantity`
- **参数**: `monitor, quantity, side, setup_name, variations, ref_temperature, time`
- **模块**: `ansys.aedt.core.visualization.post.post_icepak`
- **描述**: Export monitor field output.

### `PostProcessorIcepak.evaluate_object_quantity`
- **参数**: `object_name, quantity_name, side, volume, setup_name, variations, ref_temperature, time`
- **模块**: `ansys.aedt.core.visualization.post.post_icepak`
- **描述**: Export the field output on or in an object.

### `PostProcessor3D.model_units`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Model units.

### `PostProcessor3D.change_field_property`
- **参数**: `plot_name, property_name, property_value`
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Modify a field plot property.

### `PostProcessor3D.nb_display`
- **参数**: `show_axis, show_grid, show_ruler`
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Show the Jupyter Notebook display.

### `PostProcessor3D.animate_fields_from_aedtplt`
- **参数**: `plot_name, plot_folder, variation_variable, variations, project_path, export_gif, show, dark_mode, show_bounding, show_grid`
- **模块**: `ansys.aedt.core.visualization.post.post_common_3d`
- **描述**: Generate a field plot to an image file (JPG or PNG) using PyVista.

### `SolutionData.active_variation`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: No description provided.

### `SolutionData.active_variation`
- **参数**: `value`
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: No description provided.

### `SolutionData.enable_pandas_output`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: Set/Get a flag to use Pandas to export dict and lists.

### `SolutionData.enable_pandas_output`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: No description provided.

### `SolutionData.set_active_variation`
- **参数**: `var_id`
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: Set the active variations to one of available variations in self.variations.

### `SolutionData.variation_values`
- **参数**: `variation`
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: Get the list of the specific variation available values.

### `SolutionData.intrinsics`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: Get intrinsics dictionary on active variation.

### `SolutionData.intrinsics_by_variation`
- **参数**: `variation`
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: Get intrinsics dictionary on active variation.

### `SolutionData.nominal_variation`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: Nominal variation.

### `SolutionData.nominal_variation`
- **参数**: `val`
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: No description provided.

### `SolutionData.full_matrix_real_imag`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: Get the full available solution data in Real and Imaginary parts.

### `SolutionData.full_matrix_mag_phase`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: Get the full available solution data magnitude and phase in radians.

### `SolutionData.to_degrees`
- **参数**: `input_list`
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: Convert an input list from radians to degrees.

### `SolutionData.to_radians`
- **参数**: `input_list`
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: Convert an input list from degrees to radians.

### `SolutionData.lookup_column_value`
- **参数**: `array, match_columns, match_values, output_column`
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: Filters rows in a NumPy array based on column-value matches,

### `SolutionData.data_real`
- **参数**: `expression, convert_to_SI`
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: Retrieve the real part of the data for an expression.

### `SolutionData.is_real_only`
- **参数**: `expression`
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: Check if the expression has only real values or not.

### `SolutionData.ifft`
- **参数**: `curve_header, u_axis, v_axis, window`
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: Create IFFT of given complex data.

### `SolutionData.ifft_to_file`
- **参数**: `u_axis, v_axis, coord_system_center, db_val, num_frames, csv_path, csv_file_header`
- **模块**: `ansys.aedt.core.visualization.post.solution_data`
- **描述**: Save IFFT matrix to a list of CSV files (one per time step).

### `COMParameters.standard`
- **参数**: ``
- **模块**: `ansys.aedt.core.visualization.post.spisim_com_configuration_files.com_parameters`
- **描述**: Standard name.

### `COMParameters.standard`
- **参数**: `value`
- **模块**: `ansys.aedt.core.visualization.post.spisim_com_configuration_files.com_parameters`
- **描述**: No description provided.

### `COMParameters.load`
- **参数**: `file_path`
- **模块**: `ansys.aedt.core.visualization.post.spisim_com_configuration_files.com_parameters`
- **描述**: Load COM parameters from a JSON file.

### `COMParameters.load_spisim_cfg`
- **参数**: `file_path`
- **模块**: `ansys.aedt.core.visualization.post.spisim_com_configuration_files.com_parameters`
- **描述**: Load a SPIsim configuration file.

### `PostLayoutDesignExtension.pedb`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.post_layout_design`
- **描述**: No description provided.

### `PostLayoutDesignExtension.add_extension_content`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.post_layout_design`
- **描述**: Add custom content to the extension UI.

### `ViaDesignExtension.add_extension_content`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.via_design`
- **描述**: Add custom content to the extension UI.

### `PushExcitation3DLayoutExtension.add_extension_content`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.push_excitation_from_file_3dl`
- **描述**: Add content to the extension UI.

### `PushExcitation3DLayoutExtension.browse_files`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.push_excitation_from_file_3dl`
- **描述**: Open file dialog to browse for excitation files.

### `ArbitraryWavePortExtension.add_extension_content`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.generate_arbitrary_wave_ports`
- **描述**: Add custom content to the extension UI.

### `ViaClusteringExtension.add_extension_content`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.via_clustering`
- **描述**: Add custom content to the extension UI.

### `ParametrizeEdbExtension.add_extension_content`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.parametrize_edb`
- **描述**: Add extension content to the UI.

### `ParametrizeEdbExtension.show_error_message`
- **参数**: `message`
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.parametrize_edb`
- **描述**: Show error message.

### `ParametrizeEdbExtension.generate_callback`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.parametrize_edb`
- **描述**: Generate callback function.

### `CutoutExtension.add_extension_content`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.cutout`
- **描述**: Add custom content to the extension UI.

### `CutoutExtension.objects_net`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.cutout`
- **描述**: Get objects by net from the EDB modeler.

### `CutoutExtension.execute_cutout`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.cutout`
- **描述**: Get whether the cutout should be executed.

### `ExportLayoutExtension.add_extension_content`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.export_layout`
- **描述**: Add custom content to the extension UI.

### `ExportTo3DExtension.add_extension_content`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.export_to_3d`
- **描述**: Add custom content to the extension UI.

### `ConfigureLayoutExtension.selected_edb`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.resources.configure_layout.master_ui`
- **描述**: No description provided.

### `ConfigureLayoutExtension.selected_edb`
- **参数**: `value`
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.resources.configure_layout.master_ui`
- **描述**: No description provided.

### `ConfigureLayoutExtension.add_toggle_theme_button`
- **参数**: `parent, toggle_row, toggle_column`
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.resources.configure_layout.master_ui`
- **描述**: No description provided.

### `ConfigureLayoutExtension.add_toggle_theme_button_`
- **参数**: `parent`
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.resources.configure_layout.master_ui`
- **描述**: Create a button to toggle between light and dark themes.

### `ConfigureLayoutExtension.add_extension_content`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.resources.configure_layout.master_ui`
- **描述**: No description provided.

### `ConfigureLayoutExtension.apply_config_to_edb`
- **参数**: `config_path, test_folder`
- **模块**: `ansys.aedt.core.extensions.hfss3dlayout.resources.configure_layout.master_ui`
- **描述**: No description provided.

### `ChokeDesignerExtension.validate_configuration`
- **参数**: `choke`
- **模块**: `ansys.aedt.core.extensions.hfss.choke_designer`
- **描述**: Validate choke configuration parameters.

### `ChokeDesignerExtension.load_configuration`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss.choke_designer`
- **描述**: Load choke configuration from JSON file.

### `ChokeDesignerExtension.update_config`
- **参数**: `category, selected_option`
- **模块**: `ansys.aedt.core.extensions.hfss.choke_designer`
- **描述**: Update boolean configuration options.

### `ChokeDesignerExtension.update_radio_buttons`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss.choke_designer`
- **描述**: Update radio button selections based on current choke configuration.

### `ChokeDesignerExtension.update_entries`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss.choke_designer`
- **描述**: Update entry widgets based on current choke configuration.

### `ChokeDesignerExtension.callback`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss.choke_designer`
- **描述**: Callback function for Export to HFSS button.

### `ChokeDesignerExtension.create_boolean_options`
- **参数**: `parent`
- **模块**: `ansys.aedt.core.extensions.hfss.choke_designer`
- **描述**: Create boolean option radio buttons.

### `ChokeDesignerExtension.add_extension_content`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss.choke_designer`
- **描述**: Add custom content to the extension UI.

### `PushExcitationExtension.add_extension_content`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss.push_excitation_from_file`
- **描述**: Add content to the extension UI.

### `PushExcitationExtension.browse_files`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss.push_excitation_from_file`
- **描述**: Open file dialog to browse for excitation files.

### `ShieldingEffectivenessExtension.add_extension_content`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss.shielding_effectiveness`
- **描述**: Add custom content to the extension UI.

### `MoveItExtension.add_extension_content`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss.move_it`
- **描述**: Add custom content to the extension UI.

### `MCADAssemblyFrontend.add_toggle_theme_button`
- **参数**: `parent, toggle_row, toggle_column`
- **模块**: `ansys.aedt.core.extensions.hfss.mcad_assembly`
- **描述**: Create a button to toggle between light and dark themes.

### `MCADAssemblyFrontend.add_extension_content`
- **参数**: ``
- **模块**: `ansys.aedt.core.extensions.hfss.mcad_assembly`
- **描述**: No description provided.

### `MCADAssemblyFrontend.run`
- **参数**: `config_data`
- **模块**: `ansys.aedt.core.extensions.hfss.mcad_assembly`
- **描述**: No description provided.

### `Component.load`
- **参数**: `cls, name, data`
- **模块**: `ansys.aedt.core.extensions.hfss.mcad_assembly`
- **描述**: No description provided.

### `Component.assemble_sub_components`
- **参数**: `hfss, cs_prefix`
- **模块**: `ansys.aedt.core.extensions.hfss.mcad_assembly`
- **描述**: No description provided.

### `Component.apply_arrange`
- **参数**: `hfss`
- **模块**: `ansys.aedt.core.extensions.hfss.mcad_assembly`
- **描述**: No description provided.

### `Component.assemble`
- **参数**: `hfss, cs_prefix`
- **模块**: `ansys.aedt.core.extensions.hfss.mcad_assembly`
- **描述**: Parameters

### `MCADAssemblyBackend.load`
- **参数**: `cls, data, cur_dir`
- **模块**: `ansys.aedt.core.extensions.hfss.mcad_assembly`
- **描述**: No description provided.

### `MCADAssemblyBackend.run`
- **参数**: `hfss`
- **模块**: `ansys.aedt.core.extensions.hfss.mcad_assembly`
- **描述**: No description provided.

### `GraphSetup.minimum_time`
- **参数**: ``
- **模块**: `ansys.aedt.core.filtersolutions_core.graph_setup`
- **描述**: Minimum time value for exporting time response. The default is ``0 s``.

### `GraphSetup.minimum_time`
- **参数**: `min_time_string`
- **模块**: `ansys.aedt.core.filtersolutions_core.graph_setup`
- **描述**: No description provided.

### `GraphSetup.maximum_time`
- **参数**: ``
- **模块**: `ansys.aedt.core.filtersolutions_core.graph_setup`
- **描述**: Maximum time value for exporting time response. The default is ``10 ns``.

### `GraphSetup.maximum_time`
- **参数**: `max_time_string`
- **模块**: `ansys.aedt.core.filtersolutions_core.graph_setup`
- **描述**: No description provided.

### `ModelerCircuit.o_def_manager`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.schematic`
- **描述**: AEDT Definition manager.

### `ModelerCircuit.schematic_units`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.schematic`
- **描述**: Schematic units.

### `ModelerCircuit.schematic_units`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.schematic`
- **描述**: No description provided.

### `ModelerCircuit.ocomponent_manager`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.schematic`
- **描述**: Component manager object.

### `ModelerCircuit.omodel_manager`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.schematic`
- **描述**: Model manager object.

### `ModelerCircuit.oeditor`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.schematic`
- **描述**: Oeditor Module.

### `ModelerCircuit.zoom_to_fit`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.schematic`
- **描述**: Zoom To Fit.

### `ModelerCircuit.connect_schematic_components`
- **参数**: `starting_component, ending_component, pin_starting, pin_ending, use_wire`
- **模块**: `ansys.aedt.core.modeler.schematic`
- **描述**: Connect schematic components.

### `ModelerCircuit.create_text`
- **参数**: `text, x_origin, y_origin, text_size, text_angle, text_color, show_rect, x1, y1, x2, y2, rect_line_width, rect_border_color, rect_fill, rect_color`
- **模块**: `ansys.aedt.core.modeler.schematic`
- **描述**: Draw Text.

### `ModelerCircuit.change_text_property`
- **参数**: `assignment, name, value`
- **模块**: `ansys.aedt.core.modeler.schematic`
- **描述**: Change an oeditor property.

### `ModelerNexxim.layouteditor`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.schematic`
- **描述**: Return the Circuit Layout Editor.

### `ModelerNexxim.schematic`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.schematic`
- **描述**: Schematic Component.

### `ModelerNexxim.pages`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.schematic`
- **描述**: Return the number of pages of the current schematic.

### `ModelerNexxim.page_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.schematic`
- **描述**: Page names in the schematic.

### `ModelerNexxim.add_page`
- **参数**: `name`
- **模块**: `ansys.aedt.core.modeler.schematic`
- **描述**: Add a page to the schematic.

### `ModelerNexxim.rename_page`
- **参数**: `page, name`
- **模块**: `ansys.aedt.core.modeler.schematic`
- **描述**: Rename a page in the schematic.

### `ModelerNexxim.edb`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.schematic`
- **描述**: EDB.

### `ModelerNexxim.model_units`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.schematic`
- **描述**: Layout model units.

### `ModelerNexxim.layout`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.schematic`
- **描述**: Primitives.

### `ModelerNexxim.model_units`
- **参数**: `units`
- **模块**: `ansys.aedt.core.modeler.schematic`
- **描述**: Set the model units as a string e.g. "mm".

### `ModelerTwinBuilder.components`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.schematic`
- **描述**: .. deprecated:: 0.4.13

### `ModelerTwinBuilder.schematic`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.schematic`
- **描述**: Schematic Object.

### `ModelerMaxwellCircuit.schematic`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.schematic`
- **描述**: Schematic Object.

### `Modeler3DLayout.o_def_manager`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: AEDT Definition manager.

### `Modeler3DLayout.stackup`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Get the Stackup class and its methods.

### `Modeler3DLayout.oeditor`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Oeditor Module.

### `Modeler3DLayout.ocomponent_manager`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Component manager object.

### `Modeler3DLayout.omodel_manager`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Model manager object.

### `Modeler3DLayout.edb`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: EBD. Supported only in IronPython.

### `Modeler3DLayout.logger`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Logger.

### `Modeler3DLayout.fit_all`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Fit all.

### `Modeler3DLayout.model_units`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Model units as a string (for example, "mm").

### `Modeler3DLayout.model_units`
- **参数**: `units`
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: No description provided.

### `Modeler3DLayout.obounding_box`
- **参数**: `assignment`
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Bounding box of a specified object.

### `Modeler3DLayout.change_property`
- **参数**: `assignment, name, value, aedt_tab`
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Change an oeditor property.

### `Modeler3DLayout.change_clip_plane_position`
- **参数**: `name, location`
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Change the clip plane position.

### `Modeler3DLayout.colinear_heal`
- **参数**: `assignment, tolerance`
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Remove small edges of one or more primitives.

### `Modeler3DLayout.expand`
- **参数**: `assignment, size, expand_type, replace_original`
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Expand the object by a specific size.

### `Modeler3DLayout.convert_to_selections`
- **参数**: `assignment, return_list`
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Convert one or more object to selections.

### `Modeler3DLayout.intersect`
- **参数**: `assignment`
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Intersect objects from names.

### `Modeler3DLayout.duplicate`
- **参数**: `assignment, count, vector`
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Duplicate one or more elements along a vector.

### `Modeler3DLayout.duplicate_across_layers`
- **参数**: `assignment, layers`
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Duplicate one or more elements along a vector.

### `Modeler3DLayout.set_temperature_dependence`
- **参数**: `include_temperature_dependence, enable_feedback, ambient_temp, create_project_var`
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Set the temperature dependence for the design.

### `Modeler3DLayout.set_spice_model`
- **参数**: `assignment, input_file, model_name, subcircuit_name, pin_map`
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Assign a Spice model to a component.

### `Modeler3DLayout.set_touchstone_model`
- **参数**: `assignment, input_file, model_name`
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Assign a Touchstone model to a component.

### `Modeler3DLayout.clip_plane`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Create a clip plane in the layout.

### `Modeler3DLayout.clip_planes`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: All available clip planes. To be considered a clip plane, the name must follow this

### `Modeler3DLayout.geometry_check_and_fix_all`
- **参数**: `min_area`
- **模块**: `ansys.aedt.core.modeler.modeler_pcb`
- **描述**: Run Geometry Check.

### `GeometryOperators.List2list`
- **参数**: `input_list`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Convert a C# list object to a Python list.

### `GeometryOperators.parse_dim_arg`
- **参数**: `string, scale_to_unit, variable_manager`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Convert a number and unit to a float.

### `GeometryOperators.cs_plane_to_axis_str`
- **参数**: `val`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Retrieve a string for a coordinate system plane.

### `GeometryOperators.cs_plane_to_plane_str`
- **参数**: `val`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Retrieve a string for a coordinate system plane.

### `GeometryOperators.cs_axis_str`
- **参数**: `val`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Retrieve a string for a coordinate system axis.

### `GeometryOperators.draft_type_str`
- **参数**: `val`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Retrieve the draft type.

### `GeometryOperators.v_cross`
- **参数**: `a, b`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Evaluate the cross product of two geometry vectors.

### `GeometryOperators.v_dot`
- **参数**: `a, b`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Evaluate the dot product between two geometry vectors.

### `GeometryOperators.v_prod`
- **参数**: `s, v`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Evaluate the product between a scalar value and a vector.

### `GeometryOperators.v_sub`
- **参数**: `a, b`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Evaluate two geometry vectors by subtracting them (a-b).

### `GeometryOperators.v_sum`
- **参数**: `a, b`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Evaluate two geometry vectors by adding them (a+b).

### `GeometryOperators.v_norm`
- **参数**: `a`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Evaluate the Euclidean norm of a geometry vector.

### `GeometryOperators.normalize_vector`
- **参数**: `v`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Normalize a geometry vector.

### `GeometryOperators.v_points`
- **参数**: `p1, p2`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Vector from one point to another point.

### `GeometryOperators.points_distance`
- **参数**: `p1, p2`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Evaluate the distance between two points expressed as their Cartesian coordinates.

### `GeometryOperators.find_point_on_plane`
- **参数**: `pointlists, direction`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Find a point on a plane.

### `GeometryOperators.distance_vector`
- **参数**: `p, a, b`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Evaluate the vector distance between point ``p`` and a line defined by two points, ``a`` and ``b``.

### `GeometryOperators.is_between_points`
- **参数**: `p, a, b, tol`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Check if a point lies on the segment defined by two points.

### `GeometryOperators.is_parallel`
- **参数**: `a1, a2, b1, b2, tol`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Check if a segment defined by two points is parallel to a segment defined by two other points.

### `GeometryOperators.parallel_coeff`
- **参数**: `a1, a2, b1, b2`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: ADD DESCRIPTION.

### `GeometryOperators.is_collinear`
- **参数**: `a, b, tol`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Check if two vectors are collinear (parallel or anti-parallel).

### `GeometryOperators.v_angle`
- **参数**: `a, b`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Evaluate the angle between two geometry vectors.

### `GeometryOperators.deg2rad`
- **参数**: `angle`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Convert the angle from degrees to radians.

### `GeometryOperators.rad2deg`
- **参数**: `angle`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Convert the angle from radians to degrees.

### `GeometryOperators.is_orthonormal_triplet`
- **参数**: `x, y, z, tol`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Check if three vectors are orthonormal.

### `GeometryOperators.is_unit_vector`
- **参数**: `v, tol`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Check if a vector is a unit vector.

### `GeometryOperators.is_orthogonal_matrix`
- **参数**: `matrix, tol`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Check if a given 3x3 matrix is orthogonal.

### `GeometryOperators.is_small`
- **参数**: `s`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Return ``True`` if the number represented by s is zero (i.e very small).

### `GeometryOperators.is_vector_equal`
- **参数**: `v1, v2, tolerance`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Return ``True`` if two vectors are equal.

### `GeometryOperators.numeric_cs`
- **参数**: `cs_in`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Return a list of [x,y,z] numeric values given a coordinate system as input.

### `GeometryOperators.orient_polygon`
- **参数**: `x, y, clockwise`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Orient a polygon clockwise or counterclockwise.

### `GeometryOperators.v_angle_sign`
- **参数**: `va, vb, vn, right_handed`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Evaluate the signed angle between two geometry vectors.

### `GeometryOperators.v_angle_sign_2D`
- **参数**: `va, vb, right_handed`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Evaluate the signed angle between two 2D geometry vectors.

### `GeometryOperators.point_in_polygon`
- **参数**: `point, polygon, tolerance`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Determine if a point is inside, outside the polygon or at exactly at the border.

### `GeometryOperators.is_point_in_polygon`
- **参数**: `point, polygon`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Determine if a point is inside or outside a polygon, both located on the same plane.

### `GeometryOperators.are_segments_intersecting`
- **参数**: `a1, a2, b1, b2, include_collinear`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Determine if the two segments a and b are intersecting.

### `GeometryOperators.is_segment_intersecting_polygon`
- **参数**: `a, b, polygon`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Determine if a segment defined by two points ``a`` and ``b`` intersects a polygon.

### `GeometryOperators.is_perpendicular`
- **参数**: `a, b, tol`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Check if two vectors are perpendicular.

### `GeometryOperators.point_segment_distance`
- **参数**: `p, a, b`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Calculate the distance between a point ``p`` and a segment defined by two points ``a`` and ``b``.

### `GeometryOperators.find_largest_rectangle_inside_polygon`
- **参数**: `polygon, partition_max_order`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Find the largest area rectangles of arbitrary orientation in a polygon.

### `GeometryOperators.degrees_over_rounded`
- **参数**: `angle, digits`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Ceil of angle.

### `GeometryOperators.radians_over_rounded`
- **参数**: `angle, digits`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Radian angle ceiling.

### `GeometryOperators.degrees_default_rounded`
- **参数**: `angle, digits`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Convert angle to degree with given digits rounding.

### `GeometryOperators.radians_default_rounded`
- **参数**: `angle, digits`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Convert to radians with given round.

### `GeometryOperators.mirror_point`
- **参数**: `start, reference, vector`
- **模块**: `ansys.aedt.core.modeler.geometry_operators`
- **描述**: Mirror point about a plane defining by a point on the plane and a normal point.

### `Modeler3D.create_3dcomponent`
- **参数**: `input_file, name, variables_to_include, assignment, boundaries, excitations, coordinate_systems, reference_coordinate_system, is_encrypted, allow_edit, security_message, password, edit_password, password_type, hide_contents, replace_names, component_outline, export_auxiliary, monitor_objects, datasets, native_components, create_folder`
- **模块**: `ansys.aedt.core.modeler.modeler_3d`
- **描述**: Create a 3D component file.

### `Modeler3D.replace_3dcomponent`
- **参数**: `name, variables_to_include, assignment, boundaries, excitations, coordinate_systems, reference_coordinate_system`
- **模块**: `ansys.aedt.core.modeler.modeler_3d`
- **描述**: Replace with 3D component.

### `Modeler3D.create_coaxial`
- **参数**: `origin, axis, inner_radius, outer_radius, diel_radius, length, mat_inner, mat_outer, mat_diel`
- **模块**: `ansys.aedt.core.modeler.modeler_3d`
- **描述**: Create a coaxial.

### `Modeler3D.create_waveguide`
- **参数**: `origin, wg_direction_axis, wgmodel, wg_length, wg_thickness, wg_material, parametrize_w, parametrize_h, create_sheets_on_openings, name`
- **模块**: `ansys.aedt.core.modeler.modeler_3d`
- **描述**: Create a standard waveguide and optionally parametrize `W` and `H`.

### `Modeler3D.create_conical_rings`
- **参数**: `axis, origin, bottom_radius, top_radius, cone_height, ring_height, thickness, name`
- **模块**: `ansys.aedt.core.modeler.modeler_3d`
- **描述**: Create rings in a conical shape.

### `Modeler3D.objects_in_bounding_box`
- **参数**: `bounding_box, check_solids, check_lines, check_sheets`
- **模块**: `ansys.aedt.core.modeler.modeler_3d`
- **描述**: Given a bounding box checks if objects, sheets and lines are inside it.

### `Modeler3D.objects_segmentation`
- **参数**: `assignment, segmentation_thickness, segments, apply_mesh_sheets, mesh_sheets`
- **模块**: `ansys.aedt.core.modeler.modeler_3d`
- **描述**: Get segmentation of an object given the segmentation thickness or number of segments.

### `Modeler3D.change_region_padding`
- **参数**: `padding_data, padding_type, direction, region_name`
- **模块**: `ansys.aedt.core.modeler.modeler_3d`
- **描述**: Change region padding settings.

### `Modeler3D.change_region_coordinate_system`
- **参数**: `assignment, name`
- **模块**: `ansys.aedt.core.modeler.modeler_3d`
- **描述**: Change region coordinate system.

### `TransmissionLine.microstrip_synthesis`
- **参数**: `substrate_height, permittivity, impedance, electrical_length`
- **模块**: `ansys.aedt.core.modeler.calculators`
- **描述**: Strip line calculator.

### `TransmissionLine.microstrip_analysis`
- **参数**: `substrate_height, permittivity, width, thickness`
- **模块**: `ansys.aedt.core.modeler.calculators`
- **描述**: Strip line calculator.

### `TransmissionLine.differential_microstrip_analysis`
- **参数**: `substrate_height, permittivity, width, separation, thickness`
- **模块**: `ansys.aedt.core.modeler.calculators`
- **描述**: Strip line calculator.

### `TransmissionLine.stripline_synthesis`
- **参数**: `substrate_height, permittivity, impedance`
- **模块**: `ansys.aedt.core.modeler.calculators`
- **描述**: Strip line calculator.

### `TransmissionLine.suspended_strip_synthesis`
- **参数**: `substrate_height, permittivity, w1, units`
- **模块**: `ansys.aedt.core.modeler.calculators`
- **描述**: Suspended stripline calculator.

### `StandardWaveguide.waveguide_list`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.calculators`
- **描述**: Waveguide lists.

### `StandardWaveguide.find_waveguide`
- **参数**: `freq, units`
- **模块**: `ansys.aedt.core.modeler.calculators`
- **描述**: Find the closest standard waveguide for the operational frequency.

### `ModelerRMxprt.oeditor`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.modeler_2d`
- **描述**: The oEditor Module.

### `Modeler2D.calculate_radius_2D`
- **参数**: `assignment, inner`
- **模块**: `ansys.aedt.core.modeler.modeler_2d`
- **描述**: Calculate the extremity of an object in the radial direction.

### `Modeler2D.radial_split_2D`
- **参数**: `radius, name`
- **模块**: `ansys.aedt.core.modeler.modeler_2d`
- **描述**: Split the stator and rotor for mesh refinement.

### `Modeler2D.objects_in_bounding_box`
- **参数**: `bounding_box, check_lines, check_sheets`
- **模块**: `ansys.aedt.core.modeler.modeler_2d`
- **描述**: Given a 2D bounding box, check if sheets and lines are inside it.

### `Primitives3DLayout.opadstack_manager`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: AEDT padstack manager.

### `Primitives3DLayout.components`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Components.

### `Primitives3DLayout.coordinate_systems`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Coordinate systems.

### `Primitives3DLayout.coordinate_system_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Coordinate system names.

### `Primitives3DLayout.geometries`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: All Geometries including voids.

### `Primitives3DLayout.voids`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: All voids.

### `Primitives3DLayout.objects_by_layer`
- **参数**: `layer, object_filter, include_voids`
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Retrieve the list of objects that belongs to a specific layer.

### `Primitives3DLayout.objects_by_net`
- **参数**: `net, object_filter, include_voids`
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Retrieve the list of objects that belongs to a specific net.

### `Primitives3DLayout.polygon_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Get the list of all polygons in layout.

### `Primitives3DLayout.polygon_voids_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Get the list of all void polygons in layout.

### `Primitives3DLayout.line_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Get the list of all lines in layout.

### `Primitives3DLayout.line_voids_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Get the list of all void lines in layout.

### `Primitives3DLayout.rectangle_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Get the list of all rectangles in layout.

### `Primitives3DLayout.rectangle_void_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Get the list of all void rectangles in layout.

### `Primitives3DLayout.circle_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Get the list of all circles in layout.

### `Primitives3DLayout.circle_voids_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Get the list of all void circles in layout.

### `Primitives3DLayout.via_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Get the list of all vias in layout.

### `Primitives3DLayout.cleanup_objects`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Clean up all 3D Layout geometries.

### `Primitives3DLayout.polygons`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Polygons.

### `Primitives3DLayout.lines`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Lines.

### `Primitives3DLayout.circles`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Circles.

### `Primitives3DLayout.rectangles`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Rectangles.

### `Primitives3DLayout.polygons_voids`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Void Polygons.

### `Primitives3DLayout.lines_voids`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Void Lines.

### `Primitives3DLayout.circles_voids`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Void Circles.

### `Primitives3DLayout.rectangles_voids`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Void Rectangles.

### `Primitives3DLayout.components_3d`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Components.

### `Primitives3DLayout.pins`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Pins.

### `Primitives3DLayout.vias`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Vias.

### `Primitives3DLayout.nets`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Nets.

### `Primitives3DLayout.power_nets`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Nets.

### `Primitives3DLayout.signal_nets`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Nets.

### `Primitives3DLayout.no_nets`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Nets without class type.

### `Primitives3DLayout.logger`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Logger.

### `Primitives3DLayout.version`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: AEDT version.

### `Primitives3DLayout.modeler`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Modeler.

### `Primitives3DLayout.model_units`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Model units.

### `Primitives3DLayout.Padstack`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Padstack.

### `Primitives3DLayout.new_padstack`
- **参数**: `name`
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Create a `Padstack` object that can be used to create a padstack.

### `Primitives3DLayout.padstacks`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Read all definitions from HFSS 3D Layout.

### `Primitives3DLayout.change_net_visibility`
- **参数**: `assignment, visible`
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Change the visibility of one or more nets.

### `Primitives3DLayout.create_via`
- **参数**: `padstack, x, y, rotation, hole_diam, top_layer, bot_layer, name, net`
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Create a via based on an existing padstack.

### `Primitives3DLayout.create_circle`
- **参数**: `layer, x, y, radius, name, net`
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Create a circle on a layer.

### `Primitives3DLayout.create_polygon`
- **参数**: `layer, point_list, units, name, net`
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Create a polygon on a specified layer.

### `Primitives3DLayout.create_polygon_void`
- **参数**: `layer, points, assignment, units, name`
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Create a polygon void on a specified layer.

### `Primitives3DLayout.create_line`
- **参数**: `layer, center_line_coordinates, lw, start_style, end_style, name, net`
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Create a line based on a list of points.

### `Primitives3DLayout.place_3d_component`
- **参数**: `component_path, number_of_terminals, placement_layer, component_name, pos_x, pos_y, create_ports, is_3d_placement, pos_z`
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Place an HFSS 3D component in HFSS 3D Layout.

### `Primitives3DLayout.create_component_on_pins`
- **参数**: `pins, definition_name, component_type, ref_des`
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Create a component based on a pin list.

### `Primitives3DLayout.create_text`
- **参数**: `text, position, layer, angle, font_size`
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Create a text primitive object.

### `Primitives3DLayout.create_coordinate_system`
- **参数**: `origin, name`
- **模块**: `ansys.aedt.core.modeler.pcb.primitives_3d_layout`
- **描述**: Create a coordinate system.

### `Object3DLayout.object_units`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Object units.

### `Object3DLayout.change_property`
- **参数**: `value, names`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Modify a property.

### `Object3DLayout.set_property_value`
- **参数**: `name, value`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Set a property value.

### `Object3DLayout.angle`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Get/Set the circle radius.

### `Object3DLayout.angle`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `Object3DLayout.absolute_angle`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Get the absolute angle location for 2 pins components.

### `Object3DLayout.net_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Get/Set the net name.

### `Object3DLayout.net_name`
- **参数**: `netname`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `Object3DLayout.placement_layer`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Get/Set the placement layer of the object.

### `Object3DLayout.placement_layer`
- **参数**: `layer_name`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `Object3DLayout.bounding_box`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Get component bounding box.

### `Object3DLayout.create_clearance_on_component`
- **参数**: `extra_soldermask_clearance`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Create a Clearance on Soldermask layer by drawing a rectangle.

### `Object3DLayout.location`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Retrieve/Set the absolute location in model units.

### `Object3DLayout.location`
- **参数**: `position`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `Object3DLayout.lock_position`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Get/Set the lock position.

### `Object3DLayout.lock_position`
- **参数**: `lock_position`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `ModelInfoRlc.rlc_model_type`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `ModelInfoRlc.res`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `ModelInfoRlc.cap`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `ModelInfoRlc.ind`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `ModelInfoRlc.is_parallel`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `Components3DLayout.part`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Retrieve the component part.

### `Components3DLayout.part_type`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Retrieve the component part type.

### `Components3DLayout.enabled`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Enable or Disable the RLC Component.

### `Components3DLayout.enabled`
- **参数**: `status`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `Components3DLayout.die_properties`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Get die properties from component.

### `Components3DLayout.solderball_enabled`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Check if solderball is enabled.

### `Components3DLayout.die_enabled`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Check if the die is enabled. This method is valid for integrated circuits only.

### `Components3DLayout.die_type`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Die type.

### `Components3DLayout.set_die_type`
- **参数**: `die_type, orientation, height, reference_offset, auto_reference, reference_x, reference_y`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Set the die type.

### `Components3DLayout.set_solderball`
- **参数**: `solderball_type, diameter, mid_diameter, height, material, reference_offset`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Set solderball on the active component.

### `Components3DLayout.pins`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Component pins.

### `Components3DLayout.model`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: RLC model if available.

### `Nets3DLayout.components`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Components that belongs to the Nets.

### `Nets3DLayout.geometry_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: List of geometry names.

### `Pins3DLayout.start_layer`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Retrieve the starting layer of the pin.

### `Pins3DLayout.stop_layer`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Retrieve the starting layer of the pin.

### `Pins3DLayout.holediam`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Retrieve the hole diameter of the pin.

### `Geometries3DLayout.obounding_box`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Bounding box of a specified object.

### `Geometries3DLayout.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Name of Primitive.

### `Geometries3DLayout.name`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `Geometries3DLayout.points`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Provide the polygon points. For Lines it returns the center line.

### `Geometries3DLayout.edges`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Edges list.

### `Geometries3DLayout.edge_by_point`
- **参数**: `point`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Return the index of the closest edge to the specified point.

### `Geometries3DLayout.bottom_edge_x`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Compute the lower edge in the layout on x direction.

### `Geometries3DLayout.top_edge_x`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Compute the upper edge in the layout on x direction.

### `Geometries3DLayout.bottom_edge_y`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Compute the lower edge in the layout on y direction.

### `Geometries3DLayout.top_edge_y`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Compute the upper edge in the layout on y direction.

### `Geometries3DLayout.negative`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Get/Set the negative.

### `Geometries3DLayout.negative`
- **参数**: `negative`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `Geometries3DLayout.net_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Get/Set the net name.

### `Geometries3DLayout.net_name`
- **参数**: `netname`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `Polygons3DLayout.polygon_voids`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: All Polygon Voids.

### `Circle3dLayout.center`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Get/Set the circle center.

### `Circle3dLayout.center`
- **参数**: `position`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `Circle3dLayout.radius`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Get/Set the circle radius.

### `Circle3dLayout.radius`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `Rect3dLayout.corner_radius`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Get/Set the circle radius.

### `Rect3dLayout.corner_radius`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `Rect3dLayout.two_point_description`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Get/Set the circle radius.

### `Rect3dLayout.two_point_description`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `Rect3dLayout.center`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Get/Set the rectangle center.

### `Rect3dLayout.center`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `Rect3dLayout.width`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Get/Set the circle radius.

### `Rect3dLayout.width`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `Rect3dLayout.height`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Get/Set the circle radius.

### `Rect3dLayout.height`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `Rect3dLayout.point_a`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Get/Set the Point A value if 2Point Description is enabled.

### `Rect3dLayout.point_a`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `Rect3dLayout.point_b`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Get/Set the Point A value if 2Point Description is enabled.

### `Rect3dLayout.point_b`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `Line3dLayout.bend_type`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Get/Set the line bend type.

### `Line3dLayout.bend_type`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `Line3dLayout.start_cap_type`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Get/Set the line start type.

### `Line3dLayout.start_cap_type`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `Line3dLayout.end_cap_type`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Get/Set the line end type.

### `Line3dLayout.end_cap_type`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `Line3dLayout.width`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Get/Set the line width.

### `Line3dLayout.width`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `Line3dLayout.length`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Get the line length.

### `Line3dLayout.center_line`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Get the center line points and arc height.

### `Line3dLayout.center_line`
- **参数**: `points`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `Line3dLayout.add`
- **参数**: `point, position`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Add a new point to the center line.

### `Points3dLayout.is_arc`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Either if the Point is an arc or not.

### `Points3dLayout.position`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Points x and y coordinate.

### `ComponentsSubCircuit3DLayout.component_info`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Retrieve all component info.

### `ComponentsSubCircuit3DLayout.component_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Retrieve the component name.

### `ComponentsSubCircuit3DLayout.angle`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Retrieve/Set the component angle.

### `ComponentsSubCircuit3DLayout.angle`
- **参数**: `angle_val`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `ComponentsSubCircuit3DLayout.is_3d_placement`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Retrieve if the component has 3d placement.

### `ComponentsSubCircuit3DLayout.is_3d_placement`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `ComponentsSubCircuit3DLayout.is_flipped`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Retrieve if the component is flipped or not.

### `ComponentsSubCircuit3DLayout.is_flipped`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `ComponentsSubCircuit3DLayout.rotation_axis`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Rotation axis around which the component is rotated.

### `ComponentsSubCircuit3DLayout.rotation_axis`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `ComponentsSubCircuit3DLayout.rotation_axis_direction`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Axis direction of the rotation.

### `ComponentsSubCircuit3DLayout.rotation_axis_direction`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `ComponentsSubCircuit3DLayout.local_origin`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Retrieve if the component has 3d placement, the local origin.

### `ComponentsSubCircuit3DLayout.local_origin`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `ComponentsSubCircuit3DLayout.location`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Retrieve/Set the absolute location in model units.

### `ComponentsSubCircuit3DLayout.location`
- **参数**: `position`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `Padstack.pads_args`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Pad properties.

### `Padstack.add_layer`
- **参数**: `layer, pad_hole, antipad_hole, thermal_hole, connx, conny, conndir, layer_id`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Create a layer in the padstack.

### `Padstack.add_hole`
- **参数**: `hole_type, sizes, x, y, rotation`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Add a hole.

### `Padstack.create`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Create a padstack in AEDT.

### `Padstack.update`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Update the padstack in AEDT.

### `CoordinateSystems3DLayout.valid_properties`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Valid properties.

### `CoordinateSystems3DLayout.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Name of the coordinate system as a string value.

### `CoordinateSystems3DLayout.name`
- **参数**: `obj_name`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `CoordinateSystems3DLayout.origin`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Location of the coordinate system.

### `CoordinateSystems3DLayout.origin`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `CoordinateSystems3DLayout.create`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Create coordinate systems in HFSS 3D Layout.

### `CoordinateSystems3DLayout.change_property`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Modify a property.

### `CoordinateSystems3DLayout.delete`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Delete the coordinate system.

### `PDSLayer.pad`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Pad.

### `PDSLayer.antipad`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Antipad.

### `PDSLayer.pad`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `PDSLayer.antipad`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `PDSLayer.thermal`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: Thermal.

### `PDSLayer.thermal`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.pcb.object_3d_layout`
- **描述**: No description provided.

### `BuildingsPrep.create_building_roof`
- **参数**: `all_pos`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.osm`
- **描述**: Generate a filled in polygon from outline.

### `BuildingsPrep.generate_buildings`
- **参数**: `center_lat_lon, terrain_mesh, max_radius`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.osm`
- **描述**: Generate the buildings stl file.

### `RoadPrep.create_roads`
- **参数**: `center_lat_lon, terrain_mesh, max_radius, z_offset, road_step, road_width`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.osm`
- **描述**: Generate the road stl file.

### `Choke.from_dict`
- **参数**: `cls, data`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.choke`
- **描述**: Create a Choke instance from a dictionary.

### `Choke.create_choke`
- **参数**: `app`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.choke`
- **描述**: Create a choke.

### `Choke.create_ground`
- **参数**: `app`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.choke`
- **描述**: Create the ground plane.

### `Part.zero_offset`
- **参数**: `kw`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.parts`
- **描述**: Check if the coordinate system defined by kw is [0, 0, 0].

### `Part.file_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.parts`
- **描述**: Antenna file name.

### `Part.cs_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.parts`
- **描述**: Coordinate system name.

### `Part.yaw_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.parts`
- **描述**: Yaw variable name. Yaw is the rotation about the object's Z-axis.

### `Part.pitch_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.parts`
- **描述**: Pitch variable name. Pitch is the rotation about the object's Y-axis.

### `Part.roll_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.parts`
- **描述**: Roll variable name. Roll is the rotation about the object's X-axis.

### `Part.local_origin`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.parts`
- **描述**: Local part offset values.

### `Part.yaw`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.parts`
- **描述**: Yaw variable value.

### `Part.yaw`
- **参数**: `yaw`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.parts`
- **描述**: No description provided.

### `Part.pitch`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.parts`
- **描述**: Pitch variable value.

### `Part.pitch`
- **参数**: `pitch`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.parts`
- **描述**: No description provided.

### `Part.roll`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.parts`
- **描述**: Roll variable value.

### `Part.roll`
- **参数**: `roll`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.parts`
- **描述**: No description provided.

### `Part.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.parts`
- **描述**: Part name.

### `Part.set_relative_cs`
- **参数**: `app`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.parts`
- **描述**: Create a parametric coordinate system.

### `Part.rot_cs_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.parts`
- **描述**: Rotation coordinate system name.

### `Antenna.params`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.parts`
- **描述**: Multi-part component parameters.

### `NamedVariable.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Name of the variable as a string.

### `NamedVariable.unit_system`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Unit system of the expression as a string.

### `NamedVariable.units`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Units.

### `NamedVariable.value`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Value.

### `NamedVariable.numeric_value`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Numeric part of the expression as a float value.

### `NamedVariable.evaluated_value`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: String that combines the numeric value and the units.

### `DuplicatedParametrizedMaterial.permittivity`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: No description provided.

### `DuplicatedParametrizedMaterial.permeability`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: No description provided.

### `DuplicatedParametrizedMaterial.conductivity`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: No description provided.

### `DuplicatedParametrizedMaterial.dielectric_loss_tangent`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: No description provided.

### `DuplicatedParametrizedMaterial.magnetic_loss_tangent`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: No description provided.

### `Layer3D.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Layer name.

### `Layer3D.type`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Layer type.

### `Layer3D.number`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Layer ID.

### `Layer3D.thickness`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Thickness variable.

### `Layer3D.thickness_value`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Thickness value.

### `Layer3D.thickness`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: No description provided.

### `Layer3D.elevation`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Layer elevation.

### `Layer3D.elevation_value`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Layer elevation value.

### `Layer3D.stackup`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Stackup.

### `Layer3D.add_patch`
- **参数**: `frequency, patch_width, patch_length, patch_position_x, patch_position_y, patch_name, axis`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Create a parametric patch.

### `Layer3D.add_trace`
- **参数**: `line_width, line_length, is_electrical_length, is_impedance, line_position_x, line_position_y, line_name, axis, reference_system, frequency`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Create a trace.

### `Layer3D.add_polygon`
- **参数**: `points, material, is_void, poly_name`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Create a polygon.

### `PadstackLayer.layer_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Padstack instance layer.

### `PadstackLayer.pad_radius`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Pad radius on the specified layer.

### `PadstackLayer.pad_radius`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: No description provided.

### `PadstackLayer.antipad_radius`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Antipad radius on the specified layer.

### `PadstackLayer.antipad_radius`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: No description provided.

### `Padstack.plating_ratio`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Plating ratio between 0 and 1.

### `Padstack.plating_ratio`
- **参数**: `val`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: No description provided.

### `Padstack.padstacks_by_layer`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Get the padstack definitions by layers.

### `Padstack.num_sides`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Number of sides on the circle, which is ``0`` for a true circle.

### `Padstack.num_sides`
- **参数**: `val`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: No description provided.

### `Padstack.set_all_pad_value`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Set all pads in all layers to a specified value.

### `Padstack.set_all_antipad_value`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Set all antipads in all layers to a specified value.

### `Padstack.set_start_layer`
- **参数**: `layer`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Set the start layer to a specified value.

### `Padstack.set_stop_layer`
- **参数**: `layer`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Set the stop layer to a specified value.

### `Padstack.add_via`
- **参数**: `position_x, position_y, instance_name, reference_system`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Insert a new via on this padstack.

### `Stackup3D.thickness`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Total stackup thickness.

### `Stackup3D.application`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Application object.

### `Stackup3D.padstacks`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: List of definitions created.

### `Stackup3D.dielectrics`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: List of dielectrics created.

### `Stackup3D.grounds`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: List of grounds created.

### `Stackup3D.signals`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: List of signals created.

### `Stackup3D.objects`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: List of objects created.

### `Stackup3D.objects_by_layer`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: List of definitions created.

### `Stackup3D.start_position`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Variable containing the start position.

### `Stackup3D.start_position`
- **参数**: `expression`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: No description provided.

### `Stackup3D.dielectric_x_position`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Stackup x origin.

### `Stackup3D.dielectric_x_position`
- **参数**: `expression`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: No description provided.

### `Stackup3D.dielectric_y_position`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Stackup y origin.

### `Stackup3D.dielectric_y_position`
- **参数**: `expression`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: No description provided.

### `Stackup3D.dielectric_width`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Stackup width.

### `Stackup3D.dielectric_width`
- **参数**: `expression`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: No description provided.

### `Stackup3D.dielectric_length`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Stackup length.

### `Stackup3D.dielectric_length`
- **参数**: `expression`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: No description provided.

### `Stackup3D.layer_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: List of all layer names.

### `Stackup3D.layer_positions`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: List of all layer positions.

### `Stackup3D.stackup_layers`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Dictionary of all stackup layers.

### `Stackup3D.z_position_offset`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Elevation.

### `Stackup3D.add_padstack`
- **参数**: `name, material`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Add a new padstack definition.

### `Stackup3D.add_layer`
- **参数**: `name, layer_type, material_name, thickness, fill_material, frequency`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Add a new layer to the stackup.

### `Stackup3D.add_signal_layer`
- **参数**: `name, material, thickness, fill_material, frequency`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Add a new ground layer to the stackup.

### `Stackup3D.add_dielectric_layer`
- **参数**: `name, material, thickness, frequency`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Add a new dielectric layer to the stackup.

### `Stackup3D.add_ground_layer`
- **参数**: `name, material, thickness, fill_material, frequency`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Add a new ground layer to the stackup.

### `Stackup3D.resize`
- **参数**: `percentage_offset`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Resize the stackup around objects created by a percentage offset.

### `Stackup3D.resize_around_element`
- **参数**: `element, percentage_offset`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Resize the stackup around parametrized objects and make it parametrize.

### `CommonObject.reference_system`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Coordinate system of the object.

### `CommonObject.dielectric_layer`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Dielectric layer that the object belongs to.

### `CommonObject.signal_layer`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Signal layer that the object belongs to.

### `CommonObject.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Object name.

### `CommonObject.application`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: App object.

### `CommonObject.aedt_object`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: PyAEDT object 3D.

### `CommonObject.layer_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Layer name.

### `CommonObject.layer_number`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Layer ID.

### `CommonObject.points_on_layer`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Object bounding box.

### `Patch.substrate_thickness`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Substrate thickness.

### `Patch.width`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Width.

### `Patch.position_x`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Starting position X.

### `Patch.position_y`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Starting position Y.

### `Patch.permittivity`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Permittivity.

### `Patch.effective_permittivity`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Effective permittivity.

### `Patch.added_length`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Added length calculation.

### `Patch.wave_length`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Wave length.

### `Patch.length`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Length.

### `Patch.impedance`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Impedance.

### `Patch.quarter_wave_feeding_line`
- **参数**: `impedance_to_adapt`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Create a Trace to feed the patch.

### `Patch.set_optimal_width`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Set the expression of the NamedVariable corresponding to the patch width, to an optimal expression.

### `Trace.substrate_thickness`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Substrate Thickness.

### `Trace.width`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Width.

### `Trace.width_h_w`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Width when the substrat thickness is two times upper than the width.

### `Trace.width_w_h`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Width when the width is two times upper than substrat thickness.

### `Trace.position_x`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Starting Position X.

### `Trace.position_y`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Starting Position Y.

### `Trace.permittivity`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Permittivity.

### `Trace.added_length`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Added Length.

### `Trace.length`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Length.

### `Trace.charac_impedance`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Characteristic Impedance.

### `Trace.effective_permittivity`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Effective Permittivity.

### `Trace.effective_permittivity_w_h`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Effective Permittivity when width is upper than dielectric thickness.

### `Trace.effective_permittivity_h_w`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Effective Permittivity when dielectric thickness is upper than width.

### `Trace.wave_length`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Wave Length.

### `Trace.electrical_length`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Electrical Length.

### `Polygon.points_on_layer`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.stackup_3d`
- **描述**: Object Bounding Box.

### `Person.stride`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.actors`
- **描述**: Stride in meters.

### `Person.stride`
- **参数**: `s`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.actors`
- **描述**: No description provided.

### `Radar.units`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.actors`
- **描述**: Multi-part units.

### `Radar.speed_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.actors`
- **描述**: Speed variable name.

### `MultiPartComponent.start`
- **参数**: `app`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: Initialize app for SBR+ simulation.

### `MultiPartComponent.cs_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: Coordinate system name.

### `MultiPartComponent.index`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: Number of multi-part components.

### `MultiPartComponent.offset_x_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: X-axis offset name.

### `MultiPartComponent.offset_y_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: Y-axis offset name.

### `MultiPartComponent.offset_z_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: Z-axis offset name.

### `MultiPartComponent.offset_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: X-, Y-, and Z-axis offset names.

### `MultiPartComponent.yaw_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: Yaw variable name. Yaw is the rotation about the object's Z-axis.

### `MultiPartComponent.yaw`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: Yaw variable value.

### `MultiPartComponent.yaw`
- **参数**: `yaw_str`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: No description provided.

### `MultiPartComponent.pitch_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: Pitch variable name. Pitch is the rotation about the object's Y-axis.

### `MultiPartComponent.pitch`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: Pitch variable value.

### `MultiPartComponent.pitch`
- **参数**: `pitch_str`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: No description provided.

### `MultiPartComponent.roll_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: Roll variable name. Roll is the rotation about the object's X-axis.

### `MultiPartComponent.roll`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: Roll variable value.

### `MultiPartComponent.roll`
- **参数**: `roll_str`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: No description provided.

### `MultiPartComponent.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: Unique instance name.

### `MultiPartComponent.use_global_cs`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: Global coordinate system.

### `MultiPartComponent.offset`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: Offset values for the multi-part component.

### `MultiPartComponent.offset`
- **参数**: `o`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: No description provided.

### `MultiPartComponent.position_in_app`
- **参数**: `app`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: Set up design variables and values to enable motion for the multi-part 3D component.

### `Environment.cs_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: Coordinate system name.

### `Environment.yaw`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: Yaw variable value. Yaw is the rotation about the object's Z-axis.

### `Environment.yaw`
- **参数**: `yaw_str`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: No description provided.

### `Environment.pitch`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: Pitch variable value. Pitch is the rotation about the object's Y-axis.

### `Environment.pitch`
- **参数**: `pitch_str`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: No description provided.

### `Environment.roll`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: Roll variable value. Roll is the rotation about the object's X-axis.

### `Environment.roll`
- **参数**: `roll_str`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: No description provided.

### `Environment.offset`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: Offset for the multi-part component.

### `Environment.offset`
- **参数**: `o`
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: No description provided.

### `Actor.speed_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.multiparts`
- **描述**: Speed variable name.

### `Coil.create_flat_path`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.coil`
- **描述**: No description provided.

### `Coil.create_vertical_path`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.advanced_cad.coil`
- **描述**: No description provided.

### `MaxwellCircuitComponents.tab_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_maxwell_circuit`
- **描述**: Tab name.

### `MaxwellCircuitComponents.create_resistor`
- **参数**: `name, value, location, angle, use_instance_id_netlist`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_maxwell_circuit`
- **描述**: Create a resistor.

### `MaxwellCircuitComponents.create_inductor`
- **参数**: `name, value, location, angle, use_instance_id_netlist`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_maxwell_circuit`
- **描述**: Create an inductor.

### `MaxwellCircuitComponents.create_capacitor`
- **参数**: `name, value, location, angle, use_instance_id_netlist`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_maxwell_circuit`
- **描述**: Create a capacitor.

### `MaxwellCircuitComponents.create_diode`
- **参数**: `name, location, angle, use_instance_id_netlist`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_maxwell_circuit`
- **描述**: Create a diode.

### `MaxwellCircuitComponents.create_winding`
- **参数**: `name, location, angle, use_instance_id_netlist`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_maxwell_circuit`
- **描述**: Create a winding linked to a Maxwell design.

### `CircuitComponents.wires`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: All schematic wires in the design.

### `CircuitComponents.o_definition_manager`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: AEDT oDefinitionManager.

### `CircuitComponents.ocomponent_manager`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Component manager object.

### `CircuitComponents.osymbol_manager`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Model manager object.

### `CircuitComponents.version`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Version.

### `CircuitComponents.model_units`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Model units.

### `CircuitComponents.schematic_units`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Schematic units.

### `CircuitComponents.schematic_units`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: No description provided.

### `CircuitComponents.nets`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: List of all schematic nets.

### `CircuitComponents.create_unique_id`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Create an unique ID.

### `CircuitComponents.create_gnd`
- **参数**: `location, angle, page`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Create a ground.

### `CircuitComponents.create_model_from_touchstone`
- **参数**: `input_file, model_name, show_bitmap, image_path`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Create a model from a Touchstone file.

### `CircuitComponents.create_model_from_nexxim_state_space`
- **参数**: `input_file, num_terminal, model_name, port_names`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Create a model from a Touchstone file.

### `CircuitComponents.create_touchstone_component`
- **参数**: `model_name, location, angle, show_bitmap, page, image_path`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Create a component from a Touchstone model.

### `CircuitComponents.create_nexxim_state_space_component`
- **参数**: `model_name, num_terminal, location, angle, port_names, page`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Create a component from a Touchstone model.

### `CircuitComponents.create_component`
- **参数**: `name, component_library, component_name, location, angle, use_instance_id_netlist, global_netlist_list, page`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Create a component from a library.

### `CircuitComponents.disable_data_netlist`
- **参数**: `assignment`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Disable the Nexxim global net list.

### `CircuitComponents.enable_global_netlist`
- **参数**: `assignment, global_netlist_list`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Enable Nexxim global net list.

### `CircuitComponents.create_symbol`
- **参数**: `name, pins`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Create a symbol.

### `CircuitComponents.enable_use_instance_name`
- **参数**: `component_library, component_name`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Enable the use of the instance name.

### `CircuitComponents.refresh_all_ids`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Refresh all IDs and return the number of components.

### `CircuitComponents.add_id_to_component`
- **参数**: `component_id, name`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Add an ID to a component.

### `CircuitComponents.create_line`
- **参数**: `points, color, width, page`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Draw a graphical line.

### `CircuitComponents.create_wire`
- **参数**: `points, name, page`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Create a wire.

### `ComponentInfo.props`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Retrieve the component properties.

### `ComponentInfo.place`
- **参数**: `assignment, location, angle, use_instance_id_netlist, page`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Create a component from a library.

### `ComponentCatalog.find_components`
- **参数**: `filter_str`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_circuit`
- **描述**: Find all components with given filter wildcards.

### `CircuitPins.units`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Length units.

### `CircuitPins.total_angle`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Return the pin orientation in the schematic.

### `CircuitPins.location`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Pin Position in [x,y] format.

### `CircuitPins.net`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Get pin net.

### `CircuitPins.angle`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Pin angle.

### `CircuitPins.connect_to_component`
- **参数**: `assignment, page_name, use_wire, wire_name, clearance_units, page_port_angle, offset`
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Connect schematic components.

### `ModelParameters.update`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Update the model properties.

### `CircuitComponent.composed_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Composed names.

### `CircuitComponent.instance_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Instance name.

### `CircuitComponent.instance_name`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: No description provided.

### `CircuitComponent.delete`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Delete the component.

### `CircuitComponent.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Name of the component.

### `CircuitComponent.name`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: No description provided.

### `CircuitComponent.refdes`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Reference designator.

### `CircuitComponent.units`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Length units.

### `CircuitComponent.model_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Return Model Name if present.

### `CircuitComponent.model_data`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Return the model data if the component has one.

### `CircuitComponent.component_info`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Component parameters.

### `CircuitComponent.bounding_box`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Component bounding box.

### `CircuitComponent.pins`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Pins of the component.

### `CircuitComponent.page`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Get the page where the component is located.

### `CircuitComponent.location`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Get the part location.

### `CircuitComponent.location`
- **参数**: `location_xy`
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Set the part location.

### `CircuitComponent.angle`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Get the part angle.

### `CircuitComponent.angle`
- **参数**: `angle`
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Set the part angle.

### `CircuitComponent.mirror`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Get the part mirror.

### `CircuitComponent.mirror`
- **参数**: `mirror_value`
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Mirror part.

### `CircuitComponent.set_use_symbol_color`
- **参数**: `color`
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Set symbol color usage.

### `CircuitComponent.set_color`
- **参数**: `red, green, blue`
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Set symbol color.

### `CircuitComponent.set_property`
- **参数**: `name, value`
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Set a part property.

### `CircuitComponent.change_property`
- **参数**: `property_name, names`
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Modify a property.

### `CircuitComponent.enforce_touchstone_model_passive`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Enforce touchstone model passive.

### `CircuitComponent.change_symbol_pin_locations`
- **参数**: `pin_locations, keep_original_size`
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Change the locations of symbol pins.

### `CircuitComponent.component_path`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Component definition path.

### `Wire.points_in_segment`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Points in segment.

### `Wire.logger`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Logger.

### `Wire.wires`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: List of all schematic wires in the design.

### `Wire.display_wire_properties`
- **参数**: `name, property_to_display, visibility, location`
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Display wire properties.

### `Wire.set_net_name`
- **参数**: `name, split_wires`
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Set wire net name.

### `Excitations.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Excitation name.

### `Excitations.name`
- **参数**: `port_name`
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: No description provided.

### `Excitations.composed_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Composed names.

### `Excitations.impedance`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Port termination.

### `Excitations.impedance`
- **参数**: `termination`
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: No description provided.

### `Excitations.enable_noise`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Enable noise.

### `Excitations.enable_noise`
- **参数**: `enable`
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: No description provided.

### `Excitations.noise_temperature`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Enable noise.

### `Excitations.noise_temperature`
- **参数**: `noise`
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: No description provided.

### `Excitations.microwave_symbol`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Enable microwave symbol.

### `Excitations.microwave_symbol`
- **参数**: `enable`
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: No description provided.

### `Excitations.reference_node`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Reference node.

### `Excitations.reference_node`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Set the reference node of the port.

### `Excitations.enabled_sources`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Enabled sources.

### `Excitations.enabled_sources`
- **参数**: `sources`
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: No description provided.

### `Excitations.enabled_analyses`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Enabled analyses.

### `Excitations.enabled_analyses`
- **参数**: `analyses`
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: No description provided.

### `Excitations.update`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Update the excitation in AEDT.

### `Excitations.delete`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.object_3d_circuit`
- **描述**: Delete the port in AEDT.

### `TwinBuilderComponents.tab_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_twin_builder`
- **描述**: Tab name.

### `TwinBuilderComponents.components_catalog`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_twin_builder`
- **描述**: Return the syslib component catalog with all info.

### `TwinBuilderComponents.o_simmodel_manager`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_twin_builder`
- **描述**: Simulation models manager object.

### `TwinBuilderComponents.create_resistor`
- **参数**: `name, value, location, angle, use_instance_id_netlist`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_twin_builder`
- **描述**: Create a resistor.

### `TwinBuilderComponents.create_inductor`
- **参数**: `name, value, location, angle, use_instance_id_netlist`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_twin_builder`
- **描述**: Create an inductor.

### `TwinBuilderComponents.create_capacitor`
- **参数**: `name, value, location, angle, use_instance_id_netlist`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_twin_builder`
- **描述**: Create a capacitor.

### `TwinBuilderComponents.create_voltage_source`
- **参数**: `name, source_type, amplitude, freq, location, angle, use_instance_id_netlist`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_twin_builder`
- **描述**: Create a voltage source (conservative electrical output).

### `TwinBuilderComponents.create_diode`
- **参数**: `name, location, angle, use_instance_id_netlist`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_twin_builder`
- **描述**: Create a diode.

### `TwinBuilderComponents.create_npn`
- **参数**: `name, location, angle, use_instance_id_netlist`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_twin_builder`
- **描述**: Create an NPN transistor.

### `TwinBuilderComponents.create_pnp`
- **参数**: `name, location, angle, use_instance_id_netlist`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_twin_builder`
- **描述**: Create a PNP transistor.

### `TwinBuilderComponents.create_periodic_waveform_source`
- **参数**: `name, waveform_type, amplitude, freq, phase, offset, delay, location, angle, use_instance_id_netlist`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_twin_builder`
- **描述**: Create a periodic waveform source (non conservative real output).

### `TwinBuilderComponents.create_component_from_sml`
- **参数**: `input_file, model, pins_names`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_twin_builder`
- **描述**: Create and place a new component based on a .sml file.

### `TwinBuilderComponents.update_quantity_value`
- **参数**: `component_name, name, value, netlist_units`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_twin_builder`
- **描述**: Change the quantity value of a component.

### `EmitComponents.oeditor`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Oeditor Module.

### `EmitComponents.messenger`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Messenger.

### `EmitComponents.version`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Version.

### `EmitComponents.model_units`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Model units.

### `EmitComponents.omodel_manager`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: AEDT model manager.

### `EmitComponents.o_definition_manager`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: AEDT definition manager.

### `EmitComponents.osymbol_manager`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: AEDT Symbol Manager.

### `EmitComponents.ocomponent_manager`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: AEDT Component Manager.

### `EmitComponents.include_personal_library`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Include personal library.

### `EmitComponents.include_personal_library`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: No description provided.

### `EmitComponents.components_catalog`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: System library component catalog with all information.

### `EmitComponents.create_component`
- **参数**: `component_type, name, library`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Create a new component from a library.

### `EmitComponents.create_radio_antenna`
- **参数**: `radio_type, radio_name, antenna_name, library`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Create a new radio and antenna and connect them.

### `EmitComponents.refresh_all_ids`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Refresh all IDs and return the number of components.

### `EmitComponents.update_object_properties`
- **参数**: `o`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Update the properties of an EMIT component.

### `EmitComponent.register_subclass`
- **参数**: `cls, root_node_type`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: No description provided.

### `EmitComponent.create`
- **参数**: `cls, components, component_name`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Create an EMIT component.

### `EmitComponent.composed_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Component name. Needed for compatibility.

### `EmitComponent.update_property_tree`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Update the nodes (property groups) for this component.

### `EmitRadioComponent.is_emitter`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Check if the radio component is an emitter

### `EmitRadioComponent.bands`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Get the bands of this radio.

### `EmitRadioComponent.band_node`
- **参数**: `band_name`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Get the specified band node from this radio.

### `EmitRadioComponent.band_channel_bandwidth`
- **参数**: `band_node, units`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Get the channel bandwidth of the band node.

### `EmitRadioComponent.band_tx_power`
- **参数**: `band_node, units`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Get the transmit power of the band node.

### `EmitRadioComponent.has_tx_channels`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Check the radio for enabled transmit channels.

### `EmitRadioComponent.has_rx_channels`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Check the radio for enabled receive channels.

### `EmitComponentPropNode.props`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Returns a dictionary of all the properties for this node.

### `EmitComponentPropNode.enabled`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Returns ''True'' if the node is enabled and ''False'' if the node is disabled.

### `EmitComponentPropNode.set_band_power_level`
- **参数**: `power, units`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Set the power of the fundamental for the given band.

### `EmitComponentPropNode.set_channel_sampling`
- **参数**: `sampling_type, percentage, max_channels, seed`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Set the channel sampling for the radio.

### `EmitComponentPropNode.enabled`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_emit`
- **描述**: Set the node enabled or disabled.

### `NexximComponents.tab_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Tab name.

### `NexximComponents.delete_component`
- **参数**: `name`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Get and delete a component.

### `NexximComponents.components_catalog`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: System library component catalog with all information.

### `NexximComponents.create_subcircuit`
- **参数**: `location, angle, name, nested_subcircuit_id`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Add a new Circuit subcircuit to the design.

### `NexximComponents.duplicate`
- **参数**: `assignment, location, angle, flip`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Add a new subcircuit to the design.

### `NexximComponents.connect_components_in_series`
- **参数**: `assignment, use_wire`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Connect schematic components in series.

### `NexximComponents.connect_components_in_parallel`
- **参数**: `assignment`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Connect schematic components in parallel.

### `NexximComponents.add_subcircuit_3dlayout`
- **参数**: `name`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Add a subcircuit from a HFSS 3DLayout.

### `NexximComponents.create_field_model`
- **参数**: `design_name, solution_name, pin_names, model_type`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Create a field model.

### `NexximComponents.create_resistor`
- **参数**: `name, value, location, angle, use_instance_id_netlist, page`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Create a resistor.

### `NexximComponents.create_inductor`
- **参数**: `name, value, location, angle, use_instance_id_netlist, page`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Create an inductor.

### `NexximComponents.create_capacitor`
- **参数**: `name, value, location, angle, use_instance_id_netlist, page`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Create a capacitor.

### `NexximComponents.create_voltage_dc`
- **参数**: `name, value, location, angle, use_instance_id_netlist, page`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Create a voltage DC source.

### `NexximComponents.create_current_pulse`
- **参数**: `name, value_lists, location, angle, use_instance_id_netlist, page`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Create a current pulse.

### `NexximComponents.create_voltage_pulse`
- **参数**: `name, value_lists, location, angle, use_instance_id_netlist, page`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Create a voltage pulse.

### `NexximComponents.create_voltage_pwl`
- **参数**: `name, time_list, voltage_list, location, angle, use_instance_id_netlist, page`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Create a pwl voltage source.

### `NexximComponents.create_current_dc`
- **参数**: `name, value, location, angle, use_instance_id_netlist, page`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Create a current DC source.

### `NexximComponents.create_coupling_inductors`
- **参数**: `compname, l1, l2, value, location, angle, use_instance_id_netlist, page`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Create a coupling inductor.

### `NexximComponents.create_diode`
- **参数**: `name, model_name, location, angle, use_instance_id_netlist, page`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Create a diode.

### `NexximComponents.create_npn`
- **参数**: `name, value, location, angle, use_instance_id_netlist, page`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Create an NPN transistor.

### `NexximComponents.create_pnp`
- **参数**: `name, value, location, angle, use_instance_id_netlist, page`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Create a PNP transistor.

### `NexximComponents.create_new_component_from_symbol`
- **参数**: `name, pins, time_stamp, description, refbase, parameters, values, gref`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Create a component from a symbol.

### `NexximComponents.add_subcircuit_dynamic_link`
- **参数**: `pyaedt_app, solution_name, extrusion_length, enable_cable_modeling, default_matrix, tline_port, name`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Add a subcircuit from `HFSS`, `Q3d` or `2D Extractor` in circuit design.

### `NexximComponents.refresh_dynamic_link`
- **参数**: `name`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Refresh a dynamic link component.

### `NexximComponents.create_component_from_spicemodel`
- **参数**: `input_file, model, create_component, location, symbol_path, symbol, page`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Create and place a new component based on a spice .lib file.

### `NexximComponents.add_siwave_dynamic_link`
- **参数**: `input_file, solution, simulate_solutions`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Add a siwave dinamyc link object.

### `NexximComponents.add_q3d_rlgc`
- **参数**: `pyaedt_app, solution_name, matrix, name`
- **模块**: `ansys.aedt.core.modeler.circuits.primitives_nexxim`
- **描述**: Add a Q3D RLGC dynamic link to a circuit design.

### `Object3d.is_polyline`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Get or set if the body is originated by a polyline.

### `Object3d.is_polyline`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: No description provided.

### `Object3d.bounding_box`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Bounding box of a part.

### `Object3d.bounding_dimension`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Retrieve the dimension array of the bounding box.

### `Object3d.touching_conductors`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Get the conductors of given object.

### `Object3d.touching_objects`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Get the objects that touch a vertex, edge midpoint, or face of the object.

### `Object3d.faces`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Information for each face in the given part.

### `Object3d.faces_on_bounding_box`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Return only the face ids of the faces touching the bounding box.

### `Object3d.largest_face`
- **参数**: `n`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Return only the face with the greatest area.

### `Object3d.longest_edge`
- **参数**: `n`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Return only the edge with the greatest length.

### `Object3d.smallest_face`
- **参数**: `n`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Return only the face with the smallest area.

### `Object3d.shortest_edge`
- **参数**: `n`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Return only the edge with the smallest length.

### `Object3d.top_face_z`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Top face in the Z direction of the object.

### `Object3d.bottom_face_z`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Bottom face in the Z direction of the object.

### `Object3d.top_face_x`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Top face in the X direction of the object.

### `Object3d.bottom_face_x`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Bottom face in the X direction of the object.

### `Object3d.top_face_y`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Top face in the Y direction of the object.

### `Object3d.bottom_face_y`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Bottom face in the X direction of the object.

### `Object3d.top_edge_z`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Top edge in the Z direction of the object. Midpoint is used as criteria to find the edge.

### `Object3d.bottom_edge_z`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Bottom edge in the Z direction of the object. Midpoint is used as criteria to find the edge.

### `Object3d.top_edge_x`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Top edge in the X direction of the object. Midpoint is used as criteria to find the edge.

### `Object3d.bottom_edge_x`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Bottom edge in the X direction of the object. Midpoint is used as criteria to find the edge.

### `Object3d.top_edge_y`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Top edge in the Y direction of the object. Midpoint is used as criteria to find the edge.

### `Object3d.bottom_edge_y`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Bottom edge in the Y direction of the object. Midpoint is used as criteria to find the edge.

### `Object3d.edges`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Information for each edge in the given part.

### `Object3d.vertices`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Information for each vertex in the given part.

### `Object3d.logger`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Logger.

### `Object3d.group_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Group the object belongs to.

### `Object3d.group_name`
- **参数**: `name`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Assign Object to a specific group. It creates a new group if the group doesn't exist.

### `Object3d.is_conductor`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Check if the object is a conductor.

### `Object3d.id`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: ID of the object.

### `Object3d.object_type`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Type of the object.

### `Object3d.is3d`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Check if the object is a 3D solid object.

### `Object3d.is_3d`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Check if the object is a 3D solid object.

### `Object3d.mass`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Object mass.

### `Object3d.volume`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Object volume.

### `Object3d.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Name of the object as a string value.

### `Object3d.name`
- **参数**: `obj_name`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: No description provided.

### `Object3d.valid_properties`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Valid properties.

### `Object3d.color`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Part color as a tuple of integer values for `(Red, Green, Blue)` color values.

### `Object3d.color_string`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Color tuple as a string in the format '(Red, Green, Blue)'.

### `Object3d.color`
- **参数**: `color_value`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: No description provided.

### `Object3d.transparency`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Part transparency as a value between 0.0 and 1.0.

### `Object3d.transparency`
- **参数**: `T`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: No description provided.

### `Object3d.object_units`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Object units.

### `Object3d.part_coordinate_system`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Part coordinate system.

### `Object3d.part_coordinate_system`
- **参数**: `sCS`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: No description provided.

### `Object3d.solve_inside`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Part solve inside flag.

### `Object3d.solve_inside`
- **参数**: `S`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: No description provided.

### `Object3d.display_wireframe`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Wireframe property of the part.

### `Object3d.display_wireframe`
- **参数**: `fWireframe`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: No description provided.

### `Object3d.history`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Object history.

### `Object3d.is_model`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Part model or non-model property.

### `Object3d.is_model`
- **参数**: `fModel`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: No description provided.

### `Object3d.model`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Part model or non-model property.

### `Object3d.model`
- **参数**: `fModel`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: No description provided.

### `Object3d.intersect`
- **参数**: `assignment, keep_originals`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Intersect the active object with a given list.

### `Object3d.split`
- **参数**: `plane, sides`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Split the active object.

### `Object3d.mirror`
- **参数**: `origin, vector, duplicate`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Mirror a selection.

### `Object3d.duplicate_around_axis`
- **参数**: `axis, angle, clones, create_new_objects`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Duplicate the object around the axis.

### `Object3d.duplicate_along_line`
- **参数**: `vector, clones, attach`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Duplicate the object along a line.

### `Object3d.section`
- **参数**: `plane, create_new, section_cross_object`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Section the object.

### `Object3d.detach_faces`
- **参数**: `faces`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Section the object.

### `Object3d.clone`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Clone the object and return the new 3D object.

### `Object3d.wrap_sheet`
- **参数**: `object_name, imprinted`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Execute the sheet wrapping around an object. This object can be either the sheet or the object.

### `Object3d.delete`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Delete the object.

### `Object3d.faces_by_area`
- **参数**: `area, area_filter, tolerance`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Filter faces by area.

### `Object3d.edges_by_length`
- **参数**: `length, length_filter, tolerance`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Filter edges by length.

### `Object3d.fillet`
- **参数**: `vertices, edges, radius, setback`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Add a fillet to the selected edges in 3D/vertices in 2D.

### `Object3d.chamfer`
- **参数**: `vertices, edges, left_distance, right_distance, angle, chamfer_type`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Add a chamfer to the selected edges in 3D/vertices in 2D.

### `Object3d.start_point`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Get the starting point in the polyline object.

### `Object3d.end_point`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: List of the ``[x, y, z]`` coordinates for the ending point in the polyline

### `Object3d.points`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Polyline Points.

### `Object3d.segment_types`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: List of the segment types of the polyline.

### `Object3d.vertex_positions`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: List of the ``[x, y, z]`` coordinates for all vertex positions in the

### `Object3d.set_crosssection_properties`
- **参数**: `section, orient, width, topwidth, height, num_seg, bend_type`
- **模块**: `ansys.aedt.core.modeler.cad.object_3d`
- **描述**: Set the properties of an existing polyline object.

### `UserDefinedComponent.layout_component`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Layout component object.

### `UserDefinedComponent.history`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Component history.

### `UserDefinedComponent.group_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Group the component belongs to.

### `UserDefinedComponent.group_name`
- **参数**: `name`
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Assign component to a specific group. A new group is created if the specified group doesn't exist.

### `UserDefinedComponent.is3dcomponent`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: 3DComponent flag.

### `UserDefinedComponent.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Name of the object.

### `UserDefinedComponent.name`
- **参数**: `component_name`
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: No description provided.

### `UserDefinedComponent.parts`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Dictionary of objects that belong to the user-defined component.

### `UserDefinedComponent.delete`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Delete the object.

### `UserDefinedComponent.duplicate_and_mirror`
- **参数**: `origin, vector`
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Duplicate and mirror a selection.

### `UserDefinedComponent.mirror`
- **参数**: `origin, vector`
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Mirror a selection.

### `UserDefinedComponent.duplicate_around_axis`
- **参数**: `axis, angle, clones, create_new_objects`
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Duplicate the component around the axis.

### `UserDefinedComponent.duplicate_along_line`
- **参数**: `vector, clones, attach`
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Duplicate the object along a line.

### `UserDefinedComponent.update_native`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Update the Native Component in AEDT.

### `UserDefinedComponent.bounding_box`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Get bounding dimension of a user defined model.

### `UserDefinedComponent.center`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Get center coordinates of a user defined model.

### `UserDefinedComponent.update_definition`
- **参数**: `password, output_file, local_update`
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Update 3d component definition.

### `UserDefinedComponent.edit_definition`
- **参数**: `password`
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Edit 3d Definition. Open AEDT Project and return Pyaedt Object.

### `LayoutComponent.edb_path`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: EDB path.

### `LayoutComponent.edb_object`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: EDB object.

### `LayoutComponent.edb_definition`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Edb definition.

### `LayoutComponent.show_layout`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Show layout flag.

### `LayoutComponent.show_layout`
- **参数**: `show_layout`
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: No description provided.

### `LayoutComponent.fast_transformation`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Show layout flag.

### `LayoutComponent.fast_transformation`
- **参数**: `fast_transformation`
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: No description provided.

### `LayoutComponent.show_dielectric`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Show dielectric flag.

### `LayoutComponent.show_dielectric`
- **参数**: `show_dielectric`
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: No description provided.

### `LayoutComponent.display_mode`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Show layout flag.

### `LayoutComponent.display_mode`
- **参数**: `display_mode`
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: No description provided.

### `LayoutComponent.update_visibility`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.components_3d`
- **描述**: Update layer visibility.

### `Primitives2D.plane2d`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives_2d`
- **描述**: Create a 2D plane.

### `Primitives2D.create_circle`
- **参数**: `origin, radius, num_sides, is_covered, name, material, non_model`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_2d`
- **描述**: Create a circle.

### `Primitives2D.create_ellipse`
- **参数**: `origin, major_radius, ratio, is_covered, name, material, non_model, segments`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_2d`
- **描述**: Create an ellipse.

### `Primitives2D.create_regular_polygon`
- **参数**: `origin, start_point, num_sides, name, material, non_model`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_2d`
- **描述**: Create a rectangle.

### `Primitives2D.create_region`
- **参数**: `pad_value, pad_type, name`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_2d`
- **描述**: Create an air region.

### `BaseCoordinateSystem.set_as_working_cs`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Set the coordinate system as the working coordinate system.

### `BaseCoordinateSystem.rename`
- **参数**: `name`
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Rename the coordinate system.

### `BaseCoordinateSystem.delete`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Delete the coordinate system.

### `FaceCoordinateSystem.props`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Properties of the coordinate system.

### `FaceCoordinateSystem.create`
- **参数**: `assignment, origin, axis_position, axis, name, offset, rotation, always_move_to_end`
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Create a face coordinate system.

### `FaceCoordinateSystem.update`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Update the coordinate system.

### `CoordinateSystem.mode`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Coordinate System mode.

### `CoordinateSystem.mode`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: No description provided.

### `CoordinateSystem.props`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Coordinate System Properties.

### `CoordinateSystem.ref_cs`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Reference coordinate system getter and setter.

### `CoordinateSystem.ref_cs`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: No description provided.

### `CoordinateSystem.update`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Update the coordinate system.

### `CoordinateSystem.change_cs_mode`
- **参数**: `mode_type`
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Change the mode of the coordinate system.

### `CoordinateSystem.create`
- **参数**: `origin, reference_cs, name, mode, view, x_pointing, y_pointing, phi, theta, psi, u`
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Create a coordinate system.

### `CoordinateSystem.pointing_to_axis`
- **参数**: `x_pointing, y_pointing`
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Retrieve the axes from the HFSS X axis and Y pointing axis as per

### `CoordinateSystem.quaternion`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Quaternion computed based on specific axis mode.

### `CoordinateSystem.origin`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Coordinate system origin in model units.

### `CoordinateSystem.origin`
- **参数**: `origin`
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Set the coordinate system origin in model units.

### `ObjectCoordinateSystem.ref_cs`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Reference coordinate system.

### `ObjectCoordinateSystem.ref_cs`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: No description provided.

### `ObjectCoordinateSystem.props`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Properties of the coordinate system.

### `ObjectCoordinateSystem.create`
- **参数**: `assignment, origin, x_axis, y_axis, move_to_end, reverse_x_axis, reverse_y_axis`
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Create an object coordinate system.

### `ObjectCoordinateSystem.update`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Update the coordinate system.

### `Lists.update`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Update the List.

### `Lists.create`
- **参数**: `assignment, name, entity_type`
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Create a List.

### `Lists.delete`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Delete the List.

### `Lists.rename`
- **参数**: `name`
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Rename the List.

### `Modeler.logger`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Logger.

### `Modeler.projdir`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.modeler`
- **描述**: Project directory.

### `Primitives3D.create_polyhedron`
- **参数**: `orientation, center, origin, height, num_sides, name, material`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_3d`
- **描述**: Create a regular polyhedron.

### `Primitives3D.create_cone`
- **参数**: `orientation, origin, bottom_radius, top_radius, height, name, material`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_3d`
- **描述**: Create a cone.

### `Primitives3D.create_torus`
- **参数**: `origin, major_radius, minor_radius, axis, name, material`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_3d`
- **描述**: Create a torus.

### `Primitives3D.create_bondwire`
- **参数**: `start, end, h1, h2, alpha, beta, bond_type, diameter, facets, name, material, orientation`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_3d`
- **描述**: Create a bondwire.

### `Primitives3D.create_circle`
- **参数**: `orientation, origin, radius, num_sides, is_covered, name, material, non_model`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_3d`
- **描述**: Create a circle.

### `Primitives3D.create_ellipse`
- **参数**: `orientation, origin, major_radius, ratio, is_covered, name, material, segments`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_3d`
- **描述**: Create an ellipse.

### `Primitives3D.create_equationbased_curve`
- **参数**: `x_t, y_t, z_t, t_start, t_end, num_points, name, xsection_type, xsection_orient, xsection_width, xsection_topwidth, xsection_height, xsection_num_seg, xsection_bend_type`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_3d`
- **描述**: Create an equation-based curve.

### `Primitives3D.create_equationbased_surface`
- **参数**: `x_uv, y_uv, z_uv, u_start, u_end, v_start, v_end, name`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_3d`
- **描述**: Create an equation-based surface.

### `Primitives3D.create_helix`
- **参数**: `assignment, origin, x_start_dir, y_start_dir, z_start_dir, turns, right_hand, radius_increment, thread`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_3d`
- **描述**: Create a helix from a polyline.

### `Primitives3D.create_udm`
- **参数**: `udm_full_name, parameters, library, name`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_3d`
- **描述**: Create a user-defined model.

### `Primitives3D.create_spiral`
- **参数**: `internal_radius, spacing, faces, turns, width, thickness, elevation, material, name`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_3d`
- **描述**: Create a spiral inductor from a polyline.

### `Primitives3D.add_layout_component_definition`
- **参数**: `file_path, name`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_3d`
- **描述**: Add a layout submodel definition to the design.

### `Primitives3D.add_person`
- **参数**: `input_dir, speed, global_offset, yaw, pitch, roll, coordinate_system, name`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_3d`
- **描述**: Add a Walking Person Multipart from 3D Components.

### `Primitives3D.add_vehicle`
- **参数**: `input_dir, speed, global_offset, yaw, pitch, roll, coordinate_system, name`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_3d`
- **描述**: Add a Moving Vehicle Multipart from 3D Components.

### `Primitives3D.add_bird`
- **参数**: `input_dir, speed, global_offset, yaw, pitch, roll, flapping_rate, coordinate_system, name`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_3d`
- **描述**: Add a Bird Multipart from 3D Components.

### `Primitives3D.add_environment`
- **参数**: `input_dir, global_offset, yaw, pitch, roll, coordinate_system, name`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_3d`
- **描述**: Add an Environment Multipart Component from JSON file.

### `Primitives3D.create_choke`
- **参数**: `input_file`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_3d`
- **描述**: Create a choke from a JSON setting file.

### `Primitives3D.check_choke_values`
- **参数**: `input_dir, create_another_file`
- **模块**: `ansys.aedt.core.modeler.cad.primitives_3d`
- **描述**: Verify the values in the json file and create another one with corrected values next to the first one.

### `ModifiablePrimitive.fillet`
- **参数**: `radius, setback`
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Add a fillet to the selected edges in 3D/vertices in 2D.

### `ModifiablePrimitive.chamfer`
- **参数**: `left_distance, right_distance, angle, chamfer_type`
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Add a chamfer to the selected edges in 3D/vertices in 2D.

### `VertexPrimitive.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Name of the object.

### `VertexPrimitive.position`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Position of the vertex.

### `EdgePrimitive.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Name of the object.

### `EdgePrimitive.segment_info`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Compute segment information using the object-oriented method (from AEDT 2021 R2

### `EdgePrimitive.vertices`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Vertices list.

### `EdgePrimitive.midpoint`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Midpoint coordinates of the edge.

### `EdgePrimitive.length`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Length of the edge.

### `EdgePrimitive.create_object`
- **参数**: `non_model`
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Return a new object from the selected edge.

### `EdgePrimitive.fillet`
- **参数**: `radius, setback`
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Add a fillet to the selected edges in 3D/vertices in 2D.

### `EdgePrimitive.chamfer`
- **参数**: `left_distance, right_distance, angle, chamfer_type`
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Add a chamfer to the selected edges in 3D/vertices in 2D.

### `FacePrimitive.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Name of the object.

### `FacePrimitive.oeditor`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Oeditor Module.

### `FacePrimitive.logger`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Logger.

### `FacePrimitive.touching_objects`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Get the objects that touch one of the vertex, edge midpoint or the actual face.

### `FacePrimitive.edges`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Edges lists.

### `FacePrimitive.vertices`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Vertices lists.

### `FacePrimitive.id`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Face ID.

### `FacePrimitive.center_from_aedt`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Face center for a planar face in model units.

### `FacePrimitive.is_planar`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Check if a face is planar or not.

### `FacePrimitive.center`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Face center in model units.

### `FacePrimitive.area`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Face area.

### `FacePrimitive.top_edge_z`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Top edge in the Z direction of the object. Midpoint is used as criteria to find the edge.

### `FacePrimitive.bottom_edge_z`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Bottom edge in the Z direction of the object. Midpoint is used as criteria to find the edge.

### `FacePrimitive.top_edge_x`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Top edge in the X direction of the object. Midpoint is used as criteria to find the edge.

### `FacePrimitive.bottom_edge_x`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Bottom edge in the X direction of the object. Midpoint is used as criteria to find the edge.

### `FacePrimitive.top_edge_y`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Top edge in the Y direction of the object. Midpoint is used as criteria to find the edge.

### `FacePrimitive.bottom_edge_y`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Bottom edge in the X direction of the object. Midpoint is used as criteria to find the edge.

### `FacePrimitive.is_on_bounding`
- **参数**: `tolerance`
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Check if the face is on bounding box or Not.

### `FacePrimitive.normal`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Face normal.

### `FacePrimitive.create_object`
- **参数**: `non_model`
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Return a new object from the selected face.

### `Point.logger`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Logger.

### `Point.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Name of the point as a string value.

### `Point.name`
- **参数**: `point_name`
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: No description provided.

### `Point.valid_properties`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Valid properties.

### `Point.set_color`
- **参数**: `color_value`
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Set symbol color.

### `Point.coordinate_system`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Coordinate system of the point.

### `Point.coordinate_system`
- **参数**: `new_coordinate_system`
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: No description provided.

### `Point.delete`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Delete the point.

### `Plane.logger`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Logger.

### `Plane.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Name of the plane as a string value.

### `Plane.name`
- **参数**: `plane_name`
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: No description provided.

### `Plane.valid_properties`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Valid properties.

### `Plane.set_color`
- **参数**: `color_value`
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Set symbol color.

### `Plane.coordinate_system`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Coordinate system of the plane.

### `Plane.coordinate_system`
- **参数**: `new_coordinate_system`
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: No description provided.

### `Plane.delete`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Delete the plane.

### `HistoryProps.pop`
- **参数**: `key, default`
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: No description provided.

### `BinaryTreeNode.children`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: No description provided.

### `BinaryTreeNode.properties`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Properties data.

### `BinaryTreeNode.command`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Command of the modeler hystory if available.

### `BinaryTreeNode.update_property`
- **参数**: `prop_name, prop_value`
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Update the property of the binary tree node.

### `BinaryTreeNode.jsonalize_tree`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Create dictionary from the Binary Tree.

### `BinaryTreeNode.suppress_all`
- **参数**: `app`
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Activate suppress option for all the operations contained in the binary tree node.

### `BinaryTreeNode.unsuppress_all`
- **参数**: `app`
- **模块**: `ansys.aedt.core.modeler.cad.elements_3d`
- **描述**: Disable suppress option for all the operations contained in the binary tree node.

### `Objects.keys`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: No description provided.

### `Objects.values`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: No description provided.

### `Objects.items`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: No description provided.

### `GeometryModeler.rescale_model`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Whether to rescale the model to model units.

### `GeometryModeler.rescale_model`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: No description provided.

### `GeometryModeler.coordinate_systems`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Coordinate systems.

### `GeometryModeler.user_lists`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: User lists.

### `GeometryModeler.planes`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Planes.

### `GeometryModeler.oeditor`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: AEDT ``oEditor`` module.

### `GeometryModeler.model_units`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Model units as a string. For example, ``"mm"``.

### `GeometryModeler.model_units`
- **参数**: `units`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: No description provided.

### `GeometryModeler.selections`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Selections.

### `GeometryModeler.obounding_box`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Bounding box.

### `GeometryModeler.dimension`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Dimensions.

### `GeometryModeler.geometry_mode`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Geometry mode.

### `GeometryModeler.solid_bodies`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: List of object names.

### `GeometryModeler.solid_objects`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: List of all solid objects.

### `GeometryModeler.sheet_objects`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: List of all sheet objects.

### `GeometryModeler.line_objects`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: List of all line objects.

### `GeometryModeler.point_objects`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: List of points objects.

### `GeometryModeler.unclassified_objects`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: List of all unclassified objects.

### `GeometryModeler.object_list`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: List of all objects.

### `GeometryModeler.solid_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: List of the names of all solid objects.

### `GeometryModeler.sheet_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: List of the names of all sheet objects.

### `GeometryModeler.line_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: List of the names of all line objects.

### `GeometryModeler.unclassified_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: List of the names of all unclassified objects.

### `GeometryModeler.object_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: List of the names of all objects.

### `GeometryModeler.point_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: List of the names of all points.

### `GeometryModeler.user_defined_component_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: List of the names of all 3D component objects.

### `GeometryModeler.layout_component_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: List of the names of all Layout component objects.

### `GeometryModeler.logger`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Logger.

### `GeometryModeler.version`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Version.

### `GeometryModeler.model_objects`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: List of the names of all model objects.

### `GeometryModeler.non_model_objects`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: List of objects of all non-model objects.

### `GeometryModeler.objects_by_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Object dictionary organized by name.

### `GeometryModeler.refresh`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Refresh this object.

### `GeometryModeler.cleanup_objects`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Clean up objects that no longer exist in the modeler because they were removed by previous operations.

### `GeometryModeler.cleanup_solids`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Clean up solids that no longer exist in the modeler because

### `GeometryModeler.cleanup_points`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Clean up points that no longer exist in the modeler because they were removed by previous operations.

### `GeometryModeler.find_new_objects`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Find any new objects in the modeler that were created by previous operations.

### `GeometryModeler.add_new_objects`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Add objects that have been created in the modeler by previous operations.

### `GeometryModeler.add_new_solids`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Add objects that have been created in the modeler by previous operations.

### `GeometryModeler.add_new_points`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Add objects that have been created in the modeler by previous operations.

### `GeometryModeler.add_new_user_defined_component`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Add 3D components and user-defined models that have been created in the modeler by

### `GeometryModeler.refresh_all_ids`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Refresh all IDs.

### `GeometryModeler.fit_all`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Fit all.

### `GeometryModeler.cover_lines`
- **参数**: `assignment`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Cover closed lines and transform them to a sheet.

### `GeometryModeler.cover_faces`
- **参数**: `assignment`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Cover a face.

### `GeometryModeler.uncover_faces`
- **参数**: `assignment`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Uncover faces.

### `GeometryModeler.create_coordinate_system`
- **参数**: `origin, reference_cs, name, mode, view, x_pointing, y_pointing, psi, theta, phi, u`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Create a coordinate system.

### `GeometryModeler.create_face_coordinate_system`
- **参数**: `face, origin, axis_position, axis, name, offset, rotation, always_move_to_end`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Create a face coordinate system.

### `GeometryModeler.create_object_coordinate_system`
- **参数**: `assignment, origin, x_axis, y_axis, move_to_end, reverse_x_axis, reverse_y_axis, name`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Create an object coordinate system.

### `GeometryModeler.global_to_cs`
- **参数**: `point, coordinate_system`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Transform a point from the global coordinate system to another coordinate system.

### `GeometryModeler.set_working_coordinate_system`
- **参数**: `name`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Set the working coordinate system to another coordinate system.

### `GeometryModeler.invert_cs`
- **参数**: `coordinate_system, to_global`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Get the inverse translation and the conjugate quaternion of the input coordinate system.

### `GeometryModeler.reference_cs_to_global`
- **参数**: `coordinate_system`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Get the origin and quaternion defining the coordinate system in the global coordinates.

### `GeometryModeler.duplicate_coordinate_system_to_global`
- **参数**: `coordinate_system`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Create a duplicate coordinate system referenced to the global coordinate system.

### `GeometryModeler.set_objects_deformation`
- **参数**: `assignment`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Assign deformation objects to a Workbench link.

### `GeometryModeler.set_objects_temperature`
- **参数**: `assignment, ambient_temperature, create_project_var`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Assign temperatures to objects.

### `GeometryModeler.find_point_around`
- **参数**: `assignment, origin, offset, plane`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Find the point around an object.

### `GeometryModeler.create_sheet_to_ground`
- **参数**: `assignment, ground_name, orientation, sheet_dim`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Create a sheet between an object and a ground plane.

### `GeometryModeler.set_object_model_state`
- **参数**: `assignment, model`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Set a list of objects to either models or non-models.

### `GeometryModeler.convert_to_selections`
- **参数**: `assignment, return_list`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Convert modeler objects.

### `GeometryModeler.split`
- **参数**: `assignment, plane, sides, tool, split_crossing_objs, delete_invalid_objs`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Split a list of objects.

### `GeometryModeler.duplicate_and_mirror`
- **参数**: `assignment, origin, vector, is_3d_comp, duplicate_assignment`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Duplicate and mirror a selection.

### `GeometryModeler.mirror`
- **参数**: `assignment, origin, vector, duplicate, is_3d_comp, duplicate_assignment`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Mirror a selection.

### `GeometryModeler.duplicate_around_axis`
- **参数**: `assignment, axis, angle, clones, create_new_objects, is_3d_comp, duplicate_assignment`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Duplicate a selection around an axis.

### `GeometryModeler.duplicate_along_line`
- **参数**: `assignment, vector, clones, attach, is_3d_comp, duplicate_assignment`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Duplicate a selection along a line.

### `GeometryModeler.thicken_sheet`
- **参数**: `assignment, thickness, both_sides`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Thicken the sheet of the selection.

### `GeometryModeler.section`
- **参数**: `assignment, plane, create_new, section_cross_object`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Section the selection.

### `GeometryModeler.separate_bodies`
- **参数**: `assignment, create_group`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Separate bodies of the selection.

### `GeometryModeler.imprint`
- **参数**: `blank_list, tool_list, keep_originals`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Imprint an object list on another object list.

### `GeometryModeler.purge_history`
- **参数**: `assignment, non_model`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Purge history objects from object names.

### `GeometryModeler.clone`
- **参数**: `assignment`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Clone objects from a list of object IDs.

### `GeometryModeler.copy`
- **参数**: `assignment`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Copy objects to the clipboard.

### `GeometryModeler.paste`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Paste objects from the clipboard.

### `GeometryModeler.intersect`
- **参数**: `assignment, keep_originals`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Intersect objects from a list.

### `GeometryModeler.detach_faces`
- **参数**: `assignment, faces`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Section the object.

### `GeometryModeler.connect`
- **参数**: `assignment`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Connect objects from a list.

### `GeometryModeler.check_plane`
- **参数**: `assignment, face_location, offset`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Check for the plane that is defined as the face for an object.

### `GeometryModeler.clean_objects_name`
- **参数**: `main_part_name`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Clean the names of the objects for a main part.

### `GeometryModeler.create_airbox`
- **参数**: `offset, offset_type, name`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Create an airbox that is as big as the bounding extension of the project.

### `GeometryModeler.create_air_region`
- **参数**: `x_pos, y_pos, z_pos, x_neg, y_neg, z_neg, is_percentage`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Create an air region.

### `GeometryModeler.edit_region_dimensions`
- **参数**: `values`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Modify the dimensions of the region.

### `GeometryModeler.create_face_list`
- **参数**: `assignment, name`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Create a list of faces given a list of face ID or a list of objects.

### `GeometryModeler.create_object_list`
- **参数**: `assignment, name`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Create an object list given a list of object names.

### `GeometryModeler.generate_object_history`
- **参数**: `assignment, non_model`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Generate history for the object.

### `GeometryModeler.create_faceted_bondwire_from_true_surface`
- **参数**: `assignment, direction, min_size, number_of_segments`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Create a faceted bondwire from an existing true surface bondwire.

### `GeometryModeler.create_outer_facelist`
- **参数**: `assignment, name`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Create a face list from a list of outer objects.

### `GeometryModeler.vertex_data_of_lines`
- **参数**: `text_filter`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Generate a dictionary of line vertex data for all lines contained within the design.

### `GeometryModeler.break_spaceclaim_connection`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Disconnect from the running SpaceClaim instance.

### `GeometryModeler.scale`
- **参数**: `assignment, x, y, z`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Scale a list of objects.

### `GeometryModeler.select_allfaces_fromobjects`
- **参数**: `assignment`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Select all outer faces given a list of objects.

### `GeometryModeler.setunassigned_mats`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Find unassagned objects and set them to non-model.

### `GeometryModeler.automatic_thicken_sheets`
- **参数**: `assignment, value, extrude_internally, internal_extrusion`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Create thickened sheets for a list of input faces.

### `GeometryModeler.create_group`
- **参数**: `objects, components, groups, group_name`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Group objects or groups into one group.

### `GeometryModeler.ungroup`
- **参数**: `groups`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Ungroup one or more groups.

### `GeometryModeler.flatten_assembly`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Flatten the assembly, removing all group trees.

### `GeometryModeler.wrap_sheet`
- **参数**: `sheet, object, imprinted`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Execute the sheet wrapping around an object.

### `GeometryModeler.heal_objects`
- **参数**: `assignment, auto_heal, tolerant_stitch, simplify_geometry, tighten_gaps, heal_to_solid, stop_after_first_stitch_error, max_stitch_tolerance, explode_and_stitch, geometry_simplification_tolerance, maximum_generated_radius, simplify_type, tighten_gaps_width, remove_silver_faces, remove_small_edges, remove_small_faces, silver_face_tolerance, small_edge_tolerance, small_face_area_tolerance, bounding_box_scale_factor, remove_holes, remove_chamfers, remove_blends, hole_radius_tolerance, chamfer_width_tolerance, blend_radius_tolerance, allowable_surface_area_change, allowable_volume_change`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Repair invalid geometry entities for the selected objects within the specified tolerance settings.

### `GeometryModeler.simplify_objects`
- **参数**: `assignment, simplify_type, extrusion_axis, clean_up, allow_splitting, separate_bodies, clone_body, generate_primitive_history, interior_points_on_arc, length_threshold_percentage, create_group_for_new_objects`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Simplify command to converts complex objects into simpler primitives which are easy to mesh and solve.

### `GeometryModeler.create_point`
- **参数**: `position, name, color`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Create a point.

### `GeometryModeler.create_plane`
- **参数**: `name, plane_base_x, plane_base_y, plane_base_z, plane_normal_x, plane_normal_y, plane_normal_z, color`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Create a plane.

### `GeometryModeler.update_object`
- **参数**: `assignment`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Update any :class:`ansys.aedt.core.modeler.cad.object_3d.Object3d` derivatives

### `GeometryModeler.update_geometry_property`
- **参数**: `assignment, name, value`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Update property of assigned geometry objects.

### `GeometryModeler.value_in_object_units`
- **参数**: `value`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Convert one or more strings for numerical lengths to floating point values.

### `GeometryModeler.does_object_exists`
- **参数**: `assignment`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Check to see if an object exists.

### `GeometryModeler.create_subregion`
- **参数**: `padding_values, padding_types, assignment, name`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Create a subregion.

### `GeometryModeler.reassign_subregion`
- **参数**: `region, parts`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Modify parts in the subregion.

### `GeometryModeler.create_region`
- **参数**: `pad_value, pad_type, name`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Create an air region.

### `GeometryModeler.create_object_from_edge`
- **参数**: `assignment, non_model`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Create an object from one or multiple edges.

### `GeometryModeler.create_object_from_face`
- **参数**: `assignment, non_model`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Create an object from one or multiple face.

### `GeometryModeler.polyline_segment`
- **参数**: `type, num_seg, num_points, arc_angle, arc_center, arc_plane`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: New segment of a polyline.

### `GeometryModeler.create_polyline`
- **参数**: `points, segment_type, cover_surface, close_surface, name, material, xsection_type, xsection_orient, xsection_width, xsection_topwidth, xsection_height, xsection_num_seg, xsection_bend_type, non_model`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Draw a polyline object in the 3D modeler.

### `GeometryModeler.create_spiral_on_face`
- **参数**: `assignment, width, filling_factor`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Create a Spiral Polyline inside a face.

### `GeometryModeler.create_udp`
- **参数**: `dll, parameters, library, name`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Create a user-defined primitive (UDP).

### `GeometryModeler.update_udp`
- **参数**: `assignment, operation, parameters`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Update an existing geometrical object that was originally created using a user-defined primitive (UDP).

### `GeometryModeler.delete`
- **参数**: `assignment`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Delete objects or groups.

### `GeometryModeler.delete_objects_containing`
- **参数**: `contained_string, case_sensitive`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Delete all objects with a given prefix.

### `GeometryModeler.delete_all_points`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Delete all points.

### `GeometryModeler.convert_segments_to_line`
- **参数**: `assignment`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Convert a CreatePolyline list of segments to lines.

### `PrimitivesBuilder.logger`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Logger.

### `PrimitivesBuilder.create`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Create instances of defined primitives.

### `PrimitivesBuilder.convert_units`
- **参数**: `values`
- **模块**: `ansys.aedt.core.modeler.cad.primitives`
- **描述**: Convert input values to default units.

### `ComponentArray.create`
- **参数**: `cls, app, input_data, name`
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: Create a component array.

### `ComponentArray.component_names`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: List of component names.

### `ComponentArray.cells`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: List of :class:`ansys.aedt.core.modeler.cad.component_array.CellArray` objects.

### `ComponentArray.name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: Name of the array.

### `ComponentArray.name`
- **参数**: `array_name`
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: No description provided.

### `ComponentArray.properties`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: Ordered dictionary of the properties of the component array.

### `ComponentArray.post_processing_cells`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: Dictionary of each component's postprocessing cells.

### `ComponentArray.post_processing_cells`
- **参数**: `val`
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: No description provided.

### `ComponentArray.visible`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: Flag indicating if the array is visible.

### `ComponentArray.visible`
- **参数**: `val`
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: No description provided.

### `ComponentArray.show_cell_number`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: Flag indicating if the array cell number is shown.

### `ComponentArray.show_cell_number`
- **参数**: `val`
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: No description provided.

### `ComponentArray.render_choices`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: List of rendered name choices.

### `ComponentArray.render`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: Array rendering.

### `ComponentArray.render`
- **参数**: `val`
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: No description provided.

### `ComponentArray.render_id`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: Array rendering ID.

### `ComponentArray.a_vector_choices`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: List of name choices for vector A.

### `ComponentArray.b_vector_choices`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: List of name choices for vector B.

### `ComponentArray.a_vector_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: Name of vector A.

### `ComponentArray.a_vector_name`
- **参数**: `val`
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: No description provided.

### `ComponentArray.b_vector_name`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: Name of vector B.

### `ComponentArray.b_vector_name`
- **参数**: `val`
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: No description provided.

### `ComponentArray.a_size`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: Number of cells in the vector A direction.

### `ComponentArray.a_size`
- **参数**: `val`
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: No description provided.

### `ComponentArray.b_size`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: Number of cells in the vector B direction.

### `ComponentArray.b_size`
- **参数**: `val`
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: No description provided.

### `ComponentArray.a_length`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: Length of the array in A direction.

### `ComponentArray.b_length`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: Length of the array in B direction.

### `ComponentArray.padding_cells`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: Number of padding cells.

### `ComponentArray.padding_cells`
- **参数**: `val`
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: No description provided.

### `ComponentArray.coordinate_system`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: Coordinate system name.

### `ComponentArray.coordinate_system`
- **参数**: `name`
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: No description provided.

### `ComponentArray.update_properties`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: Update component array properties.

### `ComponentArray.delete`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: Delete the component array.

### `ComponentArray.lattice_vector`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: Get model lattice vector.

### `CellArray.rotation`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: Rotation value of the cell object.

### `CellArray.rotation`
- **参数**: `val`
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: No description provided.

### `CellArray.component`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: Component name of the cell object.

### `CellArray.component`
- **参数**: `val`
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: No description provided.

### `CellArray.is_active`
- **参数**: ``
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: Flag indicating if the cell object is active or passive.

### `CellArray.is_active`
- **参数**: `val`
- **模块**: `ansys.aedt.core.modeler.cad.component_array`
- **描述**: No description provided.

