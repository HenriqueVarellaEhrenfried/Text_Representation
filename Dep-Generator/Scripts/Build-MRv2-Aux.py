import os


OUTPUT = ['../Datasets/MR/MR-Default-TAG-Distance', '../Datasets/MR/MR-Order-TAG-Distance', '../Datasets/MR/MR-Order-Multigraph-TAG-Distance', '../Datasets/MR/MR-Default-Self-TAG-None', '../Datasets/MR/MR-Order-Self-TAG-None', '../Datasets/MR/MR-Order-Multigraph-Self-TAG-None', '../Datasets/MR/MR-Default-Self-TAG-DEP', '../Datasets/MR/MR-Order-Self-TAG-DEP', '../Datasets/MR/MR-Order-Multigraph-Self-TAG-DEP', '../Datasets/MR/MR-Default-Self-TAG-POS', '../Datasets/MR/MR-Order-Self-TAG-POS', '../Datasets/MR/MR-Order-Multigraph-Self-TAG-POS', '../Datasets/MR/MR-Default-Self-TAG-DEP-POS', '../Datasets/MR/MR-Order-Self-TAG-DEP-POS', '../Datasets/MR/MR-Order-Multigraph-Self-TAG-DEP-POS', '../Datasets/MR/MR-Default-Self-TAG-POS-DEP', '../Datasets/MR/MR-Order-Self-TAG-POS-DEP', '../Datasets/MR/MR-Order-Multigraph-Self-TAG-POS-DEP', '../Datasets/MR/MR-Default-Self-TAG-SQRT-PROD', '../Datasets/MR/MR-Order-Self-TAG-SQRT-PROD', '../Datasets/MR/MR-Order-Multigraph-Self-TAG-SQRT-PROD', '../Datasets/MR/MR-Default-Self-TAG-Distance', '../Datasets/MR/MR-Order-Self-TAG-Distance', '../Datasets/MR/MR-Order-Multigraph-Self-TAG-Distance']
GRAPH_MODE = ['tree_only', 'tree_and_order', 'tree_and_order_multi_graph', 'tree_and_self', 'tree_order_and_self', 'tree_order_multigraph_and_self']
TAG_MODE = ['none', 'dep', 'pos', 'dep-pos', 'pos-dep', 'sqrt_product', 'distance']

HELPER = {
    'MR-Default-TAG-Distance':'tree_only',
    'MR-Order-TAG-Distance':'tree_and_order',
    'MR-Order-Multigraph-TAG-Distance':'tree_and_order_multi_graph',
    'MR-Default-Self-TAG-None':'tree_and_self',
    'MR-Order-Self-TAG-None':'tree_order_and_self',
    'MR-Order-Multigraph-Self-TAG-None':'tree_order_multigraph_and_self',
    'MR-Default-Self-TAG-DEP':'tree_and_self',
    'MR-Order-Self-TAG-DEP':'tree_order_and_self',
    'MR-Order-Multigraph-Self-TAG-DEP':'tree_order_multigraph_and_self',
    'MR-Default-Self-TAG-POS':'tree_and_self',
    'MR-Order-Self-TAG-POS':'tree_order_and_self',
    'MR-Order-Multigraph-Self-TAG-POS':'tree_order_multigraph_and_self',
    'MR-Default-Self-TAG-DEP-POS':'tree_and_self',
    'MR-Order-Self-TAG-DEP-POS':'tree_order_and_self',
    'MR-Order-Multigraph-Self-TAG-DEP-POS':'tree_order_multigraph_and_self',
    'MR-Default-Self-TAG-POS-DEP':'tree_and_self',
    'MR-Order-Self-TAG-POS-DEP':'tree_order_and_self',
    'MR-Order-Multigraph-Self-TAG-POS-DEP':'tree_order_multigraph_and_self',
    'MR-Default-Self-TAG-SQRT-PROD':'tree_and_self',
    'MR-Order-Self-TAG-SQRT-PROD':'tree_order_and_self',
    'MR-Order-Multigraph-Self-TAG-SQRT-PROD':'tree_order_multigraph_and_self',
    'MR-Default-Self-TAG-Distance':'tree_and_self',
    'MR-Order-Self-TAG-Distance':'tree_order_and_self',
    'MR-Order-Multigraph-Self-TAG-Distance':'tree_order_multigraph_and_self',
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

