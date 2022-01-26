# Dataset generator for the U2GNN

# Libraries
import spacy
import sys
from optparse import OptionParser

from DatasetGenerator import DatasetGenerator


SET_OPTIONS = ['Both', 'Test', 'Train']
LANGUAGES = ['en', 'pt', 'de']
GRAPH_MODE = ['tree_only', 'tree_and_order', 'tree_and_order_multi_graph', 'tree_and_self', 'tree_order_and_self', 'tree_order_multigraph_and_self']
TAG_MODE = ['none', 'dep', 'pos', 'dep-pos', 'pos-dep', 'sqrt_product', 'distance']

parser = OptionParser()
parser.add_option("-i", "--input_path", dest="input_path", help="Set input path")
parser.add_option("-o", "--output_path", dest="output_path", help="Set output path")
parser.add_option("-n", "--name", dest="name", help="Name of the dataset")
parser.add_option("-s", "--set", dest="set", help="Select between 'Test' and 'Train' dataset creation to name it correctly.")
parser.add_option("-d", "--dimension", dest="dimension", default='300', help="Select the dimension of the embeddings (DEFAULT: 300)")
parser.add_option("-c", "--cores", dest="cores",  default='1', help="Number of CPU cores to use")
parser.add_option("-l", "--language", dest="language", default="en", help="Language to load auxiliary models")
parser.add_option("-g", "--graph_mode", dest="graph_mode", default="tree_only", help="Type of graph to build")
parser.add_option("-t", "--tag_mode", dest="tag_mode", default="none", help="Type of tag for nodes")

(options, args) = parser.parse_args()

SPACY_MODEL = ""

if not(options.set in SET_OPTIONS):
    print("Unknown set (parameter of: -s / --set). Select one of the following set: 'Both', 'Test', 'Train'")
    exit(1)
if not(options.language in LANGUAGES):
    print("Unknown language (parameter of: -l / --language). Select one of the following languages:", LANGUAGES)
    exit(1)
if not(options.graph_mode in GRAPH_MODE):
    print("Unknown graph mode (parameter of: -g / --graph_mode): Select on of the following graph modes", GRAPH_MODE)
    exit(1)
if not(options.tag_mode in TAG_MODE):
    print("Unknown tag mode (parameter of: -t / --tag_mode): Select on of the following tag modes", TAG_MODE)
    exit(1)

if options.language == "en":
    SPACY_MODEL = "en_core_web_lg"
elif options.language == "pt":
    SPACY_MODEL = "pt_core_news_lg"
elif options.language == "de":
    SPACY_MODEL = "de_core_news_lg"

# Load Spacy model - It will be used for word vectors
print("Importing spacy model")
nlp = spacy.load(SPACY_MODEL)
print("Spacy model loaded")

# Initialize class
dg = DatasetGenerator(nlp, options)
# Run dataset generator
dg.generate_dataset()

## TODO: Make a way to allow the training and test dataset to be created with a single command


print("Everything done")

# python main.py -i ./Dataset/IDPT_2021/Alternative/Train_Tweets/ -o ./Output/IDPT_2021/Tweets -n IDPT_2021_Tweets -s Train -d 300 -c 20 -l pt