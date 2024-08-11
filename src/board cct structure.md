        board = {
            "node_id": self.node_id,
            "board_parent_node_id": parent_id,
            "name": f"DB L: {level}: {self.node_id}",
            "board_section" : str_board_section,
            "board_floor" : str_board_floor,
            "board_location": str_board_location,
            "phase": str_board_phase,
            "circuits": []
        }

###########

"tbl_board": [{
                    "board_id": m_board_id_guid ,
                    "copied_from_board_id": "",
                    "board_reference": m_board_reference,
                    "board_reference_type": "DB",
                    "board_nominal_voltage": map_board_nominal_voltage(index, df_data),
                    "board_phase": s_board_phase,
                    "board_circuit_phase_naming":  s_board_circuit_phase_naming,
                    "Is_Mains_Distribution": "",
                    "board_manufacturer": map_board_manufacturer(index, df_data),
                    "board_function": map_board_function(index,df_data),
                    "board_ways": 0,
                    "board_type":  " ",
                    "board_rating": " ",
                    "board_asset_number": map_board_asset_number(index, df_data),
                    "board_earth_loop": "",
                    "board_PSSC": "",   
                    "board_OPT": map_board_OPT(index,df_data),
                    "board_OPT_type":  map_board_OPT_type(index,df_data),
                    
                    "board_location_block": "",
                    "board_location_floor": map_board_location_floor(index, df_data), 
                    "board_location": map_board_location(index,df_data),
                    "board_picture_id": "",

                    "board_supply_source_reference_id": "",
                    ## board supply reference should have a single circuit_id 
                    ## for 1 phase and multi cct_id for multiple phases, ie. 
                    ## [1234, 5678, 91011], wjere each calue is a circuit id relating to the 3 phase circuit
                    "board_supply_source_circuit_reference_id" : "",

                    # if we have the cct id's the values below are not required
                    # the values below are required only if manually entered and there is no supply_circuit_id
                    "board_supply_source_reference": map_board_supply_source_reference(index, df_data),
                    "board_supply_source_reference_type": "-",
                    "board_supply_conductor_size":  map_board_supply_conductor_size(index, df_data),
                    "board_supply_circuit_reference": "",
                    "board_supply_circuit_phase": "",
                    "board_supply_circuit_conductor_size_type": s_supply_conductor_size_type,
                    "board_supply_circuit_conductor_size_type_other": s_supply_conductorsize_type_other,
                    "board_supply_conductor_rating": "",
                    
                    "board_rcd": map_board_rcd(index,df_data),
                    "board_rcd_poles": "n/a",
                    "board_rcd_rating": map_board_rcd_rating(index,df_data),
                    "current_mod_number": 0,
                    "issue_number": 0,
                    "date_last_amended": "",
                    "spreadsheet_filename": "",
                    "DateObsolete": "0000-00-00 00:00:00",
                    "board_comments": map_board_comments(index, df_data),
                    "building_id": C_BUILDING_ID,
                    "amend_status": "",
                    "board_last_thermo_date": "",
                    "board_next_thermo_date": "",

                    "qrcode_id": "",
                    "qrcode_id_assigned_date": "",
                    "spd_bs_en": "",
                    "spd_bs_en_type": "",
                    "spd_type_t1": "",
                    "spd_type_t2": "",
                    "spd_type_t3": "",
                    "spd_type_na": "",
                    "return_original": 1,
                    "qrcode_id_encoded": "",
                    "is_migrated": 0
                    }]
                }

###########
        single_cctdict = {
                        "circuit_id": str(uuid.uuid4()).lower(),
                        "board_id": m_board_id_guid,
                        "record_type": "C",
                        "circuit_date_from": "0000-00-00 00:00:00",
                        "circuit_date_to": "0000-00-00 00:00:00",
                        "circuit_reference": map_circuit_reference(current_index, df_data),
                        "circuit_phase": map_circuit_phase(current_index, df_data),
                        "circuit_equipment_connected": map_circuit_equipment_connected(current_index, df_data),
                        "circuit_is_sub_main": "N",
                        "circuit_is_3phase": m_circuit_is_3phase(current_index, df_data),
                        "circuit_conductor_size_type": s_cable_type,
                        "circuit_cable_other_text": s_cable_type_other,
                        "circuit_cable_reference": "",
                        "circuit_reference_method": s_circuit_reference_method,
                        "circuit_reference_method_id": "",
                        "circuit_number_of_points": "",
                        "circuit_conductor_csa_live": map_circuit_conductor_csa_live(current_index, df_data),
                        "circuit_conductor_csa_cpc": map_circuit_conductor_csa_cpc(current_index, df_data),
                        "circuit_load": 0,
                        "cert_location_temperature": "",
                        "cert_load_temperature_note": "",
                        "circuit_load_test_date": "",
                        "circuit_last_test_date": s_circuit_last_test_date,
                        "circuit_next_test_date": s_circuit_next_test_date,
                        "circuit_planned_test_date": s_circuit_next_test_date,
                        "circuit_scheduled_test_date": "",
                        "circuit_max_permitted_disconnection_time": s_cct_max_permitted_disconnection_time,
                        "circuit_OCPD": s_circuit_OCPD,
                        "circuit_OCPD_Type": s_circuit_OCPD_Type,
                        "circuit_OCPD_rating": s_circuit_OCPD_Rating,
                        "circuit_OCPD_scc": s_circuit_OCPD_scc,
                        "circuit_rcd_op_current": s_rcd_op_current,
                        "circuit_rcd_type": "",
                        "circuit_rcd_rating": s_circuit_rcd_rating,
                        "circuit_max_permitted_impedance": s_circuit_max_permitted_impedance,
                        "circuit_rcd_bsen": s_circuit_rcd_bsen,
                        "circuit_rcd_poles": 0,
                        "linked_circuit_id": "",
                        "date_last_amended": "2024-05-03 10:54:10",
                        "edited_in_cert": 0
                        }   