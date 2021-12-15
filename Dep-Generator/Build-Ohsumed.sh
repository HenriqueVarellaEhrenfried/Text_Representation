## Tree Variations
mkdir ../Datasets/Ohsumed/Ohsumed-Default/ 
mkdir ../Datasets/Ohsumed/Ohsumed-Order/ 
mkdir ../Datasets/Ohsumed/Ohsumed-Order-Multigraph/ 


## Node TAGS Datasets
mkdir ../Datasets/Ohsumed/Ohsumed-Order-Multigraph-Tag-Dep/ 
mkdir ../Datasets/Ohsumed/Ohsumed-Order-Multigraph-Tag-POS/ 
mkdir ../Datasets/Ohsumed/Ohsumed-Order-Multigraph-Tag-DEP_POS/ 
mkdir ../Datasets/Ohsumed/Ohsumed-Order-Multigraph-Tag-POS_DEP/
mkdir ../Datasets/Ohsumed/Ohsumed-Order-Multigraph-Tag-SQRT_PROD/

echo ">>> Building Tree Only"
python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o ../Datasets/Ohsumed/Ohsumed-Default/ -n Ohsumed -s Train -d 300 -c 20 -l en -g tree_only;

echo ">>> Building Tree and Order"
python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o ../Datasets/Ohsumed/Ohsumed-Order/ -n Ohsumed -s Train -d 300 -c 20 -l en -g tree_and_order;

echo ">>> Building Multigraph"
python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o ../Datasets/Ohsumed/Ohsumed-Order-Multigraph/ -n Ohsumed -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph;

echo ">>> Building DEP Tag"
python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o ../Datasets/Ohsumed/Ohsumed-Order-Multigraph-Tag-Dep/ -n Ohsumed -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph -t dep;

echo ">>> Building POS Tag"
python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o ../Datasets/Ohsumed/Ohsumed-Order-Multigraph-Tag-POS/ -n Ohsumed -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph -t pos;

echo ">>> Building DEP-POS Tag"
python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o ../Datasets/Ohsumed/Ohsumed-Order-Multigraph-Tag-DEP_POS/ -n Ohsumed -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph -t dep-pos;

echo ">>> Building POS-DEP Tag"
python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o ../Datasets/Ohsumed/Ohsumed-Order-Multigraph-Tag-POS_DEP/ -n Ohsumed -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph -t pos-dep;

echo ">>> Building SQRT-PROD Tag"
python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o ../Datasets/Ohsumed/Ohsumed-Order-Multigraph-Tag-SQRT_PROD/ -n Ohsumed -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph -t sqrt_product;


