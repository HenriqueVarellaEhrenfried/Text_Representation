## Tree Variations
mkdir ../Datasets/MR/MR-Default/ 
mkdir ../Datasets/MR/MR-Order/ 
mkdir ../Datasets/MR/MR-Order-Multigraph/ 


## Node TAGS Datasets
mkdir ../Datasets/MR/MR-Order-Multigraph-Tag-Dep/ 
mkdir ../Datasets/MR/MR-Order-Multigraph-Tag-POS/ 
mkdir ../Datasets/MR/MR-Order-Multigraph-Tag-DEP_POS/ 
mkdir ../Datasets/MR/MR-Order-Multigraph-Tag-POS_DEP/
mkdir ../Datasets/MR/MR-Order-Multigraph-Tag-SQRT_PROD/

echo ">>> Building Tree Only"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Default/ -n MR -s Train -d 300 -c 20 -l en -g tree_only;

echo ">>> Building Tree and Order"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Order/ -n MR -s Train -d 300 -c 20 -l en -g tree_and_order;

echo ">>> Building Multigraph"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Order-Multigraph/ -n MR -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph;

echo ">>> Building DEP Tag"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Order-Multigraph-Tag-Dep/ -n MR -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph -t dep;

echo ">>> Building POS Tag"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Order-Multigraph-Tag-POS/ -n MR -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph -t pos;

echo ">>> Building DEP-POS Tag"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Order-Multigraph-Tag-DEP_POS/ -n MR -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph -t dep-pos;

echo ">>> Building POS-DEP Tag"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Order-Multigraph-Tag-POS_DEP/ -n MR -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph -t pos-dep;

echo ">>> Building SQRT-PROD Tag"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Order-Multigraph-Tag-SQRT_PROD/ -n MR -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph -t sqrt_product;


