import os
from datetime import datetime

DATASET_ORIGIN = [
    "../Datasets/GermEval2021/Parsed/Engaging/",
    "../Datasets/GermEval2021/Parsed/FactClamming/",
    "../Datasets/GermEval2021/Parsed/Toxic/"
]

DATASET_OUTPUT_DEFAULT = "../Datasets/GermEval2021/"

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

BASE_NAME = "GermEval2021"
BASE_COMMAND = "python main.py "

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
        command += "-i %s -o %s%s-%s-%s-TAG-None -n %s-%s -s Train -d 300 -c 20 -l de -I True -g %s -t none;" % (dat_origin, DATASET_OUTPUT_DEFAULT, BASE_NAME, task, repr, BASE_NAME, task, mode)
        
        # Execute this command
        os.system(command)
        print(">> [%s] Dataset [%s-%s : %s] Created" %  (str(datetime.now()), BASE_NAME, task, mode))

print(">> [%s] Finished building all %s datasets" %  (str(datetime.now()), BASE_NAME))
print(">> Renaming Them")
os.system("bash Rename_GermEval2021.sh")

print(">> [%s] Finished building all %s datasets after time %s " %  (str(datetime.now()), BASE_NAME, str(datetime.now()-init_time)))

# mkdir -p ../Datasets/MR/MR-GOW-TAG-None
# mkdir -p ../Datasets/Ohsumed/Ohsumed-GOW-TAG-None

# mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-GOW-TAG-None
# mkdir -p ../Datasets/10kGNAD-DE/10kGNAD-GOW-TAG-None
# python main.py -i ../Datasets/GermEval2018/Parsed_ALL/Fine/ -o ../Datasets/GermEval2018/GermEval2018-Fine-DTORMS-TAG-None -n GermEval2018-Fine -s Train -d 300 -c 20 -l de -g tree_order_multigraph_and_self -t none;


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