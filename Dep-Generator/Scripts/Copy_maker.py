OUTPUT = [
    '../Datasets/MR/MR-Default-TAG-DEP',
    '../Datasets/MR/MR-Default-TAG-POS',
    '../Datasets/MR/MR-Default-TAG-DEP-POS',
    '../Datasets/MR/MR-Default-TAG-POS-DEP',
    '../Datasets/MR/MR-Default-TAG-SQRT-PROD',
    '../Datasets/MR/MR-Order-TAG-DEP',
    '../Datasets/MR/MR-Order-TAG-POS',
    '../Datasets/MR/MR-Order-TAG-DEP-POS',
    '../Datasets/MR/MR-Order-TAG-POS-DEP',
    '../Datasets/MR/MR-Order-TAG-SQRT-PROD'
]

DL_DATASET_LOCATION = '/media/SSD/Doutorado/Doutorado/Graph-Transformer/dataset'

for out in OUTPUT:
    dataset = out.split("/")[-1]
    
    print('echo ">>> Copying %s"' % (dataset) )
    print("mv %s/*.txt %s/%s.txt" % (out, out, dataset))
    print("cp -r %s %s\n" % (out, DL_DATASET_LOCATION))


# mv ../Datasets/MR/MR-Default-TAG-Distance/Train_MR.txt ../Datasets/MR/MR-Default-TAG-Distance/MR-Default-TAG-Distance.txt
# cp -r ../Datasets/MR/MR-Default-TAG-Distance /media/SSD/Doutorado/Doutorado/Graph-Transformer/dataset

