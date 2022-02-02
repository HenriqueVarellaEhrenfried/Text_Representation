import glob
import multiprocessing as mp
import pandas as pd
import os
import random
from datetime import datetime
import math

import fasttext
import fasttext.util

class DatasetGenerator():
    def __init__(self, nlp, options):
        # Parameters passed
        self.nlp = nlp
        self.input = options.input_path
        self.output = options.output_path + "/" if options.output_path[-1] != "/" else options.output_path 
        self.name = options.name 
        self.set = options.set 
        self.cores = int(options.cores)
        self.dimension = int(options.dimension)
        self.language = options.language
        self.graph_mode = options.graph_mode
        self.tag_mode = options.tag_mode

        # TAG SECTION
        #  PT MODEL = No component 'tagger' found in pipeline. Available names: ['tok2vec', 'morphologizer', 'parser', 'senter', 'attribute_ruler', 'lemmatizer', 'ner']
        if options.language == "en":
            self.pos_types = list(nlp.get_pipe("tagger").labels)
            self.pos_types.append('_SP')
        if options.language == "de":
            self.pos_types = list(nlp.get_pipe("tagger").labels)
        elif options.language == "pt":
            self.pos_types = ['ADP', 'VERB', 'AUX', 'DET', 'X', 'INTJ', 'NUM', 'SCONJ', 'PROPN', 'CCONJ', 'NOUN', 'ADJ', 'SYM', 'PUNCT', 'PRON', 'PART', 'ADV']
            
        self.dep_types = list(nlp.get_pipe("parser").labels)       

        # Helper for distances 
        self.combinations = self.combine(list(range(0,len(self.dep_types))),list(range(0,len(self.pos_types))))
        self.distances = self.calculate_all_distances(self.combinations)
        self.distances_sorted = sorted(self.distances)

        # States
        self.all_graphs = None
        self.word_vectors = None
        self.files = self.read_files()
        self.final_dataset = []

        # Funcion Initialize
        self.load_fasttext()

###############################################################################
############################## AUXYLIARY METHODS ##############################
###############################################################################
   # Word to vector methods

    def load_fasttext(self):
        # English - Download model if it does not exist
        fasttext.util.download_model(self.language, if_exists='ignore')
        
        model_to_load = 'cc.' + self.language + ".300.bin"

        # Load the model
        self.word_vectors = fasttext.load_model(model_to_load)
        
        # Change its dimension
        if  self.dimension != 300:
            fasttext.util.reduce_model(self.word_vectors, self.dimension)
        
        return self.word_vectors
    
    def get_vector(self, raw_word):
        word = raw_word.lower()
        return self.word_vectors.get_word_vector(word)
  
###############################################################################
    # Useful methods

    def timestamp(self):
        now = datetime.now()
        return now.strftime("[%d/%m/%Y %H:%M:%S] ")

    def read_files(self):
        print(">> Reading files from:", self.input)
        return glob.glob(self.input + "*.txt")

    def get_ranges(self, array, number):
        ranges = []
        print(">> There are", len(array), "itens to process")
        for _ in range(0, number):
            step = len(array)/number
            if ranges:
                a = int(ranges[-1])
                b = int(a + step)
                ranges.append(a)
                ranges.append(b)
            else:
                a = int(0)
                b = int(a + step)
                ranges.append(a)
                ranges.append(b) 
        # Observe that the last range is bigger to acoomodate missing jobs
        ranges[-1] = ranges[-1] + (len(array) - ranges[-1]) 
        return ranges

    def separe_sentences(self, doc):
        aux = []
        sentences = []
        for token in doc:
            aux.append(token)
            # if token.text in [".", "!", "?"] :
            #     sentences.append(aux)
            #     aux = []

        # If the last sentece does not finish with punctuation    
        if len(aux) > 0:
            sentences.append(aux)

        return sentences

    def distance(self, xa, xb, ya, yb):
        x = (xb - xa) ** 2
        y = (yb - ya) ** 2
        s = x + y 
        d = s ** 0.5
        return d 

    def combine(self, set1, set2):
        combinations = []
        for s1 in set1:
            for s2 in set2:
                combinations.append([s1,s2])
        return combinations

    def calculate_all_distances(self, combinations):
        distances = []

        for i in range(0,len(combinations)):
            comb = combinations[i]
            # Calculate distance of the point to the orgin
            distances1 = self.distance(0,(comb[0]),0,(comb[1]))
            # Calculate distance to the point above (max(X)+1, max(Y)+1)
            distances2 = self.distance((combinations[-1][0])+1,(comb[0]),(combinations[-1][1])+1,(comb[1]))
            # Calculate difference between the distances
            distances.append(distances1-distances2)
        return distances

    def list_neighbors(self, sentence,current_token, num_tokens, neighbors):
        if current_token+1 != num_tokens:
            linear_neighbor = sentence[current_token+1]
        else:
            return list(neighbors)
        return list(set(list(neighbors) + [linear_neighbor]))

    def list_neighbors_multi_graph(self, sentence,current_token, num_tokens, neighbors):
        if current_token+1 != num_tokens:
            linear_neighbor = sentence[current_token+1]
        else:
            return list(neighbors)
        return list(list(neighbors) + [linear_neighbor])

    def handle_neighbors_tree_and_order_multi_graph(self, sentence):
        token_number = 0
        num_tokens = len(sentence)
        result = []
        for token in sentence:            
            token_children = self.list_neighbors_multi_graph(sentence, token_number, num_tokens, token.children)           
            number_neighbors = len(list(token_children))
            i = 0
            NEIGHBORS = ""           
            for child in token_children:
                if i + 1 == number_neighbors:
                    NEIGHBORS = NEIGHBORS + str(child.i)
                else:
                    NEIGHBORS = NEIGHBORS + str(child.i) + " "
                i += 1
            token_number +=1
            result.append(NEIGHBORS)
        return result


    def handle_neighbors_tree_and_order(self, sentence):
        # This Funciont parses the text using the sPacy and build the neighbors from it. Additionaly, it 
        # inserts reading notation (not multigraph) - This means that if there is an edge to a node that
        # occurs natually from the parsing, a new edge will not be added.
        token_number = 0
        num_tokens = len(sentence)
        result = []
        
        for token in sentence:            
            token_children = self.list_neighbors(sentence, token_number, num_tokens, token.children)           
            number_neighbors = len(list(token_children))
            i = 0
            NEIGHBORS = ""           
            for child in token_children:
                if i + 1 == number_neighbors:
                    NEIGHBORS = NEIGHBORS + str(child.i)
                else:
                    NEIGHBORS = NEIGHBORS + str(child.i) + " "
                i += 1
            token_number +=1
            result.append(NEIGHBORS)
        return result

    def handle_neighbors_tree_only(self, sentence):
        # This Funciont parses the text using the sPacy and build the neighbors from it
        token_number = 0
        num_tokens = len(sentence)
        result = []

        for token in sentence:            
            token_children = list(token.children)
            number_neighbors = len(list(token_children))
            i = 0
            NEIGHBORS = ""           
            for child in token_children:
                if i + 1 == number_neighbors:
                    NEIGHBORS = NEIGHBORS + str(child.i)
                else:
                    NEIGHBORS = NEIGHBORS + str(child.i) + " "
                i += 1
            token_number +=1
            result.append(NEIGHBORS)
        return result

    def handle_neighbors_tree_and_self(self, sentence):
        token_number = 0
        num_tokens = len(sentence)
        result = []
        for token in sentence:            
            token_children = list(token.children)
            token_children.append(token) # Add self-loop
            number_neighbors = len(list(token_children))
            i = 0
            NEIGHBORS = ""           
            for child in token_children:
                if i + 1 == number_neighbors:
                    NEIGHBORS = NEIGHBORS + str(child.i)
                else:
                    NEIGHBORS = NEIGHBORS + str(child.i) + " "
                i += 1
            token_number +=1
            result.append(NEIGHBORS)
        return result

    def handle_neighbors_tree_order_and_self(self, sentence):
        token_number = 0
        num_tokens = len(sentence)
        result = []
        for token in sentence:            
            token_children = self.list_neighbors(sentence, token_number, num_tokens, token.children)   
            token_children.append(token) # Add self-loop        
            number_neighbors = len(list(token_children))
            i = 0
            NEIGHBORS = ""           
            for child in token_children:
                if i + 1 == number_neighbors:
                    NEIGHBORS = NEIGHBORS + str(child.i)
                else:
                    NEIGHBORS = NEIGHBORS + str(child.i) + " "
                i += 1
            token_number +=1
            result.append(NEIGHBORS)
        return result    

    def handle_neighbors_tree_order_multigraph_and_self(self, sentence):
        token_number = 0
        num_tokens = len(sentence)
        result = []
        for token in sentence:            
            token_children = self.list_neighbors_multi_graph(sentence, token_number, num_tokens, token.children) 
            token_children.append(token) # Add self-loop           
            number_neighbors = len(list(token_children))
            i = 0
            NEIGHBORS = ""           
            for child in token_children:
                if i + 1 == number_neighbors:
                    NEIGHBORS = NEIGHBORS + str(child.i)
                else:
                    NEIGHBORS = NEIGHBORS + str(child.i) + " "
                i += 1
            token_number +=1
            result.append(NEIGHBORS)
        return result

    def POS_as_tag(self, token):
        index = self.pos_types.index(token.tag_) if token.tag_ in self.pos_types else 99
        return index

    def DEP_as_tag(self, token):
        index = self.dep_types.index(token.dep_) if token.dep_ in self.dep_types else 99
        return index

    def composition_as_tag(self, token):
        dep = self.dep_types.index(token.dep_) if token.dep_ in self.dep_types else 99
        pos = self.pos_types.index(token.tag_) if token.tag_ in self.pos_types else 99
        
        composition = (dep * 100) + pos
        return composition

    def composition_as_tag_inverted(self, token):
        dep = self.dep_types.index(token.dep_) if token.dep_ in self.dep_types else 99
        pos = self.pos_types.index(token.tag_) if token.tag_ in self.pos_types else 99
        
        composition = (pos * 100) + dep
        return composition

    def sqrt_of_product_node_tag(self, token):
        dep = self.dep_types.index(token.dep_) if token.dep_ in self.dep_types else 99
        pos = self.pos_types.index(token.tag_) if token.tag_ in self.pos_types else 99
        
        composition = math.ceil((dep*pos)**1/2)
        return composition

    def distance_as_tag(self, token):
        def calculate_distance(limit, x, y):
            # Calculate distance of the point to the orgin
            d1 = self.distance(0,x,0,y)
            # Calculate distance to the point above (max(X)+1, max(Y)+1)
            d2 = self.distance(limit[0]+1,x,limit[1]+1,y)
            # Calculate difference between the distances
            d = d1 - d2

            return d
        
        dep = self.dep_types.index(token.dep_)
        pos = self.pos_types.index(token.tag_)
    
        tag = self.distances_sorted.index(calculate_distance([len(self.dep_types)-1,len(self.pos_types)-1],dep,pos))
        return tag

    def build_nodes(self, sentences):
        # This method must generate the following line:
        # [t (tag)] [m (number of neighbors)] [EACH_NEIGHBOR_NUMBER] [d (node features)]
        ROOT_NAME = "@#|ROOT|#@"
        sentence_parsed = []
        root_children = []
        for sentence in sentences:
            if self.graph_mode == "tree_only":
                parcial_neighbor = self.handle_neighbors_tree_only(sentence)
            elif self.graph_mode == "tree_and_order":
                parcial_neighbor = self.handle_neighbors_tree_and_order(sentence)
            elif self.graph_mode == "tree_and_order_multi_graph":
                parcial_neighbor = self.handle_neighbors_tree_and_order_multi_graph(sentence)
                #### New Addition (After NAACL 2022 Submission) ####
            elif self.graph_mode == "tree_and_self":
                parcial_neighbor = self.handle_neighbors_tree_and_self(sentence)
            elif self.graph_mode == "tree_order_and_self":
                parcial_neighbor = self.handle_neighbors_tree_order_and_self(sentence)
            elif self.graph_mode == "tree_order_multigraph_and_self":
                parcial_neighbor = self.handle_neighbors_tree_order_multigraph_and_self(sentence)

            i = 0
            for token in sentence:
                number_neighbors = len(list(token.children))

                if token.dep_ == "ROOT":
                    # Save the root children to create the root node at the end of the process
                    root_children.append(token.i)

                if self.tag_mode == "none":
                    TAG = "0"
                elif self.tag_mode == "dep":
                    TAG = str(self.DEP_as_tag(token))
                elif self.tag_mode == "pos":
                    TAG = str(self.POS_as_tag(token))
                elif self.tag_mode == "dep-pos":
                    TAG = str(self.composition_as_tag(token))
                elif self.tag_mode == "pos-dep":
                    TAG = str(self.composition_as_tag_inverted(token))
                elif self.tag_mode == "sqrt_product":
                    TAG = str(self.sqrt_of_product_node_tag(token))
                    #### New Addition (After NAACL 2022 Submission) ####
                elif self.tag_mode == "distance":
                    TAG = str(self.distance_as_tag(token))

                NEIGHBORS = parcial_neighbor[i]
                NUMBER_NEIGHBORS = str(len(NEIGHBORS.split(" "))) if NEIGHBORS != '' else '0'
                NODE_FEATURES = ' '.join(str(d) for d in self.get_vector(token.text))

                if NEIGHBORS != "":
                    sentence_parsed.append(TAG + " " + NUMBER_NEIGHBORS + " " + NEIGHBORS + " " + NODE_FEATURES)
                else:
                    sentence_parsed.append(TAG + " " + NUMBER_NEIGHBORS + " " + NODE_FEATURES)
                i += 1
        
        # Create the ROOT node
        TAG = "0"
        NUMBER_NEIGHBORS = str(len(root_children))
        NEIGHBORS = ""
        NODE_FEATURES = ' '.join(str(d) for d in self.get_vector(ROOT_NAME))
        i = 0
        for child in root_children:
            if i + 1 == len(root_children):
                NEIGHBORS = NEIGHBORS + str(child)
            else:
                NEIGHBORS = NEIGHBORS + str(child) + " "
            i += 1

        sentence_parsed.append(TAG + " " + NUMBER_NEIGHBORS + " " + NEIGHBORS + " " + NODE_FEATURES)

        return sentence_parsed                

    def save_to_file(self, file_name):
        if not os.path.exists(self.output):
            os.makedirs(self.output)

        number_of_graphs = str(len(self.final_dataset))
        with open(file_name, 'w') as f:
            f.write(number_of_graphs)
            for g in self.final_dataset:
                for l in g:
                    f.write("\n" + l)

###############################################################################
###############################################################################
###############################################################################
    def worker(self, id, files_in, return_dict):
        print(self.timestamp(), ">> Starting worker:", id)
        print(self.timestamp(), ">> Worker:", id, "has to process", len(files_in), "file(s)")
        result = []
        for file_in in files_in:
            f = open(file_in, "r")
            file_content = f.read()
            f.close()

            doc = self.nlp(file_content)
            sentences = self.separe_sentences(doc)       

            # Get build the graph of the file
            nodes = self.build_nodes(sentences)

            # Get the number of nodes
            NUMBER_OF_NODES = str(len(nodes))
            CLASS = file_in.split("/")[-1].split("_")[0]
            GRAPH = [NUMBER_OF_NODES + " " + CLASS]
            for n in nodes:
                GRAPH.append(n)

            result.append(GRAPH)

        return_dict[id] = result
        print(self.timestamp(), "!! >> Worker [", id, "] finished its job")

    def generate_dataset(self):
        
        number_of_threads = self.cores

        array = self.files
        processes = []
        ranges = self.get_ranges(array,number_of_threads)
        y = 0
        
        manager = mp.Manager()
        return_dict = manager.dict()

        for i in range(0,number_of_threads):            
            processes.append(mp.Process(target=self.worker, args=(str(i), array[ranges[y]:ranges[y+1]], return_dict)))
            y = y + 2 

        for p in processes:
            p.start()

        for p in processes:
            p.join()        
    
        for i in return_dict:
            for rd in return_dict[i]:
                self.final_dataset.append(rd)

        # ------ Save the position of the shuffled dataset ----
        x = list(enumerate(self.final_dataset))
        random.shuffle(x)
        indices, self.final_dataset = zip(*x)

        
        len_indices = len(indices)
        len_array = len(array)
        index_csv = []
        if len_array != len_indices:
            print("Error: Lists with different sizes")
            exit(1)
        else:
            for i in range(0, len_array):
                index_csv.append([array[i],indices[i]])
            
            df = pd.DataFrame(index_csv, columns=["file","new_index"])
        
        # The above line saves a CSV containing the file and its position in the shuffled dataset
        df.to_csv(self.output + self.set + "_" + self.name + '.csv', sep=";")
        # -----------------------------------------------------

        # Save the dataset
        self.save_to_file(self.output + self.set + "_" + self.name + '.txt')

#  ''' 
#     More info : https://github.com/daiquocnguyen/U2GNN/issues/2
#     Format:
#     1st line = number of graphs
#     N blocks (equal to the number of graphs)
#     Each block cointais:
#         The first line: [n (number of nodes)] and [l (the graph label)] 
#         Each line (until n) is a node
#             [t (tag)] [m (number of neighbors)] [EACH_NEIGHBOR_NUMBER] [d (node features)]
#     exemple:
#     1
#     3 1
#     0 1 2 
#     0 2 0 2
#     0 0
# '''