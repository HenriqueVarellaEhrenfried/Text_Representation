## Transform the original dataset into format Class_id.txt

# Useful links:
# https://tblock.github.io/10kGNAD/
# https://ofai.github.io/million-post-corpus/
# https://github.com/tblock/10kGNAD

SOURCE = '../articles.csv'
TARGET = '../Parsed/'

def get_file_content(file_name):
    with open(file_name, 'r') as f:
        result = [line.rstrip().split(';')  for line in f]
    return result

def save_file(file_name, content):
    with open(file_name, 'w') as f:
        f.write(content)

def get_classes(content):
    classes = []
    counter = {}
    for c in content:
        classes.append(c[0])
        if c[0] not in counter:
            counter[c[0]] = 1
        else:
            counter[c[0]] += 1

    return(list(set(classes)), counter)


all_lines = get_file_content(SOURCE)
classes, counter = get_classes(all_lines)


for i in range(0,len(all_lines)):
    text_class = classes.index(all_lines[i][0])
    content = all_lines[i][1]
    name = TARGET + str(text_class) + "_" + str(i) + ".txt"
    print(">> Working with file: ", name)
    save_file(name, content)

print("Available classes: ", classes)
print("Counter of classes: ", counter)


# Available classes:  ['International', 'Sport', 'Panorama', 'Etat', 'Wirtschaft', 'Wissenschaft', 'Web', 'Inland', 'Kultur']
# Counter of classes:  {'Etat': 668, 'Inland': 1015, 'International': 1511, 'Kultur': 539, 'Panorama': 1678, 'Sport': 1201, 'Web': 1677, 'Wirtschaft': 1411, 'Wissenschaft': 573}