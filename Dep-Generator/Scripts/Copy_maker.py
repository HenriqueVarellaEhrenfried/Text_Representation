OUTPUT = ['../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-Distance', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-TAG-Distance', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-TAG-Distance', '../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-None', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-None', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-None', '../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-DEP', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-DEP', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-DEP', '../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-POS', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-POS', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-POS', '../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-DEP-POS', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-DEP-POS', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-DEP-POS', '../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-POS-DEP', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-POS-DEP', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-POS-DEP', '../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-SQRT-PROD', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-SQRT-PROD', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-SQRT-PROD', '../Datasets/B2W/B2W_COMPLETE-Rating-Default-Self-TAG-Distance', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Self-TAG-Distance', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-Multigraph-Self-TAG-Distance', '../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-DEP', '../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-POS', '../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-DEP-POS', '../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-POS-DEP', '../Datasets/B2W/B2W_COMPLETE-Rating-Default-TAG-SQRT-PROD', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-TAG-DEP', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-TAG-POS', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-TAG-DEP-POS', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-TAG-POS-DEP', '../Datasets/B2W/B2W_COMPLETE-Rating-Order-TAG-SQRT-PROD']

DL_DATASET_LOCATION = '/media/SSD/Doutorado/Doutorado/Graph-Transformer/dataset'

for out in OUTPUT:
    dataset = out.split("/")[-1]
    
    print('echo ">>> Copying %s"' % (dataset) )
    print("mv %s/Train_B2W-Rating.txt %s/%s.txt" % (out, out, dataset))
    print("cp -r %s %s\n" % (out, DL_DATASET_LOCATION))


# mv ../Datasets/MR/MR-Default-TAG-Distance/Train_MR.txt ../Datasets/MR/MR-Default-TAG-Distance/MR-Default-TAG-Distance.txt
# cp -r ../Datasets/MR/MR-Default-TAG-Distance /media/SSD/Doutorado/Doutorado/Graph-Transformer/dataset

