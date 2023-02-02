# mkdir -p ../Datasets/MR/MR-AVL_Tree-TAG-None
# mkdir -p ../Datasets/MR/MR-AVL_Tree-TAG-None-SH10
# mkdir -p ../Datasets/MR/MR-AVL_Tree-TAG-None-SH20
# mkdir -p ../Datasets/MR/MR-AVL_Tree-TAG-None-SH30
# mkdir -p ../Datasets/MR/MR-AVL_Tree-TAG-None-SH40

# mkdir -p ../Datasets/Ohsumed/Ohsumed-AVL-Tree-TAG-None
# mkdir -p ../Datasets/Ohsumed/Ohsumed-AVL-Tree-TAG-None-SH10
# mkdir -p ../Datasets/Ohsumed/Ohsumed-AVL-Tree-TAG-None-SH20
# mkdir -p ../Datasets/Ohsumed/Ohsumed-AVL-Tree-TAG-None-SH30
# mkdir -p ../Datasets/Ohsumed/Ohsumed-AVL-Tree-TAG-None-SH40


mkdir -p ../Datasets/B2W/B2W-RedBlack_Tree-TAG-None
mkdir -p ../Datasets/10kGNAD-DE/10kGNAD-RedBlack_Tree-Tag-None


# python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-AVL_Tree-TAG-None -n MR -s Train -d 300 -c 20 -l en -g avl_tree -t none;
# python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-AVL_Tree-TAG-None-SH10 -n MR -s Train -d 300 -c 20 -l en -g avl_tree -t none -S 10 ;
# python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-AVL_Tree-TAG-None-SH20 -n MR -s Train -d 300 -c 20 -l en -g avl_tree -t none -S 20 ;
# python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-AVL_Tree-TAG-None-SH30 -n MR -s Train -d 300 -c 20 -l en -g avl_tree -t none -S 30 ;
# python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-AVL_Tree-TAG-None-SH40 -n MR -s Train -d 300 -c 20 -l en -g avl_tree -t none -S 40 ;


# python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o ../Datasets/Ohsumed/Ohsumed-AVL-Tree-TAG-None -n Ohsumed -s Train -d 300 -c 20 -l en -g avl_tree -t none;
# python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o ../Datasets/Ohsumed/Ohsumed-AVL-Tree-TAG-None-SH10 -n Ohsumed -s Train -d 300 -c 20 -l en -g avl_tree -t none -S 10;
# python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o ../Datasets/Ohsumed/Ohsumed-AVL-Tree-TAG-None-SH20 -n Ohsumed -s Train -d 300 -c 20 -l en -g avl_tree -t none -S 20;
# python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o ../Datasets/Ohsumed/Ohsumed-AVL-Tree-TAG-None-SH30 -n Ohsumed -s Train -d 300 -c 20 -l en -g avl_tree -t none -S 30;
# python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o ../Datasets/Ohsumed/Ohsumed-AVL-Tree-TAG-None-SH40 -n Ohsumed -s Train -d 300 -c 20 -l en -g avl_tree -t none -S 40;




python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W-RedBlack_Tree-TAG-None -n B2W-Rating -s Train -d 300 -c 20 -l pt -g red_black_tree -t none;

python main.py -i ../Datasets/10kGNAD-DE/Parsed/ -o ../Datasets/10kGNAD-DE/10kGNAD-RedBlack_Tree-Tag-None -n 10kGNAD-DE -s Train -d 300 -c 20 -l de -g red_black_tree -t none;
