import os


OUTPUT = ['../Datasets/10kGNAD-DE/10kGNAD-DE-Default-Self-TAG-None', '../Datasets/10kGNAD-DE/10kGNAD-DE-Order-Self-TAG-None', '../Datasets/10kGNAD-DE/10kGNAD-DE-Order-Multigraph-Self-TAG-None', '../Datasets/10kGNAD-DE/10kGNAD-DE-Only-Order-TAG-None', '../Datasets/10kGNAD-DE/10kGNAD-DE-Order-Circular-TAG-None', '../Datasets/10kGNAD-DE/10kGNAD-DE-Binary-Tree-TAG-None']
GRAPH_MODE = ['tree_only', 'tree_and_order', 'tree_and_order_multi_graph', 'tree_and_self', 'tree_order_and_self', 'tree_order_multigraph_and_self']
TAG_MODE = ['none', 'dep', 'pos', 'dep-pos', 'pos-dep', 'sqrt_product', 'distance']

HELPER = {
    '10kGNAD-DE-Default-Self-TAG-None':'tree_and_self',
    '10kGNAD-DE-Order-Self-TAG-None':'tree_order_and_self',
    '10kGNAD-DE-Order-Multigraph-Self-TAG-None':'tree_order_multigraph_and_self',

    '10kGNAD-DE-Only-Order-TAG-None':'only_order',
    '10kGNAD-DE-Order-Circular-TAG-None':'order_circular',
    '10kGNAD-DE-Binary-Tree-TAG-None':'binary_tree'   
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

print("")
for out in OUTPUT:
    graph_mode = out.split("/")[-1]
    tag = out.split("/")[-1].split("TAG-")[-1]
    print("echo \">>> Building %s\"" % (graph_mode))
    print("python main.py -i ../Datasets/10kGNAD-DE/Parsed/ -o %s -n 10kGNAD-DE -s Train -d 300 -c 1 -l de -g %s -t %s;" % (out, HELPER[graph_mode], HELPER2[tag]))
    print("")