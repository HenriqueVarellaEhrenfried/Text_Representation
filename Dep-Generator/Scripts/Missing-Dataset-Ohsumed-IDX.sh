mkdir -p ../Datasets/Ohsumed/Ohsumed-Default-Self-TAG-None
mkdir -p ../Datasets/Ohsumed/Ohsumed-Order-Self-TAG-None
mkdir -p ../Datasets/Ohsumed/Ohsumed-Order-Multigraph-Self-TAG-None
mkdir -p ../Datasets/Ohsumed/Ohsumed-Only-Order-TAG-None
mkdir -p ../Datasets/Ohsumed/Ohsumed-Order-Circular-TAG-None
mkdir -p ../Datasets/Ohsumed/Ohsumed-Binary-Tree-TAG-None

echo ">>> Building Ohsumed-Default-Self-TAG-None"
python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o ../Datasets/Ohsumed/Ohsumed-Default-Self-TAG-None -n Ohsumed -s Train -d 300 -c 20 -l en -g tree_and_self -t none;

echo ">>> Building Ohsumed-Order-Self-TAG-None"
python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o ../Datasets/Ohsumed/Ohsumed-Order-Self-TAG-None -n Ohsumed -s Train -d 300 -c 20 -l en -g tree_order_and_self -t none;

echo ">>> Building Ohsumed-Order-Multigraph-Self-TAG-None"
python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o ../Datasets/Ohsumed/Ohsumed-Order-Multigraph-Self-TAG-None -n Ohsumed -s Train -d 300 -c 20 -l en -g tree_order_multigraph_and_self -t none;

echo ">>> Building Ohsumed-Only-Order-TAG-None"
python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o ../Datasets/Ohsumed/Ohsumed-Only-Order-TAG-None -n Ohsumed -s Train -d 300 -c 20 -l en -g only_order -t none;

echo ">>> Building Ohsumed-Order-Circular-TAG-None"
python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o ../Datasets/Ohsumed/Ohsumed-Order-Circular-TAG-None -n Ohsumed -s Train -d 300 -c 20 -l en -g order_circular -t none;

echo ">>> Building Ohsumed-Binary-Tree-TAG-None"
python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o ../Datasets/Ohsumed/Ohsumed-Binary-Tree-TAG-None -n Ohsumed -s Train -d 300 -c 20 -l en -g binary_tree -t none;

