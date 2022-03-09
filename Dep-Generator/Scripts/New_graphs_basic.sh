mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Only_Order-TAG-None
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Order_Circular-TAG-None
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Binary_Tree-TAG-None
mkdir -p ../Datasets/MR/MR-Only_Order-TAG-None
mkdir -p ../Datasets/MR/MR-Order_Circular-TAG-None
mkdir -p ../Datasets/MR/MR-Binary_Tree-TAG-None


echo ">>> Building B2W_COMPLETE-Rating-Only_Order-TAG-None"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Only_Order-TAG-None -n B2W-Rating -s Train -d 300 -c 20 -l pt -g only_order -t none;

echo ">>> Building B2W_COMPLETE-Rating-Order_Circular-TAG-None"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Order_Circular-TAG-None -n B2W-Rating -s Train -d 300 -c 20 -l pt -g order_circular -t none;

echo ">>> Building B2W_COMPLETE-Rating-Binary_Tree-TAG-None"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Binary_Tree-TAG-None -n B2W-Rating -s Train -d 300 -c 20 -l pt -g binary_tree -t none;

echo ">>> Building MR-Only_Order-TAG-None"
python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-Only_Order-TAG-None -n MR -s Train -d 300 -c 20 -l en -g only_order -t none;

echo ">>> Building MR-Order_Circular-TAG-None"
python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-Order_Circular-TAG-None -n MR -s Train -d 300 -c 20 -l en -g order_circular -t none;

echo ">>> Building MR-Binary_Tree-TAG-None"
python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-Binary_Tree-TAG-None -n MR -s Train -d 300 -c 20 -l en -g binary_tree -t none;





# ------------



echo ">>> Renaming B2W_COMPLETE-Rating-Only_Order-TAG-None"
mv ../Datasets/B2W/B2W_COMPLETE-Rating-Only_Order-TAG-None/Train_B2W-Rating.txt ../Datasets/B2W/B2W_COMPLETE-Rating-Only_Order-TAG-None/B2W_COMPLETE-Rating-Only_Order-TAG-None.txt
echo ">>> Coping dataset B2W_COMPLETE-Rating-Only_Order-TAG-None"
cp -r ../Datasets/B2W/B2W_COMPLETE-Rating-Only_Order-TAG-None ../../Graph-Transformer/dataset/

echo ">>> Renaming B2W_COMPLETE-Rating-Order_Circular-TAG-None"
mv ../Datasets/B2W/B2W_COMPLETE-Rating-Order_Circular-TAG-None/Train_B2W-Rating.txt ../Datasets/B2W/B2W_COMPLETE-Rating-Order_Circular-TAG-None/B2W_COMPLETE-Rating-Order_Circular-TAG-None.txt
echo ">>> Coping dataset B2W_COMPLETE-Rating-Order_Circular-TAG-None"
cp -r ../Datasets/B2W/B2W_COMPLETE-Rating-Order_Circular-TAG-None ../../Graph-Transformer/dataset/

echo ">>> Renaming B2W_COMPLETE-Rating-Binary_Tree-TAG-None"
mv ../Datasets/B2W/B2W_COMPLETE-Rating-Binary_Tree-TAG-None/Train_B2W-Rating.txt ../Datasets/B2W/B2W_COMPLETE-Rating-Binary_Tree-TAG-None/B2W_COMPLETE-Rating-Binary_Tree-TAG-None.txt
echo ">>> Coping dataset B2W_COMPLETE-Rating-Binary_Tree-TAG-None"
cp -r ../Datasets/B2W/B2W_COMPLETE-Rating-Binary_Tree-TAG-None ../../Graph-Transformer/dataset/

echo ">>> Renaming MR-Only_Order-TAG-None"
mv ../Datasets/MR/MR-Only_Order-TAG-None/Train_MR.txt ../Datasets/MR/MR-Only_Order-TAG-None/MR-Only_Order-TAG-None.txt
echo ">>> Coping dataset MR-Only_Order-TAG-None"
cp -r ../Datasets/MR/MR-Only_Order-TAG-None ../../Graph-Transformer/dataset/

echo ">>> Renaming MR-Order_Circular-TAG-None"
mv ../Datasets/MR/MR-Order_Circular-TAG-None/Train_MR.txt ../Datasets/MR/MR-Order_Circular-TAG-None/MR-Order_Circular-TAG-None.txt
echo ">>> Coping dataset MR-Order_Circular-TAG-None"
cp -r ../Datasets/MR/MR-Order_Circular-TAG-None ../../Graph-Transformer/dataset/

echo ">>> Renaming MR-Binary_Tree-TAG-None"
mv ../Datasets/MR/MR-Binary_Tree-TAG-None/Train_MR.txt ../Datasets/MR/MR-Binary_Tree-TAG-None/MR-Binary_Tree-TAG-None.txt
echo ">>> Coping dataset MR-Binary_Tree-TAG-None"
cp -r ../Datasets/MR/MR-Binary_Tree-TAG-None ../../Graph-Transformer/dataset/

