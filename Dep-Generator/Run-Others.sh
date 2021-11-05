## Tree Variations
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Default-PT/ 
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Recommend-Default-PT/ 
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Default-PT/ 

mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-PT/ 
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Recommend-Order-PT/ 
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order-PT/ 

mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-PT/ 
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Recommend-Order-Multigraph-PT/ 
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order-Multigraph-PT/ 

## Node TAGS Datasets
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-Tag-Dep-PT/ 
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Recommend-Order-Multigraph-Tag-Dep-PT/ 
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order-Multigraph-Tag-Dep-PT/ 

mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-Tag-POS-PT/ 
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Recommend-Order-Multigraph-Tag-POS-PT/ 
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order-Multigraph-Tag-POS-PT/ 

mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-Tag-DEP_POS-PT/ 
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Recommend-Order-Multigraph-Tag-DEP_POS-PT/ 
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order-Multigraph-Tag-DEP_POS-PT/ 



echo ">>> Building Tree Only"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Polarity-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Default-PT/ -n B2W-Polarity -s Train -d 300 -c 20 -l pt -g tree_only;
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Recommend-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Recommend-Default-PT/ -n B2W-Recommend -s Train -d 300 -c 20 -l pt -g tree_only;
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Default-PT/ -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_only;

echo ">>> Building Tree and Order"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Polarity-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-PT/ -n B2W-Polarity -s Train -d 300 -c 20 -l pt -g tree_and_order;
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Recommend-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Recommend-Order-PT/ -n B2W-Recommend -s Train -d 300 -c 20 -l pt -g tree_and_order;
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order-PT/ -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_and_order;

echo ">>> Building Multigraph"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Polarity-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-PT/ -n B2W-Polarity -s Train -d 300 -c 20 -l pt -g tree_and_order_multi_graph;
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Recommend-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Recommend-Order-Multigraph-PT/ -n B2W-Recommend -s Train -d 300 -c 20 -l pt -g tree_and_order_multi_graph;
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order-Multigraph-PT/ -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_and_order_multi_graph;


echo ">>> Building DEP Tag"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Polarity-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-Tag-Dep-PT/ -n B2W-Polarity -s Train -d 300 -c 20 -l pt -g tree_and_order_multi_graph -t dep;
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Recommend-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Recommend-Order-Multigraph-Tag-Dep-PT/ -n B2W-Recommend -s Train -d 300 -c 20 -l pt -g tree_and_order_multi_graph -t dep;
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order-Multigraph-Tag-Dep-PT/ -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_and_order_multi_graph -t dep;

echo ">>> Building POS Tag"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Polarity-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-Tag-POS-PT/ -n B2W-Polarity -s Train -d 300 -c 1 -l pt -g tree_and_order_multi_graph -t pos;
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Recommend-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Recommend-Order-Multigraph-Tag-POS-PT/ -n B2W-Recommend -s Train -d 300 -c 20 -l pt -g tree_and_order_multi_graph -t pos;
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order-Multigraph-Tag-POS-PT/ -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_and_order_multi_graph -t pos;

echo ">>> Building DEP-POS Tag"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Polarity-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-Tag-DEP_POS-PT/ -n B2W-Polarity -s Train -d 300 -c 20 -l pt -g tree_and_order_multi_graph -t dep-pos;
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Recommend-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Recommend-Order-Multigraph-Tag-DEP_POS-PT/ -n B2W-Recommend -s Train -d 300 -c 20 -l pt -g tree_and_order_multi_graph -t dep-pos;
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order-Multigraph-Tag-DEP_POS-PT/ -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_and_order_multi_graph -t dep-pos;
