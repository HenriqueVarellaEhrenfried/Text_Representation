mkdir -p ../Datasets/10kGNAD-DE/10kGNAD-DE-Default-Self-TAG-None
mkdir -p ../Datasets/10kGNAD-DE/10kGNAD-DE-Order-Self-TAG-None
mkdir -p ../Datasets/10kGNAD-DE/10kGNAD-DE-Order-Multigraph-Self-TAG-None
mkdir -p ../Datasets/10kGNAD-DE/10kGNAD-DE-Only-Order-TAG-None
mkdir -p ../Datasets/10kGNAD-DE/10kGNAD-DE-Order-Circular-TAG-None
mkdir -p ../Datasets/10kGNAD-DE/10kGNAD-DE-Binary-Tree-TAG-None

echo ">>> Building 10kGNAD-DE-Default-Self-TAG-None"
python main.py -i ../Datasets/10kGNAD-DE/Parsed/ -o ../Datasets/10kGNAD-DE/10kGNAD-DE-Default-Self-TAG-None -n 10kGNAD-DE -s Train -d 300 -c 1 -l de -g tree_and_self -t none;

echo ">>> Building 10kGNAD-DE-Order-Self-TAG-None"
python main.py -i ../Datasets/10kGNAD-DE/Parsed/ -o ../Datasets/10kGNAD-DE/10kGNAD-DE-Order-Self-TAG-None -n 10kGNAD-DE -s Train -d 300 -c 1 -l de -g tree_order_and_self -t none;

echo ">>> Building 10kGNAD-DE-Order-Multigraph-Self-TAG-None"
python main.py -i ../Datasets/10kGNAD-DE/Parsed/ -o ../Datasets/10kGNAD-DE/10kGNAD-DE-Order-Multigraph-Self-TAG-None -n 10kGNAD-DE -s Train -d 300 -c 1 -l de -g tree_order_multigraph_and_self -t none;

echo ">>> Building 10kGNAD-DE-Only-Order-TAG-None"
python main.py -i ../Datasets/10kGNAD-DE/Parsed/ -o ../Datasets/10kGNAD-DE/10kGNAD-DE-Only-Order-TAG-None -n 10kGNAD-DE -s Train -d 300 -c 1 -l de -g only_order -t none;

echo ">>> Building 10kGNAD-DE-Order-Circular-TAG-None"
python main.py -i ../Datasets/10kGNAD-DE/Parsed/ -o ../Datasets/10kGNAD-DE/10kGNAD-DE-Order-Circular-TAG-None -n 10kGNAD-DE -s Train -d 300 -c 1 -l de -g order_circular -t none;

echo ">>> Building 10kGNAD-DE-Binary-Tree-TAG-None"
python main.py -i ../Datasets/10kGNAD-DE/Parsed/ -o ../Datasets/10kGNAD-DE/10kGNAD-DE-Binary-Tree-TAG-None -n 10kGNAD-DE -s Train -d 300 -c 1 -l de -g binary_tree -t none;

