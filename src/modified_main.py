
import json
import random
import os
import uuid

class ElectricalNetworkGenerator:
    def __init__(self, num_roots, num_levels, num_children_per_node):
        self.num_roots = num_roots
        self.num_levels = num_levels
        self.num_children_per_node = num_children_per_node
        self.node_id = 1
        self.boards = []

    def generate_board(self, level, position, parent_phase, parent_id=None, parent_circuit_id=None, branch_id=None):
        if level <= 1:
            # Force level 1 and 2 to be 3-phase
            str_board_phase = "Three-phase"
        else:
            if parent_phase == "Single-phase":
                str_board_phase = "Single-phase"
            else: 
                str_board_phase = "Three-phase"

        str_board_section = random.choice(["NORTH", "SOUTH", "EAST", "WEST", "EXTERNAL", ""])
        str_board_floor = random.choice(["LG", "G", "1ST", "2ND", "3RD", ""])
        str_board_location = f"{str_board_section} {str_board_floor}".strip()

        board = {
            "id": str(self.node_id),
            "parent_id": parent_id,
            "parent_circuit_id": parent_circuit_id,
            "branch_id": branch_id,
            "phase": str_board_phase,
            "location": str_board_location,
            "children": []
        }

        self.boards.append(board)
        current_board_id = str(self.node_id)
        self.node_id += 1

        if level < self.num_levels:
            # Generate branches
            for i in range(self.num_children_per_node):
                branch_id = f"{parent_circuit_id}-{i + 1}" if parent_circuit_id else f"{self.node_id}-{i + 1}"
                self.generate_board(
                    level + 1,
                    i,
                    str_board_phase,
                    parent_id=current_board_id,
                    parent_circuit_id=branch_id,
                    branch_id=branch_id
                )
                
    def generate(self):
        for i in range(self.num_roots):
            root_circuit_id = str(uuid.uuid4())
            self.generate_board(1, i, "Three-phase", parent_circuit_id=root_circuit_id)
        return self.boards

if __name__ == "__main__":
    generator = ElectricalNetworkGenerator(num_roots=2, num_levels=3, num_children_per_node=2)
    network = generator.generate()
    output_path = "electrical_network.json"
    with open(output_path, "w") as outfile:
        json.dump(network, outfile, indent=4)
    print(f"Electrical network saved to {output_path}")
