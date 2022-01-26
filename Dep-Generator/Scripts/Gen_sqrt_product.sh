mkdir ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order-Multigraph-Tag-SQRT_PROD-PT/ 
mkdir ../Datasets/MR/MR_COMLPLETE-Order-Multigraph-Tag-SQRT_PROD/ 


echo ">>>> MR"

python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR_COMLPLETE-Order-Multigraph-Tag-SQRT_PROD/ -n MR -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph -t sqrt_product


echo ">>>> B2W-Rating"

python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order-Multigraph-Tag-SQRT_PROD-PT/ -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_and_order_multi_graph -t sqrt_product;


mv ../Datasets/MR/MR_COMLPLETE-Order-Multigraph-Tag-SQRT_PROD/Train_MR.txt ../Datasets/MR/MR_COMLPLETE-Order-Multigraph-Tag-SQRT_PROD/MR_COMLPLETE-Order-Multigraph-Tag-SQRT_PROD.txt 
mv ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order-Multigraph-Tag-SQRT_PROD-PT/Train_B2W-Rating.txt ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order-Multigraph-Tag-SQRT_PROD-PT/B2W_COMPLETE-Rating-Order-Multigraph-Tag-SQRT_PROD-PT.txt

cp -r  ../Datasets/MR/MR_COMLPLETE-Order-Multigraph-Tag-SQRT_PROD/ ../../Graph-Transformer/dataset/;
cp -r  ../Datasets/B2W-PT/B2W_COMPLETE-Rating-Order-Multigraph-Tag-SQRT_PROD-PT/ ../../Graph-Transformer/dataset/;