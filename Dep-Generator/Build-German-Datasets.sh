# GRAPH_MODE = ['tree_only', 'tree_and_order', 'tree_and_order_multi_graph']
# TAG_MODE = ['none', 'dep', 'pos', 'dep-pos', 'pos-dep', 'sqrt_product']

mkdir ../Datasets/10kGNAD-DE/Tree/ 
mkdir ../Datasets/10kGNAD-DE/Tree-Order/ 
mkdir ../Datasets/10kGNAD-DE/Tree-Order-Multigraph/ 
mkdir ../Datasets/10kGNAD-DE/Tree-Order-Multigraph-DEP/ 
mkdir ../Datasets/10kGNAD-DE/Tree-Order-Multigraph-POS/ 
mkdir ../Datasets/10kGNAD-DE/Tree-Order-Multigraph-DEP-POS/ 
mkdir ../Datasets/10kGNAD-DE/Tree-Order-Multigraph-POS-DEP/ 
mkdir ../Datasets/10kGNAD-DE/Tree-Order-Multigraph-SQRT-PROD/ 



echo ">> Building Tree [1/8]"
python main.py -i ../Datasets/10kGNAD-DE/Parsed/ -o ../Datasets/10kGNAD-DE/Tree/ -n 10kGNAD -s Train -d 300 -c 20 -l de -g tree_only -t none

echo ">> Building Tree-Order [2/8]"
python main.py -i ../Datasets/10kGNAD-DE/Parsed/ -o ../Datasets/10kGNAD-DE/Tree-Order/ -n 10kGNAD -s Train -d 300 -c 20 -l de -g tree_and_order -t none

echo ">> Building Tree-Order-Multigraph [3/8]"
python main.py -i ../Datasets/10kGNAD-DE/Parsed/ -o ../Datasets/10kGNAD-DE/Tree-Order-Multigraph/ -n 10kGNAD -s Train -d 300 -c 20 -l de -g tree_and_order_multi_graph -t none

echo ">> Building Tree-Order-Multigraph-DEP [4/8]"
python main.py -i ../Datasets/10kGNAD-DE/Parsed/ -o ../Datasets/10kGNAD-DE/Tree-Order-Multigraph-DEP/ -n 10kGNAD -s Train -d 300 -c 20 -l de -g tree_and_order_multi_graph -t dep

echo ">> Building Tree-Order-Multigraph-POS [5/8]"
python main.py -i ../Datasets/10kGNAD-DE/Parsed/ -o ../Datasets/10kGNAD-DE/Tree-Order-Multigraph-POS/ -n 10kGNAD -s Train -d 300 -c 20 -l de -g tree_and_order_multi_graph -t pos

echo ">> Building Tree-Order-Multigraph-DEP-POS [6/8]"
python main.py -i ../Datasets/10kGNAD-DE/Parsed/ -o ../Datasets/10kGNAD-DE/Tree-Order-Multigraph-DEP-POS/ -n 10kGNAD -s Train -d 300 -c 20 -l de -g tree_and_order_multi_graph -t dep-pos

echo ">> Building Tree-Order-Multigraph-POS-DEP [7/8]"
python main.py -i ../Datasets/10kGNAD-DE/Parsed/ -o ../Datasets/10kGNAD-DE/Tree-Order-Multigraph-POS-DEP/ -n 10kGNAD -s Train -d 300 -c 20 -l de -g tree_and_order_multi_graph -t pos-dep

echo ">> Building Tree-Order-Multigraph-SQRT-PROD [8/8]"
python main.py -i ../Datasets/10kGNAD-DE/Parsed/ -o ../Datasets/10kGNAD-DE/Tree-Order-Multigraph-SQRT-PROD/ -n 10kGNAD -s Train -d 300 -c 20 -l de -g tree_and_order_multi_graph -t sqrt_product

