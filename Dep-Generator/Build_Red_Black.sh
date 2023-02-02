echo "Create Outupu directory..."

mkdir -p ../Datasets/MR/MR-RedBlack_Tree-TAG-None
mkdir -p ../Datasets/MR/MR-RedBlack_Tree-TAG-None-SH10
mkdir -p ../Datasets/MR/MR-RedBlack_Tree-TAG-None-SH20
mkdir -p ../Datasets/MR/MR-RedBlack_Tree-TAG-None-SH30
mkdir -p ../Datasets/MR/MR-RedBlack_Tree-TAG-None-SH40

mkdir -p ../Datasets/Ohsumed/Ohsumed-RedBlack-Tree-TAG-None
mkdir -p ../Datasets/Ohsumed/Ohsumed-RedBlack-Tree-TAG-None-SH10
mkdir -p ../Datasets/Ohsumed/Ohsumed-RedBlack-Tree-TAG-None-SH20
mkdir -p ../Datasets/Ohsumed/Ohsumed-RedBlack-Tree-TAG-None-SH30
mkdir -p ../Datasets/Ohsumed/Ohsumed-RedBlack-Tree-TAG-None-SH40

echo "Build datasets..."

python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-RedBlack_Tree-TAG-None -n MR -s Train -d 300 -c 20 -l en -g red_black_tree -t none;
python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-RedBlack_Tree-TAG-None-SH10 -n MR -s Train -d 300 -c 20 -l en -g red_black_tree -t none -S 10 ;
python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-RedBlack_Tree-TAG-None-SH20 -n MR -s Train -d 300 -c 20 -l en -g red_black_tree -t none -S 20 ;
python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-RedBlack_Tree-TAG-None-SH30 -n MR -s Train -d 300 -c 20 -l en -g red_black_tree -t none -S 30 ;
python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-RedBlack_Tree-TAG-None-SH40 -n MR -s Train -d 300 -c 20 -l en -g red_black_tree -t none -S 40 ;


python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o ../Datasets/Ohsumed/Ohsumed-RedBlack-Tree-TAG-None -n Ohsumed -s Train -d 300 -c 20 -l en -g red_black_tree -t none;
python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o ../Datasets/Ohsumed/Ohsumed-RedBlack-Tree-TAG-None-SH10 -n Ohsumed -s Train -d 300 -c 20 -l en -g red_black_tree -t none -S 10;
python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o ../Datasets/Ohsumed/Ohsumed-RedBlack-Tree-TAG-None-SH20 -n Ohsumed -s Train -d 300 -c 20 -l en -g red_black_tree -t none -S 20;
python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o ../Datasets/Ohsumed/Ohsumed-RedBlack-Tree-TAG-None-SH30 -n Ohsumed -s Train -d 300 -c 20 -l en -g red_black_tree -t none -S 30;
python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o ../Datasets/Ohsumed/Ohsumed-RedBlack-Tree-TAG-None-SH40 -n Ohsumed -s Train -d 300 -c 20 -l en -g red_black_tree -t none -S 40;


echo "Renaming Files..."
mv ../Datasets/MR/MR-RedBlack_Tree-TAG-None/Train_MR.txt      ../Datasets/MR/MR-RedBlack_Tree-TAG-None/MR-RedBlack_Tree-TAG-None.txt 
mv ../Datasets/MR/MR-RedBlack_Tree-TAG-None-SH10/Train_MR.txt ../Datasets/MR/MR-RedBlack_Tree-TAG-None-SH10/MR-RedBlack_Tree-TAG-None-SH10.txt 
mv ../Datasets/MR/MR-RedBlack_Tree-TAG-None-SH20/Train_MR.txt ../Datasets/MR/MR-RedBlack_Tree-TAG-None-SH20/MR-RedBlack_Tree-TAG-None-SH20.txt 
mv ../Datasets/MR/MR-RedBlack_Tree-TAG-None-SH30/Train_MR.txt ../Datasets/MR/MR-RedBlack_Tree-TAG-None-SH30/MR-RedBlack_Tree-TAG-None-SH30.txt 
mv ../Datasets/MR/MR-RedBlack_Tree-TAG-None-SH40/Train_MR.txt ../Datasets/MR/MR-RedBlack_Tree-TAG-None-SH40/MR-RedBlack_Tree-TAG-None-SH40.txt 

mv ../Datasets/Ohsumed/Ohsumed-RedBlack-Tree-TAG-None/Train_Ohsumed.txt ../Datasets/Ohsumed/Ohsumed-RedBlack-Tree-TAG-None/Ohsumed-RedBlack-Tree-TAG-None.txt
mv ../Datasets/Ohsumed/Ohsumed-RedBlack-Tree-TAG-None-SH10/Train_Ohsumed.txt ../Datasets/Ohsumed/Ohsumed-RedBlack-Tree-TAG-None-SH10/Ohsumed-RedBlack-Tree-TAG-None-SH10.txt
mv ../Datasets/Ohsumed/Ohsumed-RedBlack-Tree-TAG-None-SH20/Train_Ohsumed.txt ../Datasets/Ohsumed/Ohsumed-RedBlack-Tree-TAG-None-SH20/Ohsumed-RedBlack-Tree-TAG-None-SH20.txt
mv ../Datasets/Ohsumed/Ohsumed-RedBlack-Tree-TAG-None-SH30/Train_Ohsumed.txt ../Datasets/Ohsumed/Ohsumed-RedBlack-Tree-TAG-None-SH30/Ohsumed-RedBlack-Tree-TAG-None-SH30.txt
mv ../Datasets/Ohsumed/Ohsumed-RedBlack-Tree-TAG-None-SH40/Train_Ohsumed.txt ../Datasets/Ohsumed/Ohsumed-RedBlack-Tree-TAG-None-SH40/Ohsumed-RedBlack-Tree-TAG-None-SH40.txt


echo "Script finished"
