import os


OUTPUT = ['../Datasets/Ohsumed/Ohsumed-Default-TAG-Distance', '../Datasets/Ohsumed/Ohsumed-Order-TAG-Distance', '../Datasets/Ohsumed/Ohsumed-Order-Multigraph-TAG-Distance', '../Datasets/Ohsumed/Ohsumed-Default-Self-TAG-None', '../Datasets/Ohsumed/Ohsumed-Order-Self-TAG-None', '../Datasets/Ohsumed/Ohsumed-Order-Multigraph-Self-TAG-None', '../Datasets/Ohsumed/Ohsumed-Default-Self-TAG-DEP', '../Datasets/Ohsumed/Ohsumed-Order-Self-TAG-DEP', '../Datasets/Ohsumed/Ohsumed-Order-Multigraph-Self-TAG-DEP', '../Datasets/Ohsumed/Ohsumed-Default-Self-TAG-POS', '../Datasets/Ohsumed/Ohsumed-Order-Self-TAG-POS', '../Datasets/Ohsumed/Ohsumed-Order-Multigraph-Self-TAG-POS', '../Datasets/Ohsumed/Ohsumed-Default-Self-TAG-DEP-POS', '../Datasets/Ohsumed/Ohsumed-Order-Self-TAG-DEP-POS', '../Datasets/Ohsumed/Ohsumed-Order-Multigraph-Self-TAG-DEP-POS', '../Datasets/Ohsumed/Ohsumed-Default-Self-TAG-POS-DEP', '../Datasets/Ohsumed/Ohsumed-Order-Self-TAG-POS-DEP', '../Datasets/Ohsumed/Ohsumed-Order-Multigraph-Self-TAG-POS-DEP', '../Datasets/Ohsumed/Ohsumed-Default-Self-TAG-SQRT-PROD', '../Datasets/Ohsumed/Ohsumed-Order-Self-TAG-SQRT-PROD', '../Datasets/Ohsumed/Ohsumed-Order-Multigraph-Self-TAG-SQRT-PROD', '../Datasets/Ohsumed/Ohsumed-Default-Self-TAG-Distance', '../Datasets/Ohsumed/Ohsumed-Order-Self-TAG-Distance', '../Datasets/Ohsumed/Ohsumed-Order-Multigraph-Self-TAG-Distance', '../Datasets/Ohsumed/Ohsumed-Default-TAG-DEP', '../Datasets/Ohsumed/Ohsumed-Default-TAG-POS', '../Datasets/Ohsumed/Ohsumed-Default-TAG-DEP-POS', '../Datasets/Ohsumed/Ohsumed-Default-TAG-POS-DEP', '../Datasets/Ohsumed/Ohsumed-Default-TAG-SQRT-PROD', '../Datasets/Ohsumed/Ohsumed-Order-TAG-DEP', '../Datasets/Ohsumed/Ohsumed-Order-TAG-POS', '../Datasets/Ohsumed/Ohsumed-Order-TAG-DEP-POS', '../Datasets/Ohsumed/Ohsumed-Order-TAG-POS-DEP', '../Datasets/Ohsumed/Ohsumed-Order-TAG-SQRT-PROD']
GRAPH_MODE = ['tree_only', 'tree_and_order', 'tree_and_order_multi_graph', 'tree_and_self', 'tree_order_and_self', 'tree_order_multigraph_and_self']
TAG_MODE = ['none', 'dep', 'pos', 'dep-pos', 'pos-dep', 'sqrt_product', 'distance']

HELPER = {
    'Ohsumed-Default-TAG-Distance':'tree_only',
    'Ohsumed-Order-TAG-Distance':'tree_and_order',
    'Ohsumed-Order-Multigraph-TAG-Distance':'tree_and_order_multi_graph',
    'Ohsumed-Default-Self-TAG-None':'tree_and_self',
    'Ohsumed-Order-Self-TAG-None':'tree_order_and_self',
    'Ohsumed-Order-Multigraph-Self-TAG-None':'tree_order_multigraph_and_self',
    'Ohsumed-Default-Self-TAG-DEP':'tree_and_self',
    'Ohsumed-Order-Self-TAG-DEP':'tree_order_and_self',
    'Ohsumed-Order-Multigraph-Self-TAG-DEP':'tree_order_multigraph_and_self',
    'Ohsumed-Default-Self-TAG-POS':'tree_and_self',
    'Ohsumed-Order-Self-TAG-POS':'tree_order_and_self',
    'Ohsumed-Order-Multigraph-Self-TAG-POS':'tree_order_multigraph_and_self',
    'Ohsumed-Default-Self-TAG-DEP-POS':'tree_and_self',
    'Ohsumed-Order-Self-TAG-DEP-POS':'tree_order_and_self',
    'Ohsumed-Order-Multigraph-Self-TAG-DEP-POS':'tree_order_multigraph_and_self',
    'Ohsumed-Default-Self-TAG-POS-DEP':'tree_and_self',
    'Ohsumed-Order-Self-TAG-POS-DEP':'tree_order_and_self',
    'Ohsumed-Order-Multigraph-Self-TAG-POS-DEP':'tree_order_multigraph_and_self',
    'Ohsumed-Default-Self-TAG-SQRT-PROD':'tree_and_self',
    'Ohsumed-Order-Self-TAG-SQRT-PROD':'tree_order_and_self',
    'Ohsumed-Order-Multigraph-Self-TAG-SQRT-PROD':'tree_order_multigraph_and_self',
    'Ohsumed-Default-Self-TAG-Distance':'tree_and_self',
    'Ohsumed-Order-Self-TAG-Distance':'tree_order_and_self',
    'Ohsumed-Order-Multigraph-Self-TAG-Distance':'tree_order_multigraph_and_self',

    'Ohsumed-Default-TAG-DEP':'tree_only',
    'Ohsumed-Default-TAG-POS':'tree_only',
    'Ohsumed-Default-TAG-DEP-POS':'tree_only',
    'Ohsumed-Default-TAG-POS-DEP':'tree_only',
    'Ohsumed-Default-TAG-SQRT-PROD':'tree_only',
    'Ohsumed-Order-TAG-DEP':'tree_and_order',
    'Ohsumed-Order-TAG-POS':'tree_and_order',
    'Ohsumed-Order-TAG-DEP-POS':'tree_and_order',
    'Ohsumed-Order-TAG-POS-DEP':'tree_and_order',
    'Ohsumed-Order-TAG-SQRT-PROD':'tree_and_order'
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
    os.system("echo python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o %s -n Ohsumed -s Train -d 300 -c 20 -l en -g %s -t %s;" % (out, HELPER[graph_mode], HELPER2[tag]))
