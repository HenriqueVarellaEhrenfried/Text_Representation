# Text Representation

This repository adds code to build datasets to the UGformer deep learning model.

It consists of three directories `Datasets`, `Dep-Generator` and `Develop`

The `Datasets` directory contains the original dataset and a code to transform it into the format that the `Dep-Generator` can work. 

The `Dep-Generator` directory contains the code to transfrom the files of the dataset into the format used in the UGformer

`Develop` contains some files to help implement new funcionalities to the `Dep-Generator`.

## Format input to Dep-Generator

To build the dataset you must have a direcotory with files in the format

```
<class>_<id>.txt
```
Where `<class>` is the class of the document and `<id>` is an arbitrary number.

To execute the program, use the `main.py` program. The available flags are:

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

> IMPORTANT: Make sure that you installed the spacy model listed in the `Dep-Generator\Models used (spacy).txt` file.


## Workflow example

1. Build a Python environment (using conda/virtualenv/venv)
2. Activate this environment
3. Install the dependencies listed in the `requirements.txt`
4. In the directory `Datasets/MR` create two directories: One called `Parsed` and another called `MR-Order-Multigraph-Tag-DEP_POS`
5. Enter de directory `Datasets/MR/Code` 
6. Execute the file `Transform.py` by running `python Transform.py`
7. In the directory `Dep-Generator` run the following command: `python main.py -i ../Datasets/MR/Parsed/Train/ -o ../Datasets/MR/MR-Order-Multigraph-Tag-DEP_POS/ -n MR -s Train -d 300 -c 4 -l en -g tree_and_order_multi_graph -t dep-pos`
8. You have created the one representation format of the MR dataset

