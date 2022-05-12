import sys
sys.path.insert(0, '../Dep-Generator')

from GraphRepresentation import GraphRepresentation
from LinearAlgebra import LinearAlgebra
from Tags import Tags
import spacy
import random

class Test():
    def __init__(self):
        SPACY_MODEL = "en_core_web_lg"
        self.nlp = spacy.load(SPACY_MODEL)

        self.tag_mode = "none"
        self.graph_mode = "binary_tree"

        self.pos_types = list(self.nlp.get_pipe("tagger").labels)
        self.pos_types.append('_SP')

        # self.pos_types = ['ADP', 'VERB', 'AUX', 'DET', 'X', 'INTJ', 'NUM', 'SCONJ', 'PROPN', 'CCONJ', 'NOUN', 'ADJ', 'SYM', 'PUNCT', 'PRON', 'PART', 'ADV']
        # self.pos_types.append('SPACE')

        self.dep_types = list(self.nlp.get_pipe("parser").labels)   

        self.seeds = [10, 20, 30, 40]
        self.shuffled_pos_types = self.shuffles_array(self.pos_types, self.seeds)
        self.shuffled_dep_types = self.shuffles_array(self.dep_types, self.seeds)

        self.print_shuffled(self.shuffled_pos_types)
        self.print_shuffled(self.shuffled_dep_types)

        self.la = LinearAlgebra()
        self.la.initialize(list(range(0,len(self.dep_types))),list(range(0,len(self.pos_types))))

        self.tags = Tags(self.tag_mode, self.la, self.pos_types, self.dep_types)

        self.graphs = GraphRepresentation(self.graph_mode, [self.dep_types, self.pos_types], self.la)

        # file_content = "I would like to present now"
        file_content = "Could you please help me with my homework ?"
        # file_content = "Você pode me ajudar a programar ?"
        # file_content = """
        # Characteristics of cholinergic neuroeffector transmission of ganglionic and aganglionic colon in Hirschsprung's disease.
        # Differences in the release and content of acetylcholine and the alpha 2 adrenoceptor mediated interaction between noradrenergic and cholinergic neurons were investigated by neurochemical and pharmacological methods in aganglionic and ganglionic segments of isolated human colon taken from children suffering from Hirschsprung's disease.
        # Both at rest and during transmural stimulation the release of acetylcholine was significantly higher in the spastic (aganglionic) segment than in the proximal dilated bowel.
        # Significant differences were found in the tissue concentration of acetylcholine between ganglionic and aganglionic specimens.
        # The pattern of response to transmural stimulation was also different in the spastic and dilated bowel.
        # Transmural stimulation induced relaxation and contraction in ganglionic specimens but only contractions in aganglionic specimens.
        # The sensitivity of the smooth muscle in the aganglionic portion to exogenous acetylcholine and to field stimulation was found to be higher than in the ganglionic portion.
        # While noradrenaline added to the organ bath reduced the stimulation-evoked release of acetylcholine from spastic segments, via an alpha 2 adrenoceptor mediated process, yohimbine did not enhance the release.
        # It is suggested that in Hirschsprung's disease the increased acetylcholine release, the enhanced sensitivity of smooth muscle cells to acetylcholine, and the lack of alpha 2 adrenoceptor mediated noradrenergic modulation of acetylcholine release from cholinergic interneurons might be responsible for the spasm of aganglionic segments.
        # """

        doc = self.nlp(file_content)
        sentences = self.separe_sentences(doc)  

        print("========================================")

        print(self.build_nodes(sentences))

    
    def print_shuffled(self, array):
        for a in array:
            print(a)
            print("\n")
        
    def shuffles_array(self, array, seeds):
        output = []
        output.append(array)
        random.seed()
        for s in seeds:
            random.seed(s)
            aux = array.copy()
            random.shuffle(aux)
            aux2 = aux.copy()
            aux = array.copy()
            output.append(aux2)
            random.seed()
        return output
    
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