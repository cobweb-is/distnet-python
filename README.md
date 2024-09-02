This python script generates a json file that contains the nodes and connections for a DAG.  The purpose is to generate test data for the electrical distribution network rendering application.
The size of the network can be changed by changing the following constants:
C_NUM_LEVELS = 3 #get_random_int(1, 5)
C_NUM_OF_WAYS = 2 #get_random_int(1, 6)
C_NUM_OF_CCT_BRANCHES = 0 # get_random_int(0, 2)

The folder path for the json file will need to be changed to your folder name by changing:
folder_path = r'C:\mytargetfolder'
The json file netwrok_data.json will be posted to C:\mytargetfolder 
The json file contains the network data for generating the distribution network.
