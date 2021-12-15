python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/U2GNN-TREE-ORDER-MULTIGRAPH/ -n MR -s Train -d 300 -c 4 -l en -g tree_and_order_multi_graph

python main.py -i ../Datasets/B2W-PT/Raw/B2W-Polarity-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Polarity/ -n B2W-Polarity -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Recommend-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Recommend/ -n B2W-Recommend -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Rating/ -n B2W-Rating -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph


mkdir B2W_COMPLETE-Polarity-Default;
mkdir B2W_COMPLETE-Recommend-Default;
mkdir B2W_COMPLETE-Rating-Default;
mkdir B2W_COMPLETE-Polarity-Order;
mkdir B2W_COMPLETE-Recommend-Order;
mkdir B2W_COMPLETE-Rating-Order;


python main.py -i ../Datasets/B2W-PT/Raw/B2W-Polarity-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Default/ -n B2W-Polarity -s Train -d 300 -c 20 -l en -g tree_only
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Recommend-Balanced/ -o ../Datasets/B2W-PT/2W_COMPLETE-Recommend-Default/ -n B2W-Recommend -s Train -d 300 -c 20 -l en -g tree_only
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Default/ -n B2W-Rating -s Train -d 300 -c 20 -l en -g tree_only

python main.py -i ../Datasets/B2W-PT/Raw/B2W-Polarity-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Polarity-Order/ -n B2W-Polarity -s Train -d 300 -c 20 -l en -g tree_and_order
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Recommend-Balanced/ -o ../Datasets/B2W-PT/2W_COMPLETE-Recommend-Order/ -n B2W-Recommend -s Train -d 300 -c 20 -l en -g tree_and_order
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order/ -n B2W-Rating -s Train -d 300 -c 20 -l en -g tree_and_order
