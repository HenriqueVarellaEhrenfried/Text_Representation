mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order-Multigraph-Tag-POS_DEP-PT/ 
mkdir ../Datasets/MR/MR_COMLPLETE-Order-Multigraph-Tag-POS_DEP/ 


echo ">>>> MR"

python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR_COMLPLETE-Order-Multigraph-Tag-POS_DEP/ -n MR -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph -t pos-dep


echo ">>>> B2W-Rating"

python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order-Multigraph-Tag-POS_DEP-PT/ -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_and_order_multi_graph -t pos-dep;
