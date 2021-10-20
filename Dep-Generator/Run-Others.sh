
# python main.py -i ../Datasets/B2W-PT/Raw/B2W-Polarity-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Default/ -n B2W-Polarity -s Train -d 300 -c 20 -l en -g tree_only;
# python main.py -i ../Datasets/B2W-PT/Raw/B2W-Recommend-Balanced/ -o ../Datasets/B2W-PT/2W_COMPLETE-Recommend-Default/ -n B2W-Recommend -s Train -d 300 -c 20 -l en -g tree_only;
# python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Default/ -n B2W-Rating -s Train -d 300 -c 20 -l en -g tree_only;

# python main.py -i ../Datasets/B2W-PT/Raw/B2W-Polarity-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order/ -n B2W-Polarity -s Train -d 300 -c 20 -l en -g tree_and_order;
# python main.py -i ../Datasets/B2W-PT/Raw/B2W-Recommend-Balanced/ -o ../Datasets/B2W-PT/2W_COMPLETE-Recommend-Order/ -n B2W-Recommend -s Train -d 300 -c 20 -l en -g tree_and_order;
# python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order/ -n B2W-Rating -s Train -d 300 -c 20 -l en -g tree_and_order;


# python main.py -i ../Datasets/B2W-PT/Raw/B2W-Polarity-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph/ -n B2W-Polarity -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph;
# python main.py -i ../Datasets/B2W-PT/Raw/B2W-Recommend-Balanced/ -o ../Datasets/B2W-PT/2W_COMPLETE-Recommend-Order-Multigraph/ -n B2W-Recommend -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph;
# python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order-Multigraph/ -n B2W-Rating -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph;



mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-Tag-Dep/ 
mkdir ../Datasets/B2W-PT/2W_COMPLETE-Recommend-Order-Multigraph-Tag-Dep/ 
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order-Multigraph-Tag-Dep/ 
mkdir ../Datasets/MR/U2GNN-TREE-ORDER-MULTIGRAPH-Tag-Dep/ 
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-Tag-POS/ 
mkdir ../Datasets/B2W-PT/2W_COMPLETE-Recommend-Order-Multigraph-Tag-POS/ 
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order-Multigraph-Tag-POS/ 
mkdir ../Datasets/MR/U2GNN-TREE-ORDER-MULTIGRAPH-Tag-POS/ 
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-Tag-DEP_POS/ 
mkdir ../Datasets/B2W-PT/2W_COMPLETE-Recommend-Order-Multigraph-Tag-DEP_POS/ 
mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order-Multigraph-Tag-DEP_POS/ 
mkdir ../Datasets/MR/U2GNN-TREE-ORDER-MULTIGRAPH-Tag-DEP_POS/ 

echo "Building DEP Tag"
# python main.py -i ../Datasets/B2W-PT/Raw/B2W-Polarity-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-Tag-Dep/ -n B2W-Polarity -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph -t dep;
# python main.py -i ../Datasets/B2W-PT/Raw/B2W-Recommend-Balanced/ -o ../Datasets/B2W-PT/2W_COMPLETE-Recommend-Order-Multigraph-Tag-Dep/ -n B2W-Recommend -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph -t dep;
# python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order-Multigraph-Tag-Dep/ -n B2W-Rating -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph -t dep;
# python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/U2GNN-TREE-ORDER-MULTIGRAPH-Tag-Dep/ -n MR -s Train -d 300 -c 4 -l en -g tree_and_order_multi_graph -t dep;

echo "Building POS Tag"
# python main.py -i ../Datasets/B2W-PT/Raw/B2W-Polarity-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-Tag-POS/ -n B2W-Polarity -s Train -d 300 -c 1 -l en -g tree_and_order_multi_graph -t pos;
# python main.py -i ../Datasets/B2W-PT/Raw/B2W-Recommend-Balanced/ -o ../Datasets/B2W-PT/2W_COMPLETE-Recommend-Order-Multigraph-Tag-POS/ -n B2W-Recommend -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph -t pos;
# python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order-Multigraph-Tag-POS/ -n B2W-Rating -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph -t pos;
# python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/U2GNN-TREE-ORDER-MULTIGRAPH-Tag-POS/ -n MR -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph -t pos;

echo "Building DEP-POS Tag"
# python main.py -i ../Datasets/B2W-PT/Raw/B2W-Polarity-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order-Multigraph-Tag-DEP_POS/ -n B2W-Polarity -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph -t dep-pos;
# python main.py -i ../Datasets/B2W-PT/Raw/B2W-Recommend-Balanced/ -o ../Datasets/B2W-PT/2W_COMPLETE-Recommend-Order-Multigraph-Tag-DEP_POS/ -n B2W-Recommend -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph -t dep-pos;
# python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order-Multigraph-Tag-DEP_POS/ -n B2W-Rating -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph -t dep-pos;
# python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/U2GNN-TREE-ORDER-MULTIGRAPH-Tag-DEP_POS/ -n MR -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph -t dep-pos;
