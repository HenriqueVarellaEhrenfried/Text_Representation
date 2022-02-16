mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-Distance
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Order-TAG-Distance
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-TAG-Distance
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-None
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-None
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-None
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-DEP
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-DEP
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-DEP
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-POS
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-POS
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-POS
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-DEP-POS
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-DEP-POS
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-DEP-POS
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-POS-DEP
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-POS-DEP
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-POS-DEP
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-SQRT-PROD
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-SQRT-PROD
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-SQRT-PROD
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-Distance
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-Distance
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-Distance
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-DEP
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-POS
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-DEP-POS
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-POS-DEP
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-SQRT-PROD
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Order-TAG-DEP
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Order-TAG-POS
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Order-TAG-DEP-POS
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Order-TAG-POS-DEP
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Order-TAG-SQRT-PROD


echo ">>> Building B2W_COMPLETE-Rating-Default-TAG-Distance"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-Distance -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_only -t distance;

echo ">>> Building B2W_COMPLETE-Rating-Order-TAG-Distance"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Order-TAG-Distance -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_and_order -t distance;

echo ">>> Building B2W_COMPLETE-Rating-Order-Multigraph-TAG-Distance"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-TAG-Distance -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_and_order_multi_graph -t distance;

echo ">>> Building B2W_COMPLETE-Rating-Default-Self-TAG-None"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-None -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_and_self -t none;

echo ">>> Building B2W_COMPLETE-Rating-Order-Self-TAG-None"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-None -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_order_and_self -t none;

echo ">>> Building B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-None"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-None -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_order_multigraph_and_self -t none;

echo ">>> Building B2W_COMPLETE-Rating-Default-Self-TAG-DEP"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-DEP -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_and_self -t dep;

echo ">>> Building B2W_COMPLETE-Rating-Order-Self-TAG-DEP"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-DEP -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_order_and_self -t dep;

echo ">>> Building B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-DEP"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-DEP -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_order_multigraph_and_self -t dep;

echo ">>> Building B2W_COMPLETE-Rating-Default-Self-TAG-POS"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-POS -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_and_self -t pos;

echo ">>> Building B2W_COMPLETE-Rating-Order-Self-TAG-POS"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-POS -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_order_and_self -t pos;

echo ">>> Building B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-POS"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-POS -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_order_multigraph_and_self -t pos;

echo ">>> Building B2W_COMPLETE-Rating-Default-Self-TAG-DEP-POS"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-DEP-POS -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_and_self -t dep-pos;

echo ">>> Building B2W_COMPLETE-Rating-Order-Self-TAG-DEP-POS"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-DEP-POS -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_order_and_self -t dep-pos;

echo ">>> Building B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-DEP-POS"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-DEP-POS -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_order_multigraph_and_self -t dep-pos;

echo ">>> Building B2W_COMPLETE-Rating-Default-Self-TAG-POS-DEP"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-POS-DEP -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_and_self -t pos-dep;

echo ">>> Building B2W_COMPLETE-Rating-Order-Self-TAG-POS-DEP"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-POS-DEP -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_order_and_self -t pos-dep;

echo ">>> Building B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-POS-DEP"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-POS-DEP -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_order_multigraph_and_self -t pos-dep;

echo ">>> Building B2W_COMPLETE-Rating-Default-Self-TAG-SQRT-PROD"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-SQRT-PROD -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_and_self -t sqrt_product;

echo ">>> Building B2W_COMPLETE-Rating-Order-Self-TAG-SQRT-PROD"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-SQRT-PROD -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_order_and_self -t sqrt_product;

echo ">>> Building B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-SQRT-PROD"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-SQRT-PROD -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_order_multigraph_and_self -t sqrt_product;

echo ">>> Building B2W_COMPLETE-Rating-Default-Self-TAG-Distance"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-Distance -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_and_self -t distance;

echo ">>> Building B2W_COMPLETE-Rating-Order-Self-TAG-Distance"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-Distance -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_order_and_self -t distance;

echo ">>> Building B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-Distance"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-Distance -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_order_multigraph_and_self -t distance;

echo ">>> Building B2W_COMPLETE-Rating-Default-TAG-DEP"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-DEP -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_only -t dep;

echo ">>> Building B2W_COMPLETE-Rating-Default-TAG-POS"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-POS -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_only -t pos;

echo ">>> Building B2W_COMPLETE-Rating-Default-TAG-DEP-POS"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-DEP-POS -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_only -t dep-pos;

echo ">>> Building B2W_COMPLETE-Rating-Default-TAG-POS-DEP"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-POS-DEP -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_only -t pos-dep;

echo ">>> Building B2W_COMPLETE-Rating-Default-TAG-SQRT-PROD"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-SQRT-PROD -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_only -t sqrt_product;

echo ">>> Building B2W_COMPLETE-Rating-Order-TAG-DEP"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Order-TAG-DEP -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_and_order -t dep;

echo ">>> Building B2W_COMPLETE-Rating-Order-TAG-POS"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Order-TAG-POS -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_and_order -t pos;

echo ">>> Building B2W_COMPLETE-Rating-Order-TAG-DEP-POS"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Order-TAG-DEP-POS -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_and_order -t dep-pos;

echo ">>> Building B2W_COMPLETE-Rating-Order-TAG-POS-DEP"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Order-TAG-POS-DEP -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_and_order -t pos-dep;

echo ">>> Building B2W_COMPLETE-Rating-Order-TAG-SQRT-PROD"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Order-TAG-SQRT-PROD -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_and_order -t sqrt_product;

