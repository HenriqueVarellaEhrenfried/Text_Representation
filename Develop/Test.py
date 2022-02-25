import sys
sys.path.insert(0, '../Dep-Generator')

from GraphRepresentation import GraphRepresentation
from LinearAlgebra import LinearAlgebra
from Tags import Tags
import spacy

class Test():
    def __init__(self):
        SPACY_MODEL = "en_core_web_lg"
        self.nlp = spacy.load(SPACY_MODEL)

        self.tag_mode = "dep"
        self.graph_mode = "binary_tree"

        self.pos_types = list(self.nlp.get_pipe("tagger").labels)
        self.pos_types.append('_SP')

        # self.pos_types = ['ADP', 'VERB', 'AUX', 'DET', 'X', 'INTJ', 'NUM', 'SCONJ', 'PROPN', 'CCONJ', 'NOUN', 'ADJ', 'SYM', 'PUNCT', 'PRON', 'PART', 'ADV']
        # self.pos_types.append('SPACE')

        self.dep_types = list(self.nlp.get_pipe("parser").labels)   

        self.la = LinearAlgebra()
        self.la.initialize(list(range(0,len(self.dep_types))),list(range(0,len(self.pos_types))))

        self.tags = Tags(self.tag_mode, self.la, self.pos_types, self.dep_types)

        self.graphs = GraphRepresentation(self.graph_mode, [self.dep_types, self.pos_types], self.la)

        # file_content = "I would like to present now"
        file_content = "Could you please help me with my homework ?"
        # file_content = "Você pode me ajudar a programar ?"

        doc = self.nlp(file_content)
        sentences = self.separe_sentences(doc)  

        print("========================================")

        print(self.build_nodes(sentences))

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
    def build_nodes(self, sentences):
        # This method must generate the following line:
        # [t (tag)] [m (number of neighbors)] [EACH_NEIGHBOR_NUMBER] [d (node features)]
        ROOT_NAME = "@#|ROOT|#@"
        sentence_parsed = []
        root_children = []
        
        for sentence in sentences:
            parcial_neighbor = self.graphs.build_graph(sentence)
            i = 0
            print("parcial_neighbor", parcial_neighbor)
            for token in sentence:
                # token_information(token)
                number_neighbors = len(list(token.children))
                
                if token.dep_ == "ROOT":
                    # Save the root children to create the root node at the end of the process
                    root_children.append(token.i)

                TAG = self.tags.build_tag(token)

                NEIGHBORS = parcial_neighbor[i]
                NUMBER_NEIGHBORS = str(len(NEIGHBORS.split(" "))) if NEIGHBORS != '' else '0'

                NODE_FEATURES = "FEATURES"
                
                if NEIGHBORS != "":
                    sentence_parsed.append(TAG + " " + NUMBER_NEIGHBORS + " " + NEIGHBORS + " " + NODE_FEATURES)
                else:
                    sentence_parsed.append(TAG + " " + NUMBER_NEIGHBORS + " " + NODE_FEATURES)
                i += 1
        return sentence_parsed

Test()