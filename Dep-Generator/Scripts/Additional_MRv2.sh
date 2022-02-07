mkdir ../Datasets/MR/MR-Default-TAG-DEP
mkdir ../Datasets/MR/MR-Default-TAG-POS
mkdir ../Datasets/MR/MR-Default-TAG-DEP-POS
mkdir ../Datasets/MR/MR-Default-TAG-POS-DEP
mkdir ../Datasets/MR/MR-Default-TAG-SQRT-PROD
mkdir ../Datasets/MR/MR-Order-TAG-DEP
mkdir ../Datasets/MR/MR-Order-TAG-POS
mkdir ../Datasets/MR/MR-Order-TAG-DEP-POS
mkdir ../Datasets/MR/MR-Order-TAG-POS-DEP
mkdir ../Datasets/MR/MR-Order-TAG-SQRT-PROD

echo ">>> [01/10] Building MR-Default-TAG-DEP"
python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-Default-TAG-DEP -n MR -s Train -d 300 -c 20 -l en -g tree_only -t dep
echo ">>> [02/10] Building MR-Default-TAG-POS"
python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-Default-TAG-POS -n MR -s Train -d 300 -c 20 -l en -g tree_only -t pos
echo ">>> [03/10] Building MR-Default-TAG-DEP-POS"
python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-Default-TAG-DEP-POS -n MR -s Train -d 300 -c 20 -l en -g tree_only -t dep-pos
echo ">>> [04/10] Building MR-Default-TAG-POS-DEP"
python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-Default-TAG-POS-DEP -n MR -s Train -d 300 -c 20 -l en -g tree_only -t pos-dep
echo ">>> [05/10] Building MR-Default-TAG-SQRT-PROD"
python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-Default-TAG-SQRT-PROD -n MR -s Train -d 300 -c 20 -l en -g tree_only -t sqrt_product
echo ">>> [06/10] Building MR-Order-TAG-DEP"
python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-Order-TAG-DEP -n MR -s Train -d 300 -c 20 -l en -g tree_and_order -t dep
echo ">>> [07/10] Building MR-Order-TAG-POS"
python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-Order-TAG-POS -n MR -s Train -d 300 -c 20 -l en -g tree_and_order -t pos
echo ">>> [08/10] Building MR-Order-TAG-DEP-POS"
python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-Order-TAG-DEP-POS -n MR -s Train -d 300 -c 20 -l en -g tree_and_order -t dep-pos
echo ">>> [09/10] Building MR-Order-TAG-POS-DEP"
python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-Order-TAG-POS-DEP -n MR -s Train -d 300 -c 20 -l en -g tree_and_order -t pos-dep
echo ">>> [10/10] Building MR-Order-TAG-SQRT-PROD"
python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-Order-TAG-SQRT-PROD -n MR -s Train -d 300 -c 20 -l en -g tree_and_order -t sqrt_product