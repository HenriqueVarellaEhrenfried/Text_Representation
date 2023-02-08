import os
from datetime import datetime

DATASET_ORIGIN = [
    "../Datasets/MR/ParsedV2/"
]

DATASET_OUTPUT_DEFAULT = "../Datasets/MR/TextGCN_Setup/"

REPRESENTATION = {
    "ROO": "only_order",
    "ROC": "order_circular",
    "BT": "binary_tree",
    "AT": "avl_tree",
    "RBT": "red_black_tree",
    "DTOY": "tree_only",
    "DTOR": "tree_and_order",
    "DTORM": "tree_and_order_multi_graph",
    "DTOYS": "tree_and_self",
    "DTORS": "tree_order_and_self",
    "DTORMS": "tree_order_multigraph_and_self",
    "GOW": "gow"
}

BASE_NAME = "MR_TextGCN_Setup"
BASE_COMMAND = "python main.py -i"

init_time = datetime.now()

for repr in REPRESENTATION.keys():
    for dat_origin in DATASET_ORIGIN:
        command = BASE_COMMAND
        task = dat_origin.split("/")[-2]
        mode = REPRESENTATION[repr]
        print(">> [%s] Creating Dataset [%s-%s : %s]" %  (str(datetime.now()), BASE_NAME, task, mode))

        # Create directory if not exists
        os.system("mkdir -p %s%s-%s-%s-TAG-None" % (DATASET_OUTPUT_DEFAULT, BASE_NAME, task, repr) )

        # Build the command to create the dataset
        command += " %s -o %s%s-%s-%s-TAG-None -n %s-%s -s Train -d 300 -c 8 -l en -I True -g %s -t none;" % (dat_origin, DATASET_OUTPUT_DEFAULT, BASE_NAME, task, repr, BASE_NAME, task, mode)
        
        # Execute this command
        os.system(command)
        print(">> [%s] Dataset [%s-%s : %s] Created" %  (str(datetime.now()), BASE_NAME, task, mode))

print(">> [%s] Finished building all %s datasets after time %s " %  (str(datetime.now()), BASE_NAME, str(datetime.now()-init_time)))
# print(">> Renaming Them")
# os.system("bash Rename_GermEval2018.sh")


#---------------------------------------------------------#

# ROO	    Read Order Only
# ROC	    Reading Order Circular
# BT	    Binary Tree
# AT	    AVL Tree
# RBT	    Red-Black Tree
# DTOY	    Dependency Tree Only
# DTOR	    Dependency Tree Order
# DTORM	    Dependency Tree Order Multigraph
# DTOYS	    Dependnecy Tree Only Self
# DTORS	    Dependency Tree Order Self
# DTORMS	Dependency Tree Order Multigraph Self
# GOW	    Graph Of Words

#---------------------------------------------------------#