import os


OUTPUT = ['../Datasets/MR/MR-Default-TAG-DEP', '../Datasets/MR/MR-Default-TAG-POS', '../Datasets/MR/MR-Default-TAG-DEP-POS', '../Datasets/MR/MR-Default-TAG-POS-DEP', '../Datasets/MR/MR-Default-TAG-SQRT-PROD', '../Datasets/MR/MR-Order-TAG-DEP', '../Datasets/MR/MR-Order-TAG-POS', '../Datasets/MR/MR-Order-TAG-DEP-POS', '../Datasets/MR/MR-Order-TAG-POS-DEP', '../Datasets/MR/MR-Order-TAG-SQRT-PROD']
GRAPH_MODE = ['tree_only', 'tree_and_order', 'tree_and_order_multi_graph', 'tree_and_self', 'tree_order_and_self', 'tree_order_multigraph_and_self']
TAG_MODE = ['none', 'dep', 'pos', 'dep-pos', 'pos-dep', 'sqrt_product', 'distance']

HELPER = {
    'MR-Default-TAG-DEP':'tree_only',
    'MR-Default-TAG-POS':'tree_only',
    'MR-Default-TAG-DEP-POS':'tree_only',
    'MR-Default-TAG-POS-DEP':'tree_only',
    'MR-Default-TAG-SQRT-PROD':'tree_only',
    'MR-Order-TAG-DEP':'tree_and_order',
    'MR-Order-TAG-POS':'tree_and_order',
    'MR-Order-TAG-DEP-POS':'tree_and_order',
    'MR-Order-TAG-POS-DEP':'tree_and_order',
    'MR-Order-TAG-SQRT-PROD':'tree_and_order'
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


for out in OUTPUT:
    graph_mode = out.split("/")[-1]
    tag = out.split("/")[-1].split("TAG-")[-1]
    print(">>> Building %s" % (graph_mode))
    os.system("echo python main.py -i ../Datasets/MR/Parsed/Train/ -o %s -n MR -s Train -d 300 -c 20 -l en -g %s -t %s;" % (out, HELPER[graph_mode], HELPER2[tag]))
