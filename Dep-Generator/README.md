# How to run the Dep-Generator
## **Command**

In the directory Dep-Generator run: `python main.py [PARAMETERS]` 

### **Parameters**

```
-i OR --input_path = Set input path
-o OR --output_path = Set output path
-n OR --name = Name of the dataset
-s OR --set = Select between 'Test' and 'Train' dataset creation to name it correctly. [options='Both', 'Test', 'Train']
-d OR --dimension = Select the dimension of the embeddings [default='300']
-c OR --cores = Number of CPU cores to use [default='1']
-l OR --language = Language to load auxiliary models [default="en"] [options='en', 'pt', 'de']
-g OR --graph_mode = Type of graph to build [default="tree_only"] [options='tree_only', 'tree_and_order', 'tree_and_order_multi_graph']
-t OR --tag_mode = Type of tag for nodes [default="none"] [options='none', 'dep', 'pos', 'dep-pos', 'pos-dep', 'sqrt_product']
```

### **Example**

```
python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Order-Multigraph-Tag-DEP_POS/ -n MR -s Train -d 300 -c 4 -l en -g tree_and_order_multi_graph -t dep-pos

```
---
## **Unprocessed dataset file tree**

Each file must be in the file `class_id.txt` where `class` is a number that represents a class and `id` is the file id

### Example:
```
Dataset
├── MR
|    ├── Train
|    |     ├── class_id.txt
|    |     ├── class_id.txt
|    |     ├── class_id.txt
|    |     ├── class_id.txt
|    |     ├── ....
|    |     ├── class_id.txt
|    |     ├── class_id.txt
|    |     ├── class_id.txt
|    |     └── class_id.txt
|    └── Test
|          ├── class_id.txt
|          ├── class_id.txt
|          ├── class_id.txt
|          ├── class_id.txt
|          ├── ....
|          ├── class_id.txt
|          ├── class_id.txt
|          ├── class_id.txt
|          └── class_id.txt
.............
└── Ohsumed
     ├── Train
     |     ├── class_id.txt
     |     ├── class_id.txt
     |     ├── class_id.txt
     |     ├── class_id.txt
     |     ├── ....
     |     ├── class_id.txt
     |     ├── class_id.txt
     |     ├── class_id.txt
     |     └── class_id.txt
     └── Test
           ├── class_id.txt
           ├── class_id.txt
           ├── class_id.txt
           ├── class_id.txt
           ├── ....
           ├── class_id.txt
           ├── class_id.txt
           ├── class_id.txt
           └── class_id.txt
```
