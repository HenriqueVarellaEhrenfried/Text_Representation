## Transform the original dataset into format Class_id.txt

SOURCE = '../Original/'
TARGET = '../ParsedV2/'

def get_file_content(file_name):
    print(file_name)
    with open(file_name, 'rb') as f:
        result = [line.rstrip() for line in f]
    return result

def save_file(file_name, content):
    with open(file_name, 'w') as f:
        f.write(content)


label_test = get_file_content(SOURCE+"label_test.txt")
text_test = get_file_content(SOURCE+"text_test.txt")

label_train = get_file_content(SOURCE+"label_train.txt")
text_train = get_file_content(SOURCE+"text_train.txt")

# The difference with V2 is that we changed the order of the labels and the texts.
labels = label_train + label_test
texts = text_train + text_test


if len(labels) != len(texts):
    print("Error: Incompatible lenghts")
    exit(1)
else:
    for i in range(0,len(texts)):
        # name = TARGET + labels[i].decode("cp1252") + "_" + str(i) + ".txt"
        name = "%s%05d_%s.txt" % (TARGET, int(i), labels[i].decode("cp1252"))
        print(">> Working with file: ", name)
        save_file(name, texts[i].decode("cp1252"))
