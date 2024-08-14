import json
import random
import os
import uuid
#1
#2

class ElectricalNetworkGenerator:
    def __init__(self, num_roots, num_levels, num_children_per_node):
        self.num_roots = num_roots
        self.num_levels = num_levels
        self.num_children_per_node = num_children_per_node
        self.node_id = 1
        self.boards = []

    def generate_board(self, level, position, parent_phase, parent_id=None, parent_circuit_id=None, is_q_cct_branch=None):
        str_print = (f"NEW parent id: {parent_id}")
        print(Indent(str_print, 5*level))

        if level <=1:
            # force level 1 and 2 to be 3 phase
            str_board_phase = "Three-phase"
        else:
            if parent_phase == "Single-phase":
                str_board_phase = "Single-phase"
            else: 
                #str_board_phase = random.choice(["Single-phase", "Three-phase"])
                str_board_phase = "Three-phase"

        str_board_section = random.choice(["NORTH", "SOUTH","EAST","WEST","EXTERNAL",""])
        str_board_floor =  random.choice(["LG", "G","1ST","2ND","3RD",""])
        str_board_location = str_board_section + "/" + str_board_floor+"/"+random.choice(["RS RM1", "RIS RM2","RIS RM3","RIS RM4",""])        
    
        board = {
            "board_id": self.node_id,
            "board_supply_source_reference_id": parent_id,
            "board_supply_source_circuit_reference_id" : parent_circuit_id,
            "board_reference": f"DB L: {level}: {self.node_id}{is_q_cct_branch}",
            "board_reference_type": "DB",
            "board_nominal_voltage": "",
            "board_phase": str_board_phase,
            "board_circuit_phase_naming":  "",
            "Is_Mains_Distribution": "",
            "board_manufacturer": "",
            "board_function": "",
            "board_ways": 0,
            "board_type":  " ",
            "board_rating": " ",
            "board_asset_number": "",
            "board_earth_loop": "",
            "board_PSSC": "",   
            "board_OPT": "",
            "board_OPT_type":  "",
            "board_location_block": "",
            "board_location_floor": "", 
            "board_location": "",
            "board_picture_id": "",
            "board_location_block" : str_board_section,
            "board_location_floor" : str_board_floor,
            "board_location": str_board_location,
            "board_phase": str_board_phase,
            "board_rcd": "",
            "board_rcd_poles": "n/a",
            "board_rcd_rating": "",
            "current_mod_number": 0,
            "issue_number": 0,
            "date_last_amended": "",
            "spreadsheet_filename": "",
            "DateObsolete": "0000-00-00 00:00:00",
            "board_comments": "",
            "building_id": "BUILDING_id",
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
            "is_migrated": 0,
            "tbl_circuits": []
        }
        
        current_id = self.node_id
        current_circuit_id = ""
        self.node_id += 1

        if level == self.num_levels:
            str_print = (f"db node: {self.node_id}, (i{level}) fed from cct {position}, board phase-{str_board_phase} - FINAL")
        else:
            str_print = (f"Dist Board(node: {self.node_id}, L:{level}) fed from cct {position}, board phase-{str_board_phase}")
        print(Indent((f"Level: {level}<-"), 5*level))
        print(Indent(str_print, 5*level))

        if level < self.num_levels:
            #number of ccts in a board
            num_of_ccts = 1
            print(Indent((f"num of ccts: {num_of_ccts}"), 5*level))
            # num_children is the number of child nodes for this node
            # num_children = random.randint(1, self.num_children_per_node)
            num_children = 1
            print(Indent((f"num of children: {num_children}"), 5*level))
            for cct_index in range(num_of_ccts):
                print(Indent((f"cct_index: {cct_index})"), 5*level))

                if str_board_phase == "Three-phase":
                    circuit_is_3phase = random.choice(["RING", "RAD", "TP"])
                    if circuit_is_3phase == "TP":
                        lst_cct_phases = ["TP"]
                    else:
                        lst_cct_phases = ["L1", "L2", "L3"]
                    
                else:
                    lst_cct_phases = ["S"]
                    circuit_is_3phase = random.choice(["RING", "RAD"])

                current_circuit_id= str(uuid.uuid4()).lower()
                for str_cct_phase in lst_cct_phases:
                    circuit = {
                        "circuit_id": current_circuit_id,
                        "circuit_reference": cct_index,
                        "circuit_number": cct_index+1,
                        "circuit_phase" : str_cct_phase,
                        "circuit_level" : level,
                        "circuit_designation": "Some circuit designation",
                        "circuit_is_3phase": circuit_is_3phase,
                        "child_board_node_id": None
                    }


                    if num_children > 0:  #if this is not the last node, i.e has children
                        #force board phaseto be 3phase if supplied by a 3 phase board
                        #if the cct is a TP then the child board must be TP
                        if circuit_is_3phase == "TP":
                            str_child_board_phase = "Three-phase"
                        else:
                            str_child_board_phase = "Single-phase"
                        print(Indent("|  ", 5*level))
                        print(Indent("_______", 5*level))
                        str_print = (f"node: {self.node_id,}, level:{level}, circuit-{cct_index} phase-{str_cct_phase} circuit type={circuit_is_3phase} not final")
                        print(Indent(str_print, 5*level))

                        if level == 1: # force level 1 to have branches
                            # occasionally a circuit will have branches, e.g tapoffs on a busbar
                            # this means a circuit may fed mutiple boards
                            #num_of_cct_branches = random.randint(0, 2)
                            num_of_cct_branches = 1
                            for branch_index in range(num_of_cct_branches): # for a circuit_ id generate the child boards for each branch 
                                print(Indent("|  ", 9*level))
                                print(Indent("B_______", 9*level))
                                str_print = (f"level:{level}, circuit-{cct_index} branch-{branch_index} phase-{str_cct_phase} circuit type={circuit_is_3phase} not final")
                                print(Indent(str_print, 9*level))
                                child_board = self.generate_board(level + 1, cct_index, str_child_board_phase, current_id, current_circuit_id,"B")
                                print(f"board_id: {board["board_id"]}")
                                print(f"current circuit_id: {current_circuit_id}")
                                print(f"Child board _id: {child_board["board_id"]}")
                                #set the child node for the cct
                                circuit["child_board_node_id"] = child_board["board_id"]
                                #print(circuit)
                                board["tbl_circuits"].append(circuit)
                        else:
                            child_board = self.generate_board(level + 1, cct_index, str_child_board_phase, current_id, current_circuit_id)
                            #set the child node for the cct
                            circuit["child_board_node_id"] = child_board["board_id"]
                            board["tbl_circuits"].append(circuit)

        self.boards.append(board)
        return board

    def generate_network_data(self):
        for root_position in range(self.num_roots):
            self.generate_board(1, str(root_position), "Three-phase")
        return self.boards

def Indent(char, num_indents):
    """
    Function to indent a character by a specified number of spaces.

    :param char: The character to be printed.
    :param num_indents: The number of spaces to indent the character.
    :return: A string with the specified number of spaces followed by the character.
    """
    return " " * num_indents + char

def charprint(char, num_times):
    """
    Function to print a character a specified number of times.
    
    :param char: The character to be printed.
    :param num_times: The number of times to print the character.
    """
    print(char * num_times)

def main():
    # Parameters
    num_roots = 1
    num_levels = 3
    num_children_per_node = 3

    # Generate Electrical Distribution Network data
    generator = ElectricalNetworkGenerator(num_roots, num_levels, num_children_per_node)
    network_data = generator.generate_network_data()

    # Convert to JSON format
    network_json = json.dumps(network_data, indent=4)

    # Print JSON to console (optional)
    # print(network_json)

    ###
    # Specify the folder path
    folder_path = r'C:\Users\micha\Dropbox\distnetwork\distnet-react\src'

    # Ensure the directory exists, if not, create it
    os.makedirs(folder_path, exist_ok=True)

    # Write JSON to a file in the specified folder
    file_path = os.path.join(folder_path, 'network_data.json')
    with open(file_path, 'w') as json_file:
        json.dump(network_data, json_file, indent=4)
    ###


if __name__ == "__main__":
    main()
