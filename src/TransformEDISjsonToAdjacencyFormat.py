import json
# Transforms the output from Main.py, a json format of the edis/boards/details to a adjacency list that is used by some JS examples
# Load the correct JSON data from the uploaded file
network_data_json = r"C:\\Users\\micha\\Dropbox\\distnetwork\\distnet-python\\src\\network_data.json"
with open(network_data_json, 'r') as file:
    data = json.load(file)

# Extract the relevant information to create the adjacency list
adjacency_list = {}

for item in data['tbl_board']:
    board_reference = item.get('board_reference')
    source_id = item.get('board_supply_source_reference_id')
    
    # Find the board_reference for the source_id
    source_reference = None
    for source_item in data['tbl_board']:
        if source_item.get('board_id') == source_id:
            source_reference = source_item.get('board_reference')
            break
    
    if source_reference:
        if source_reference not in adjacency_list:
            adjacency_list[source_reference] = []
        adjacency_list[source_reference].append(board_reference)
        
    if board_reference not in adjacency_list:
        adjacency_list[board_reference] = []

# Define the file path where the adjacency list will be saved
output_file_path = 'adjacency_list_with_references.txt'

# Convert the adjacency list to a string with proper formatting
adjacency_list_str = json.dumps(adjacency_list, indent=4)

# Write the adjacency list to the text file
with open(output_file_path, 'w') as file:
    file.write(adjacency_list_str)

print(f"Adjacency list written to {output_file_path}")
