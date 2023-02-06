from Trees import Tree

class GraphRepresentation():
    def __init__(self, graph_mode, dep_pos_types, la):
        # Parameters passed
        self.graph_mode = graph_mode
        self.dep_types = dep_pos_types[0]
        self.pos_types = dep_pos_types[1]
        self.la = la
        print("SELECTED GRAPH MODE: ", self.graph_mode)
    
    def build_graph(self, sentence):
        if self.graph_mode == "tree_only":
            parcial_neighbor = self.handle_neighbors_tree_only(sentence)
        elif self.graph_mode == "tree_and_order":
            parcial_neighbor = self.handle_neighbors_tree_and_order(sentence)
        elif self.graph_mode == "tree_and_order_multi_graph":
            parcial_neighbor = self.handle_neighbors_tree_and_order_multi_graph(sentence)
        elif self.graph_mode == "tree_and_self":
            parcial_neighbor = self.handle_neighbors_tree_and_self(sentence)
        elif self.graph_mode == "tree_order_and_self":
            parcial_neighbor = self.handle_neighbors_tree_order_and_self(sentence)
        elif self.graph_mode == "tree_order_multigraph_and_self":
            parcial_neighbor = self.handle_neighbors_tree_order_multigraph_and_self(sentence)
        elif self.graph_mode == "only_order":
            parcial_neighbor = self.order_only(sentence)
        elif self.graph_mode == "order_circular":
            parcial_neighbor = self.order_circular(sentence)
        elif self.graph_mode == "binary_tree":
            parcial_neighbor = self.generate_binary_tree(sentence)
        elif self.graph_mode == "avl_tree":
            parcial_neighbor = self.generate_avl_tree(sentence)
        elif self.graph_mode == "red_black_tree":
            parcial_neighbor = self.generate_red_black_tree(sentence)
        # Add Graph of Words (GoW)
        elif self.graph_mode == "gow":
            parcial_neighbor = self.generate_graph_of_words(sentence)

        else:
            print("!!! ATTENTION !!! >>> Graph mode unavailable")

        return parcial_neighbor


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

    def get_all_indexes(self, array, value):
        new_array = []
        if str(type(array[0])) == "<class 'spacy.tokens.token.Token'>":
            for a in array:
                new_array.append(str(a))
            return [i for i,val in enumerate(new_array) if val==str(value)]
        else:
            return [i for i,val in enumerate(array) if val==value]

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
        # This Funcion parses the text using the sPacy and build the neighbors from it
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
        # print(sentence)
        # print(result)
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

    def order_only(self, sentence):
        ## This method uses only the order of the word
        token_number = 0
        num_tokens = len(sentence)
        token_index = 0
        result = []
        
        for token in sentence:   
            NEIGHBORS = ""
            if token_index < (num_tokens):    
                if token_index + 1 != num_tokens:
                    NEIGHBORS = NEIGHBORS + str(token_index+1)
            token_index +=1
            token_number +=1
            result.append(NEIGHBORS)
        return result

    def order_circular(self, sentence):
        ## This method uses only the order of the word and the last token is linked to the first
        token_number = 0
        num_tokens = len(sentence)
        token_index = 0
        result = []
        
        for token in sentence:   
            NEIGHBORS = ""
            if token_index < (num_tokens):   
                NEIGHBORS = NEIGHBORS + str((token_index+1)%num_tokens)

            token_index +=1
            token_number +=1
            result.append(NEIGHBORS)
        return result
        
    def generate_binary_tree(self,sentence):
        ## This method creates a graph of word from the sentence
        def return_strings(tree):
            """Receives the result of Tree.defineNeighborsByID"""
            function_result = []
            for key in sorted(tree):
                data = tree[key]
                neighbor_left = str(data[0]["id"]) if data[0]["id"] != None else data[0]["id"]
                neighbor_right =str(data[1]["id"]) if data[1]["id"] != None else data[1]["id"]
                if neighbor_left and neighbor_right:
                    function_result.append(neighbor_left + " " + neighbor_right)
                elif neighbor_left and not neighbor_right:
                    function_result.append(neighbor_left)
                elif not neighbor_left and neighbor_right:
                    function_result.append(neighbor_right)
                else:
                    function_result.append('')
            return function_result

        root = None
        tree = Tree("Binary")
        elements = []
        for token in sentence:
            temp = {}
            temp["id"] = token.i
            # Using Distance first
            dep = self.dep_types.index(token.dep_)
            pos = self.pos_types.index(token.tag_)
            temp["value"] = self.la.distances_sorted.index(self.la.distance_difference(dep,pos,[len(self.dep_types)-1,len(self.pos_types)-1]))

            root = tree.insert(root, temp)

            temp["token"] = token.text
            elements.append(temp)

        tree.root = root
        results = tree.defineNeighborsByID(tree.root, {})
        return  return_strings(results)
  
    def generate_avl_tree(self,sentence):
        ## This method creates a graph of word from the sentence
        def return_strings(tree):
            """Receives the result of Tree.defineNeighborsByID"""
            function_result = []
            for key in sorted(tree):
                data = tree[key]
                neighbor_left = str(data[0]["id"]) if data[0]["id"] != None else data[0]["id"]
                neighbor_right =str(data[1]["id"]) if data[1]["id"] != None else data[1]["id"]
                if neighbor_left and neighbor_right:
                    function_result.append(neighbor_left + " " + neighbor_right)
                elif neighbor_left and not neighbor_right:
                    function_result.append(neighbor_left)
                elif not neighbor_left and neighbor_right:
                    function_result.append(neighbor_right)
                else:
                    function_result.append('')
            return function_result

        root = None
        tree = Tree("AVL")
        elements = []
        for token in sentence:
            temp = {}
            temp["id"] = token.i
            # Using Distance first
            dep = self.dep_types.index(token.dep_)
            pos = self.pos_types.index(token.tag_)
            temp["value"] = self.la.distances_sorted.index(self.la.distance_difference(dep,pos,[len(self.dep_types)-1,len(self.pos_types)-1]))

            root = tree.insert(root, temp)

            temp["token"] = token.text
            elements.append(temp)

        tree.root = root
        results = tree.defineNeighborsByID(tree.root, {})
        return  return_strings(results)

    def generate_red_black_tree(self,sentence):
        ## This method creates a graph of word from the sentence
        def return_strings(tree):
            """Receives the result of Tree.defineNeighborsByID"""
            function_result = []
            for key in sorted(tree):
                data = tree[key]
                neighbor_left = str(data[0]["id"]) if data[0]["id"] != None else data[0]["id"]
                neighbor_right =str(data[1]["id"]) if data[1]["id"] != None else data[1]["id"]
                if neighbor_left and neighbor_right:
                    function_result.append(neighbor_left + " " + neighbor_right)
                elif neighbor_left and not neighbor_right:
                    function_result.append(neighbor_left)
                elif not neighbor_left and neighbor_right:
                    function_result.append(neighbor_right)
                else:
                    function_result.append('')
            return function_result

        root = None
        tree = Tree("RedBlack")
        elements = []
        for token in sentence:
            temp = {}
            temp["id"] = token.i
            # Using Distance first
            dep = self.dep_types.index(token.dep_)
            pos = self.pos_types.index(token.tag_)
            temp["value"] = self.la.distances_sorted.index(self.la.distance_difference(dep,pos,[len(self.dep_types)-1,len(self.pos_types)-1]))

            root = tree.insert(root, temp)

            temp["token"] = token.text
            elements.append(temp)
        tree.root = root
        results = tree.defineNeighborsByID(tree.root, {})
        return  return_strings(results)

    def generate_graph_of_words(self, sentence):
        '''
        Implementation of Graph of Word from:
        François Rousseau and Michalis Vazirgiannis. 2013. Graph-of-word and tw-idf: New approach to ad hoc ir. 
        In Proceedings of the 22nd ACM International Conference on Information; Knowledge Management, CIKM ’13, 
        page 59–68, New York, NY, USA. Association for Computing Machinery.

        This code follows some assumptions:
        1) The graph is directed   (See Secetion 4.2 of the cited paper above)
        2) The graph is unweighted (See Secetion 4.3 of the cited paper above)
        3) The sliding windows has size 4 (See Secetion 4.4 of the cited paper above)
        4) If the words are written different, they are different words: [Sand, sand, SAnd] are three different words
        5) If the sliding window is bigger than the remaining sentence, reduce the sliding window
        '''
        
        
        SLIDING_WINDOW = 4
        result = []
        s_window = SLIDING_WINDOW

        # Build index equevalence
        sentence_indexes = []
        for s in sentence:
            sentence_indexes.append(self.get_all_indexes(sentence, s))
        

        i = 0
        for _ in sentence:
            working_words = []
            NEIGHBORS = ""  
            if i + s_window - 1 >= len(sentence):
                s_window -= 1

            if i + s_window - 1 < len(sentence):
                for j in range(0, s_window):
                    working_words.append(sentence[i+j])
                    if j > 0:
                        NEIGHBORS = NEIGHBORS + str(sentence_indexes[i+j][0]) + " "
            result.append(NEIGHBORS.rstrip())  
            # print(working_words)      
            i += 1
        return(result)
        
        


#  """
#       IDEAS:
#         Usar uma estrutura de árvore junto com POS/DEP/Distância
#         Ver qual árvore se enquadra melhor - Binária Red-Black / B / B+ / Patrícia
#         - Provavelmente será uma árvore Patrícia
#         - Explorar outras árvores

#         Basicamente vamos pegar o atributo POS/DEP/Distância de cada palavra e 
#         mapear para a árvore escolhida. 

#         IMPORTANTE precisa ter um jeito de colocar o TAG, portanto a ligação
#         de cada nó deve ser descoberto e depois mapeado para o formato original da
#         sentença. Assim como feito no order_rearranged 

#         ---

#         Outra ideia
#         Fazer as árvores de dependência e linkar o último nó com o  primeiro, porque 
#         nós humanos as vezes precisamos reler uma sentença para entender, então se
#         eu adicionar um loop numa árvore, tirando as propriedades de árvore, pode ser
#         que melhore o desempenho.
# """

