## Tree Variations
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Default-PT/ 
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-PT/ 
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-PT/ 


## Node TAGS Datasets
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-Tag-Dep-PT/ 
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-Tag-POS-PT/ 
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-Tag-DEP_POS-PT/ 
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-Tag-POS_DEP-PT/
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-Tag-SQRT_PROD-PT/

echo ">>> Building Tree Only"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Polarity-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Default-PT/ -n B2W-Polarity -s Train -d 300 -c 20 -l pt -g tree_only;

echo ">>> Building Tree and Order"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Polarity-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-PT/ -n B2W-Polarity -s Train -d 300 -c 20 -l pt -g tree_and_order;

echo ">>> Building Multigraph"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Polarity-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-PT/ -n B2W-Polarity -s Train -d 300 -c 20 -l pt -g tree_and_order_multi_graph;

echo ">>> Building DEP Tag"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Polarity-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-Tag-Dep-PT/ -n B2W-Polarity -s Train -d 300 -c 20 -l pt -g tree_and_order_multi_graph -t dep;

echo ">>> Building POS Tag"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Polarity-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-Tag-POS-PT/ -n B2W-Polarity -s Train -d 300 -c 20 -l pt -g tree_and_order_multi_graph -t pos;

echo ">>> Building DEP-POS Tag"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Polarity-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-Tag-DEP_POS-PT/ -n B2W-Polarity -s Train -d 300 -c 20 -l pt -g tree_and_order_multi_graph -t dep-pos;

echo ">>> Building POS-DEP Tag"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Polarity-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-Tag-POS_DEP-PT/ -n B2W-Polarity -s Train -d 300 -c 20 -l pt -g tree_and_order_multi_graph -t pos-dep;

echo ">>> Building SQRT-PROD Tag"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Polarity-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-Tag-SQRT_PROD-PT/ -n B2W-Polarity -s Train -d 300 -c 20 -l pt -g tree_and_order_multi_graph -t sqrt_product;


