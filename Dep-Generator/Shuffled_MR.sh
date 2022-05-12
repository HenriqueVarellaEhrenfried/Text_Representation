mkdir -p ../Datasets/MR/MR-Binary_Tree-TAG-None-S10
mkdir -p ../Datasets/MR/MR-Binary_Tree-TAG-None-S20
mkdir -p ../Datasets/MR/MR-Binary_Tree-TAG-None-S30
mkdir -p ../Datasets/MR/MR-Binary_Tree-TAG-None-S40

python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-Binary_Tree-TAG-None-S10 -n MR -s Train -d 300 -c 20 -l en -g binary_tree -t none -S 10 ;

python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-Binary_Tree-TAG-None-S20 -n MR -s Train -d 300 -c 20 -l en -g binary_tree -t none -S 20 ;

python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-Binary_Tree-TAG-None-S30 -n MR -s Train -d 300 -c 20 -l en -g binary_tree -t none -S 30 ;

python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-Binary_Tree-TAG-None-S40 -n MR -s Train -d 300 -c 20 -l en -g binary_tree -t none -S 40 ;