import random
from shutil import copy

def select_files():
    INPUT_PATH = "./Dataset/Irony_pt/AllFiles.txt"

    with open(INPUT_PATH, "r") as f:
        all_files = [line.rstrip().split(" ")[-1] for line in f]

    random.shuffle(all_files)

    n = random.randint(0,len(all_files)-1)

    file_list = []
    selected_index = []

    for _ in range(0,2700):

        while True:
            n = random.randint(0,len(all_files)-1)
            if not(n in selected_index):
                break

  
        selected_index.append(n)
        file_list.append(all_files[n])

    return file_list

def copy_files(selected_files):
    ORIGINAL_BASE_PATH = "./Dataset/Irony_pt/Train/"
    NEW_BASE_PATH = "./Dataset/Irony_pt/Balanced_Dataset_Train/"

    for sf in selected_files:
        copy(ORIGINAL_BASE_PATH + sf, NEW_BASE_PATH + sf)
        




selected_files = select_files()
copy_files(selected_files)