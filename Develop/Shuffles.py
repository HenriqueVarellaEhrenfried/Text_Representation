import spacy
import random

class Shuffles():
    def __init__(self):
        SPACY_MODEL = "en_core_web_lg"
        self.nlp = spacy.load(SPACY_MODEL)
        self.seeds = [10, 20, 30, 40]
        
        self.pos_types = list(self.nlp.get_pipe("tagger").labels)
        self.pos_types.append('_SP')

        self.dep_types = list(self.nlp.get_pipe("parser").labels)   

        self.shuffled_pos_types = self.shuffles_array(self.pos_types, self.seeds)
        print('-------------')
        self.shuffled_dep_types = self.shuffles_array(self.dep_types, self.seeds)

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

    def shuffle_array(self, array, seed):
        new_array = array.copy()
        random.seed()
        random.seed(seed)
        random.shuffle(new_array)
        random.seed()
        return new_array


sh = Shuffles()

print(sh.shuffle_array(sh.dep_types, 11))
