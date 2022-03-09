import os

UGFORMER_DATASET = '../../Graph-Transformer/dataset/'

OUTPUT = [
    '../Datasets/B2W/B2W_COMPLETE-Rating-Only_Order-TAG-None', 
    '../Datasets/B2W/B2W_COMPLETE-Rating-Order_Circular-TAG-None', 
    '../Datasets/B2W/B2W_COMPLETE-Rating-Binary_Tree-TAG-None', 
    '../Datasets/MR/MR-Only_Order-TAG-None', 
    '../Datasets/MR/MR-Order_Circular-TAG-None', 
    '../Datasets/MR/MR-Binary_Tree-TAG-None'
]
GRAPH_MODE = ['only_order', 'order_circular','binary_tree']
TAG_MODE = ['none']

HELPER = {
    'B2W_COMPLETE-Rating-Only_Order-TAG-None': 'only_order',
    'B2W_COMPLETE-Rating-Order_Circular-TAG-None': 'order_circular',
    'B2W_COMPLETE-Rating-Binary_Tree-TAG-None': 'binary_tree',
    'MR-Only_Order-TAG-None': 'only_order',
    'MR-Order_Circular-TAG-None': 'order_circular',
    'MR-Binary_Tree-TAG-None': 'binary_tree'
}
HELPER2 = {
    'None': 'none',
    'DEP': 'dep',
    'POS': 'pos',
    'DEP-POS': 'dep-pos',
    'POS-DEP':'pos-dep',
    'SQRT-PROD': 'sqrt_product',
    'Distance': 'distance'
}
LANGUAGE = {
    'B2W_COMPLETE-Rating-Only_Order-TAG-None': 'pt',
    'B2W_COMPLETE-Rating-Order_Circular-TAG-None': 'pt',
    'B2W_COMPLETE-Rating-Binary_Tree-TAG-None': 'pt',
    'MR-Only_Order-TAG-None': 'en',
    'MR-Order_Circular-TAG-None': 'en',
    'MR-rder_Rearranged-TAG-None': 'en',
    'MR-Binary_Tree-TAG-None': 'en'
}
INPUT = {
    'B2W_COMPLETE-Rating-Only_Order-TAG-None': '../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/',
    'B2W_COMPLETE-Rating-Order_Circular-TAG-None': '../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/',
    'B2W_COMPLETE-Rating-Binary_Tree-TAG-None': '../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/',
    'MR-Only_Order-TAG-None': '../Datasets/MR/Parsed/',
    'MR-Order_Circular-TAG-None': '../Datasets/MR/Parsed/',
    'MR-Binary_Tree-TAG-None': '../Datasets/MR/Parsed/'
}
DATASET = {
    'B2W_COMPLETE-Rating-Only_Order-TAG-None': 'B2W-Rating',
    'B2W_COMPLETE-Rating-Order_Circular-TAG-None': 'B2W-Rating',
    'B2W_COMPLETE-Rating-Binary_Tree-TAG-None': 'B2W-Rating',
    'MR-Only_Order-TAG-None': 'MR',
    'MR-Order_Circular-TAG-None': 'MR',
    'MR-Binary_Tree-TAG-None': 'MR'
}
DATASET_UGFORMER = {
    'B2W_COMPLETE-Rating-Only_Order-TAG-None': 'Train_B2W-Rating.txt',
    'B2W_COMPLETE-Rating-Order_Circular-TAG-None': 'Train_B2W-Rating.txt',
    'B2W_COMPLETE-Rating-Binary_Tree-TAG-None': 'Train_B2W-Rating.txt',
    'MR-Only_Order-TAG-None': 'Train_MR.txt',
    'MR-Order_Circular-TAG-None': 'Train_MR.txt',
    'MR-Binary_Tree-TAG-None': 'Train_MR.txt'
}


for out in OUTPUT:
    print("mkdir -p %s" %(out))

print("\n")


for out in OUTPUT:
    graph_mode = out.split("/")[-1]
    tag = out.split("/")[-1].split("TAG-")[-1]
    print("echo \">>> Building %s\"" % (graph_mode))
    print("python main.py -i %s -o %s -n %s -s Train -d 300 -c 20 -l %s -g %s -t %s;" % (INPUT[graph_mode], out, DATASET[graph_mode] , LANGUAGE[graph_mode], HELPER[graph_mode], HELPER2[tag]))
    print("")

print ("\n\n\n\n# ------------\n\n\n")

for out in OUTPUT:
    graph_mode = out.split("/")[-1]
    tag = out.split("/")[-1].split("TAG-")[-1]
    original = out + "/" + DATASET_UGFORMER[graph_mode]
    new = out + "/" + graph_mode + ".txt"

    print("echo \">>> Renaming %s\"" % (graph_mode))
    print ('mv %s %s' % (original, new) )
    print("echo \">>> Coping dataset %s\"" % (graph_mode))
    print ('cp -r %s %s' % (out, UGFORMER_DATASET) )
    print("")

