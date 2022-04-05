mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-None-NEW
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-None-NEW
mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-Only-Order-TAG-None-NEW


echo ">>> Building B2W_COMPLETE-Rating-Default-TAG-None-NEW"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-None-NEW -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_only -t none;


echo ">>> Building B2W_COMPLETE-Rating-Order-Self-TAG-None-NEW"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-None-NEW -n B2W-Rating -s Train -d 300 -c 20 -l pt -g tree_order_and_self -t none;

echo ">>> Building B2W_COMPLETE-Rating-Only-Order-TAG-None-NEW"
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-Only-Order-TAG-None-NEW -n B2W-Rating -s Train -d 300 -c 20 -l pt -g only_order -t none;