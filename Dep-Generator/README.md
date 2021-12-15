# How to run the Dep-Generator
## **Command**

In the directory Dep-Generator run: `python main.py [PARAMETERS]` 

### **Parameters**

* **Input path (`-i` or `--input_path`):** Sets the location of the files of the unprocessed dataset
* **Output path (`-o` or `--output_path`):** Sets the location to save processed dataset
* **Name (`-n` or `--name`):** Sets the name of the file of the dataset
* **Set (`-s` or `--set`):** Sets which set is been processed to name the dataset, if both is used, you can process the training ad test sets
* **Dimension (`-d` or `--dimension`):** Sets the dimension of the word vector. The default value is 300
* **Cores (`-d` or `--cores`):** Sets the number of CPU cores to use during the processing of the dataset. Default value is 1

### **Example**

```

python main.py -i ./Example/Test -o ./Output -n Example -s Test -d 300 -c 1

```
---
## **Unprocessed dataset file tree**

Each file must be in the file `class_id.txt` where `class` is a number that represents a class and `id` is the file id

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