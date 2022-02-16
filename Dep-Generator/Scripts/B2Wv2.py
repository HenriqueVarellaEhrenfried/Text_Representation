import os


OUTPUT = ['../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-Distance', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-TAG-Distance', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-TAG-Distance', '../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-None', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-None', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-None', '../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-DEP', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-DEP', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-DEP', '../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-POS', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-POS', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-POS', '../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-DEP-POS', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-DEP-POS', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-DEP-POS', '../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-POS-DEP', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-POS-DEP', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-POS-DEP', '../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-SQRT-PROD', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-SQRT-PROD', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-SQRT-PROD', '../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-Distance', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-Distance', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-Distance', '../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-DEP', '../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-POS', '../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-DEP-POS', '../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-POS-DEP', '../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-SQRT-PROD', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-TAG-DEP', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-TAG-POS', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-TAG-DEP-POS', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-TAG-POS-DEP', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-TAG-SQRT-PROD']
GRAPH_MODE = ['tree_only', 'tree_and_order', 'tree_and_order_multi_graph', 'tree_and_self', 'tree_order_and_self', 'tree_order_multigraph_and_self']
TAG_MODE = ['none', 'dep', 'pos', 'dep-pos', 'pos-dep', 'sqrt_product', 'distance']

HELPER = {
    'B2W_COMPLETE-Rating-Default-TAG-Distance':'tree_only',
    'B2W_COMPLETE-Rating-Order-TAG-Distance':'tree_and_order',
    'B2W_COMPLETE-Rating-Order-Multigraph-TAG-Distance':'tree_and_order_multi_graph',
    'B2W_COMPLETE-Rating-Default-Self-TAG-None':'tree_and_self',
    'B2W_COMPLETE-Rating-Order-Self-TAG-None':'tree_order_and_self',
    'B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-None':'tree_order_multigraph_and_self',
    'B2W_COMPLETE-Rating-Default-Self-TAG-DEP':'tree_and_self',
    'B2W_COMPLETE-Rating-Order-Self-TAG-DEP':'tree_order_and_self',
    'B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-DEP':'tree_order_multigraph_and_self',
    'B2W_COMPLETE-Rating-Default-Self-TAG-POS':'tree_and_self',
    'B2W_COMPLETE-Rating-Order-Self-TAG-POS':'tree_order_and_self',
    'B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-POS':'tree_order_multigraph_and_self',
    'B2W_COMPLETE-Rating-Default-Self-TAG-DEP-POS':'tree_and_self',
    'B2W_COMPLETE-Rating-Order-Self-TAG-DEP-POS':'tree_order_and_self',
    'B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-DEP-POS':'tree_order_multigraph_and_self',
    'B2W_COMPLETE-Rating-Default-Self-TAG-POS-DEP':'tree_and_self',
    'B2W_COMPLETE-Rating-Order-Self-TAG-POS-DEP':'tree_order_and_self',
    'B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-POS-DEP':'tree_order_multigraph_and_self',
    'B2W_COMPLETE-Rating-Default-Self-TAG-SQRT-PROD':'tree_and_self',
    'B2W_COMPLETE-Rating-Order-Self-TAG-SQRT-PROD':'tree_order_and_self',
    'B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-SQRT-PROD':'tree_order_multigraph_and_self',
    'B2W_COMPLETE-Rating-Default-Self-TAG-Distance':'tree_and_self',
    'B2W_COMPLETE-Rating-Order-Self-TAG-Distance':'tree_order_and_self',
    'B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-Distance':'tree_order_multigraph_and_self',

    'B2W_COMPLETE-Rating-Default-TAG-DEP':'tree_only',
    'B2W_COMPLETE-Rating-Default-TAG-POS':'tree_only',
    'B2W_COMPLETE-Rating-Default-TAG-DEP-POS':'tree_only',
    'B2W_COMPLETE-Rating-Default-TAG-POS-DEP':'tree_only',
    'B2W_COMPLETE-Rating-Default-TAG-SQRT-PROD':'tree_only',
    'B2W_COMPLETE-Rating-Order-TAG-DEP':'tree_and_order',
    'B2W_COMPLETE-Rating-Order-TAG-POS':'tree_and_order',
    'B2W_COMPLETE-Rating-Order-TAG-DEP-POS':'tree_and_order',
    'B2W_COMPLETE-Rating-Order-TAG-POS-DEP':'tree_and_order',
    'B2W_COMPLETE-Rating-Order-TAG-SQRT-PROD':'tree_and_order'
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
    print("mkdir -p %s" %(out))

print("\n")

for out in OUTPUT:
    graph_mode = out.split("/")[-1]
    tag = out.split("/")[-1].split("TAG-")[-1]
    print("echo \">>> Building %s\"" % (graph_mode))
    print("python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o %s -n B2W-Rating -s Train -d 300 -c 20 -l pt -g %s -t %s;" % (out, HELPER[graph_mode], HELPER2[tag]))
    print("")