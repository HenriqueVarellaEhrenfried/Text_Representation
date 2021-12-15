from os import listdir
from os.path import isfile, join

DEFAULT_PATH = '../ohsumed_single_23/'
TYPE = ['test', 'training']
CLASSES = ["C%02d" % item for item in range(1,24)]
OUTPUT_PATH = '../Output-dataset/'


def get_file_content(file_name):
    print(file_name)
    with open(file_name, 'rb') as f:
        result = [line.rstrip() for line in f]
    return result

def save_file(file_name, content):
    # print(content)
    with open(file_name, 'w') as f:
        f.write(content)

i = 1
for t in TYPE:
    for c in CLASSES:
        path = DEFAULT_PATH + t + '/' + c + '/' 
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        for f in onlyfiles:
            filename = str(int(CLASSES.index(c)) + 1) + "_" + str(i) + ".txt"
            content = get_file_content(path+f)
            save_file(OUTPUT_PATH+filename, " ".join(map(str, content)))
            i += 1
            print(">> Finished workin on file [ %s ]" % filename)