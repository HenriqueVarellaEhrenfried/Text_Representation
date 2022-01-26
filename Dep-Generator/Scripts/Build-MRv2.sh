# New Tag mode
mkdir ../Datasets/MR/MR-Default-TAG-Distance
mkdir ../Datasets/MR/MR-Order-TAG-Distance
mkdir ../Datasets/MR/MR-Order-Multigraph-TAG-Distance

# New Trees
mkdir ../Datasets/MR/MR-Default-Self-TAG-None
mkdir ../Datasets/MR/MR-Order-Self-TAG-None
mkdir ../Datasets/MR/MR-Order-Multigraph-Self-TAG-None

mkdir ../Datasets/MR/MR-Default-Self-TAG-DEP
mkdir ../Datasets/MR/MR-Order-Self-TAG-DEP
mkdir ../Datasets/MR/MR-Order-Multigraph-Self-TAG-DEP

mkdir ../Datasets/MR/MR-Default-Self-TAG-POS
mkdir ../Datasets/MR/MR-Order-Self-TAG-POS
mkdir ../Datasets/MR/MR-Order-Multigraph-Self-TAG-POS

mkdir ../Datasets/MR/MR-Default-Self-TAG-DEP-POS
mkdir ../Datasets/MR/MR-Order-Self-TAG-DEP-POS
mkdir ../Datasets/MR/MR-Order-Multigraph-Self-TAG-DEP-POS

mkdir ../Datasets/MR/MR-Default-Self-TAG-POS-DEP
mkdir ../Datasets/MR/MR-Order-Self-TAG-POS-DEP
mkdir ../Datasets/MR/MR-Order-Multigraph-Self-TAG-POS-DEP

mkdir ../Datasets/MR/MR-Default-Self-TAG-SQRT-PROD
mkdir ../Datasets/MR/MR-Order-Self-TAG-SQRT-PROD
mkdir ../Datasets/MR/MR-Order-Multigraph-Self-TAG-SQRT-PROD

mkdir ../Datasets/MR/MR-Default-Self-TAG-Distance
mkdir ../Datasets/MR/MR-Order-Self-TAG-Distance
mkdir ../Datasets/MR/MR-Order-Multigraph-Self-TAG-Distance


echo ">>> Building MR-Default-TAG-Distance"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Default-TAG-Distance -n MR -s Train -d 300 -c 20 -l en -g tree_only -t distance
echo ">>> Building MR-Order-TAG-Distance"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Order-TAG-Distance -n MR -s Train -d 300 -c 20 -l en -g tree_and_order -t distance
echo ">>> Building MR-Order-Multigraph-TAG-Distance"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Order-Multigraph-TAG-Distance -n MR -s Train -d 300 -c 20 -l en -g tree_and_order_multi_graph -t distance
echo ">>> Building MR-Default-Self-TAG-None"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Default-Self-TAG-None -n MR -s Train -d 300 -c 20 -l en -g tree_and_self -t none
echo ">>> Building MR-Order-Self-TAG-None"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Order-Self-TAG-None -n MR -s Train -d 300 -c 20 -l en -g tree_order_and_self -t none
echo ">>> Building MR-Order-Multigraph-Self-TAG-None"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Order-Multigraph-Self-TAG-None -n MR -s Train -d 300 -c 20 -l en -g tree_order_multigraph_and_self -t none
echo ">>> Building MR-Default-Self-TAG-DEP"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Default-Self-TAG-DEP -n MR -s Train -d 300 -c 20 -l en -g tree_and_self -t dep
echo ">>> Building MR-Order-Self-TAG-DEP"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Order-Self-TAG-DEP -n MR -s Train -d 300 -c 20 -l en -g tree_order_and_self -t dep
echo ">>> Building MR-Order-Multigraph-Self-TAG-DEP"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Order-Multigraph-Self-TAG-DEP -n MR -s Train -d 300 -c 20 -l en -g tree_order_multigraph_and_self -t dep
echo ">>> Building MR-Default-Self-TAG-POS"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Default-Self-TAG-POS -n MR -s Train -d 300 -c 20 -l en -g tree_and_self -t pos
echo ">>> Building MR-Order-Self-TAG-POS"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Order-Self-TAG-POS -n MR -s Train -d 300 -c 20 -l en -g tree_order_and_self -t pos
echo ">>> Building MR-Order-Multigraph-Self-TAG-POS"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Order-Multigraph-Self-TAG-POS -n MR -s Train -d 300 -c 20 -l en -g tree_order_multigraph_and_self -t pos
echo ">>> Building MR-Default-Self-TAG-DEP-POS"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Default-Self-TAG-DEP-POS -n MR -s Train -d 300 -c 20 -l en -g tree_and_self -t dep-pos
echo ">>> Building MR-Order-Self-TAG-DEP-POS"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Order-Self-TAG-DEP-POS -n MR -s Train -d 300 -c 20 -l en -g tree_order_and_self -t dep-pos
echo ">>> Building MR-Order-Multigraph-Self-TAG-DEP-POS"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Order-Multigraph-Self-TAG-DEP-POS -n MR -s Train -d 300 -c 20 -l en -g tree_order_multigraph_and_self -t dep-pos
echo ">>> Building MR-Default-Self-TAG-POS-DEP"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Default-Self-TAG-POS-DEP -n MR -s Train -d 300 -c 20 -l en -g tree_and_self -t pos-dep
echo ">>> Building MR-Order-Self-TAG-POS-DEP"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Order-Self-TAG-POS-DEP -n MR -s Train -d 300 -c 20 -l en -g tree_order_and_self -t pos-dep
echo ">>> Building MR-Order-Multigraph-Self-TAG-POS-DEP"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Order-Multigraph-Self-TAG-POS-DEP -n MR -s Train -d 300 -c 20 -l en -g tree_order_multigraph_and_self -t pos-dep
echo ">>> Building MR-Default-Self-TAG-SQRT-PROD"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Default-Self-TAG-SQRT-PROD -n MR -s Train -d 300 -c 20 -l en -g tree_and_self -t sqrt_product
echo ">>> Building MR-Order-Self-TAG-SQRT-PROD"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Order-Self-TAG-SQRT-PROD -n MR -s Train -d 300 -c 20 -l en -g tree_order_and_self -t sqrt_product
echo ">>> Building MR-Order-Multigraph-Self-TAG-SQRT-PROD"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Order-Multigraph-Self-TAG-SQRT-PROD -n MR -s Train -d 300 -c 20 -l en -g tree_order_multigraph_and_self -t sqrt_product
echo ">>> Building MR-Default-Self-TAG-Distance"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Default-Self-TAG-Distance -n MR -s Train -d 300 -c 20 -l en -g tree_and_self -t distance
echo ">>> Building MR-Order-Self-TAG-Distance"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Order-Self-TAG-Distance -n MR -s Train -d 300 -c 20 -l en -g tree_order_and_self -t distance
echo ">>> Building MR-Order-Multigraph-Self-TAG-Distance"
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Order-Multigraph-Self-TAG-Distance -n MR -s Train -d 300 -c 20 -l en -g tree_order_multigraph_and_self -t distance