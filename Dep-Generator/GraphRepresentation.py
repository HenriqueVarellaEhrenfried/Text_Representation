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
            #### New Addition OTHER FORMATS ####
        elif self.graph_mode == "only_order":
            parcial_neighbor = self.order_only(sentence)
        elif self.graph_mode == "order_circular":
            parcial_neighbor = self.order_circular(sentence)
        elif self.graph_mode == "order_rearranged":
            parcial_neighbor = self.order_rearranged(sentence)
        
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
                print("TOKEN >>", token, "\t\tCHILD >>", child)
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

    ### WIP: Below methods are being constructed    
    ## TODO: Finish and test below methods
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
                    print("DEBUG >>", token.text , '| Now:', token_index, 'Next:' , token_index+1)
                    NEIGHBORS = NEIGHBORS + str(token_index+1)
                else:
                    print("DEBUG >>", token.text , '| Now:', token_index, 'Next:' )
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
                print("DEBUG >>", token.text , '| Now:', token_index, 'Next:' , (token_index+1)%num_tokens)
                NEIGHBORS = NEIGHBORS + str((token_index+1)%num_tokens)

            token_index +=1
            token_number +=1
            result.append(NEIGHBORS)
        return result
        

    def order_rearranged(self, sentence):
        ## This method uses only the order of the word after we rearrange it by its syntatical information
        def return_child(token, token_list):
            """
            Build the token order (similar to binary tree reading)
            """
            if len(list(token.children)) == 0:
                token_list.append(token)
                return token_list
            else:
                token_list.append(token)
                for chd in list(token.children):
                    return_child(chd, token_list)
                return token_list


        print(" ----- | WIP | -----")
        result = []
        tree = []
        root = None
        for token in sentence:
            if token.dep_ == 'ROOT':
                root = token
        
        tree = return_child(root, tree)
        
        ordering = {}
        for i in range(0,len(tree)):
            if i+1 < len(tree):
                ordering[tree[i].i] = str(tree[i+1].i)
            else:
                ordering[tree[i].i] = ""

        for i in range(0, len(ordering)):
            NEIGHBORS = "%s" % (ordering[i])
            result.append(NEIGHBORS)
        return result

        print("--------------------")

    def graph_of_word(self):
        ## This method creates a graph of word from the sentence
        print(" ----- | WIP | -----")
     
        print("--------------------")

