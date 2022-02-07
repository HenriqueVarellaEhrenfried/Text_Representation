import os


OUTPUT = ['../Datasets/10kGNAD-DE/10kGNAD-DE-Default-TAG-Distance', '../Datasets/10kGNAD-DE/10kGNAD-DE-Order-TAG-Distance', '../Datasets/10kGNAD-DE/10kGNAD-DE-Order-Multigraph-TAG-Distance', '../Datasets/10kGNAD-DE/10kGNAD-DE-Default-Self-TAG-None', '../Datasets/10kGNAD-DE/10kGNAD-DE-Order-Self-TAG-None', '../Datasets/10kGNAD-DE/10kGNAD-DE-Order-Multigraph-Self-TAG-None', '../Datasets/10kGNAD-DE/10kGNAD-DE-Default-Self-TAG-DEP', '../Datasets/10kGNAD-DE/10kGNAD-DE-Order-Self-TAG-DEP', '../Datasets/10kGNAD-DE/10kGNAD-DE-Order-Multigraph-Self-TAG-DEP', '../Datasets/10kGNAD-DE/10kGNAD-DE-Default-Self-TAG-POS', '../Datasets/10kGNAD-DE/10kGNAD-DE-Order-Self-TAG-POS', '../Datasets/10kGNAD-DE/10kGNAD-DE-Order-Multigraph-Self-TAG-POS', '../Datasets/10kGNAD-DE/10kGNAD-DE-Default-Self-TAG-DEP-POS', '../Datasets/10kGNAD-DE/10kGNAD-DE-Order-Self-TAG-DEP-POS', '../Datasets/10kGNAD-DE/10kGNAD-DE-Order-Multigraph-Self-TAG-DEP-POS', '../Datasets/10kGNAD-DE/10kGNAD-DE-Default-Self-TAG-POS-DEP', '../Datasets/10kGNAD-DE/10kGNAD-DE-Order-Self-TAG-POS-DEP', '../Datasets/10kGNAD-DE/10kGNAD-DE-Order-Multigraph-Self-TAG-POS-DEP', '../Datasets/10kGNAD-DE/10kGNAD-DE-Default-Self-TAG-SQRT-PROD', '../Datasets/10kGNAD-DE/10kGNAD-DE-Order-Self-TAG-SQRT-PROD', '../Datasets/10kGNAD-DE/10kGNAD-DE-Order-Multigraph-Self-TAG-SQRT-PROD', '../Datasets/10kGNAD-DE/10kGNAD-DE-Default-Self-TAG-Distance', '../Datasets/10kGNAD-DE/10kGNAD-DE-Order-Self-TAG-Distance', '../Datasets/10kGNAD-DE/10kGNAD-DE-Order-Multigraph-Self-TAG-Distance', '../Datasets/10kGNAD-DE/10kGNAD-DE-Default-TAG-DEP', '../Datasets/10kGNAD-DE/10kGNAD-DE-Default-TAG-POS', '../Datasets/10kGNAD-DE/10kGNAD-DE-Default-TAG-DEP-POS', '../Datasets/10kGNAD-DE/10kGNAD-DE-Default-TAG-POS-DEP', '../Datasets/10kGNAD-DE/10kGNAD-DE-Default-TAG-SQRT-PROD', '../Datasets/10kGNAD-DE/10kGNAD-DE-Order-TAG-DEP', '../Datasets/10kGNAD-DE/10kGNAD-DE-Order-TAG-POS', '../Datasets/10kGNAD-DE/10kGNAD-DE-Order-TAG-DEP-POS', '../Datasets/10kGNAD-DE/10kGNAD-DE-Order-TAG-POS-DEP', '../Datasets/10kGNAD-DE/10kGNAD-DE-Order-TAG-SQRT-PROD']
GRAPH_MODE = ['tree_only', 'tree_and_order', 'tree_and_order_multi_graph', 'tree_and_self', 'tree_order_and_self', 'tree_order_multigraph_and_self']
TAG_MODE = ['none', 'dep', 'pos', 'dep-pos', 'pos-dep', 'sqrt_product', 'distance']

HELPER = {
    '10kGNAD-DE-Default-TAG-Distance':'tree_only',
    '10kGNAD-DE-Order-TAG-Distance':'tree_and_order',
    '10kGNAD-DE-Order-Multigraph-TAG-Distance':'tree_and_order_multi_graph',
    '10kGNAD-DE-Default-Self-TAG-None':'tree_and_self',
    '10kGNAD-DE-Order-Self-TAG-None':'tree_order_and_self',
    '10kGNAD-DE-Order-Multigraph-Self-TAG-None':'tree_order_multigraph_and_self',
    '10kGNAD-DE-Default-Self-TAG-DEP':'tree_and_self',
    '10kGNAD-DE-Order-Self-TAG-DEP':'tree_order_and_self',
    '10kGNAD-DE-Order-Multigraph-Self-TAG-DEP':'tree_order_multigraph_and_self',
    '10kGNAD-DE-Default-Self-TAG-POS':'tree_and_self',
    '10kGNAD-DE-Order-Self-TAG-POS':'tree_order_and_self',
    '10kGNAD-DE-Order-Multigraph-Self-TAG-POS':'tree_order_multigraph_and_self',
    '10kGNAD-DE-Default-Self-TAG-DEP-POS':'tree_and_self',
    '10kGNAD-DE-Order-Self-TAG-DEP-POS':'tree_order_and_self',
    '10kGNAD-DE-Order-Multigraph-Self-TAG-DEP-POS':'tree_order_multigraph_and_self',
    '10kGNAD-DE-Default-Self-TAG-POS-DEP':'tree_and_self',
    '10kGNAD-DE-Order-Self-TAG-POS-DEP':'tree_order_and_self',
    '10kGNAD-DE-Order-Multigraph-Self-TAG-POS-DEP':'tree_order_multigraph_and_self',
    '10kGNAD-DE-Default-Self-TAG-SQRT-PROD':'tree_and_self',
    '10kGNAD-DE-Order-Self-TAG-SQRT-PROD':'tree_order_and_self',
    '10kGNAD-DE-Order-Multigraph-Self-TAG-SQRT-PROD':'tree_order_multigraph_and_self',
    '10kGNAD-DE-Default-Self-TAG-Distance':'tree_and_self',
    '10kGNAD-DE-Order-Self-TAG-Distance':'tree_order_and_self',
    '10kGNAD-DE-Order-Multigraph-Self-TAG-Distance':'tree_order_multigraph_and_self',

    '10kGNAD-DE-Default-TAG-DEP':'tree_only',
    '10kGNAD-DE-Default-TAG-POS':'tree_only',
    '10kGNAD-DE-Default-TAG-DEP-POS':'tree_only',
    '10kGNAD-DE-Default-TAG-POS-DEP':'tree_only',
    '10kGNAD-DE-Default-TAG-SQRT-PROD':'tree_only',
    '10kGNAD-DE-Order-TAG-DEP':'tree_and_order',
    '10kGNAD-DE-Order-TAG-POS':'tree_and_order',
    '10kGNAD-DE-Order-TAG-DEP-POS':'tree_and_order',
    '10kGNAD-DE-Order-TAG-POS-DEP':'tree_and_order',
    '10kGNAD-DE-Order-TAG-SQRT-PROD':'tree_and_order'
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
    os.system("echo python main.py -i ../Datasets/10kGNAD-DE/Parsed/ -o %s -n 10kGNAD-DE -s Train -d 300 -c 20 -l en -g %s -t %s;" % (out, HELPER[graph_mode], HELPER2[tag]))
