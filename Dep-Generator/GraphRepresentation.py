class GraphRepresentation():
    def __init__(self, graph_mode):
        # Parameters passed
        self.graph_mode = graph_mode
    
    def build_graph(self, sentence):
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