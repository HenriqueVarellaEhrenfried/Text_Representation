import spacy

def separe_sentences(doc):
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

def list_neighbors(sentence,current_token, num_tokens, neighbors):
    if current_token+1 != num_tokens:
        linear_neighbor = sentence[current_token+1]
    else:
       return list(neighbors)
    return list(set(list(neighbors) + [linear_neighbor]))

def handle_neighbors_tree_and_order(sentence):
    print("Sentence:: ", sentence)
    token_number = 0
    num_tokens = len(sentence)
    result = []
    for token in sentence:            
        print("Token ", token_number, ">> ", token)
        token_children = list_neighbors(sentence, token_number, num_tokens, token.children)           
        print("\tTOKEN CHILDREN >>", token_children)
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
        print(NEIGHBORS)
        result.append(NEIGHBORS)
    return result

def handle_neighbors_tree_only(sentence):
    print("Sentence:: ", sentence)
    token_number = 0
    num_tokens = len(sentence)
    result = []
    for token in sentence:            
        print("Token ", token_number, ">> ", token)
        token_children = list(token.children)
        print("\tTOKEN CHILDREN >>", token_children)
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
        print(NEIGHBORS)
        result.append(NEIGHBORS)
    return result

def build_nodes( sentences):
    # This method must generate the following line:
    # [t (tag)] [m (number of neighbors)] [EACH_NEIGHBOR_NUMBER] [d (node features)]
    ROOT_NAME = "@#|ROOT|#@"
    sentence_parsed = []
    root_children = []
    graph_mode = "tree_only"
    # graph_mode = "tree_and_order"
    for sentence in sentences:
        if graph_mode == "tree_only":
            parcial_neighbor = handle_neighbors_tree_only(sentence)
        elif graph_mode == "tree_and_order":
            parcial_neighbor = handle_neighbors_tree_and_order(sentence)
       
        i = 0
        print("parcial_neighbor", parcial_neighbor)
        for token in sentence:
            number_neighbors = len(list(token.children))
            
            if token.dep_ == "ROOT":
                # Save the root children to create the root node at the end of the process
                root_children.append(token.i)

            TAG = "0"
            NEIGHBORS = parcial_neighbor[i]
            NUMBER_NEIGHBORS = str(len(NEIGHBORS.split(" "))) if NEIGHBORS != '' else '0'
          
            NODE_FEATURES = "FEATURES"
            
            if NEIGHBORS != "":
                sentence_parsed.append(TAG + " " + NUMBER_NEIGHBORS + " " + NEIGHBORS + " " + NODE_FEATURES)
            else:
                sentence_parsed.append(TAG + " " + NUMBER_NEIGHBORS + " " + NODE_FEATURES)
            i += 1
    return sentence_parsed


SPACY_MODEL = "en_core_web_lg"
nlp = spacy.load(SPACY_MODEL)

# https://explosion.ai/demos/displacy?text=I%20would%20like%20to%20present%20now.%20Could%20you%20make%20it%20happen%3F&model=en_core_web_sm&cpu=0&cph=0
# file_content = "I would like to present now. Could you make it happen?"
file_content = "I would like to present now"

doc = nlp(file_content)

sentences = separe_sentences(doc)  
print("========================================")

print(build_nodes(sentences))
# print(handle_neighbors_tree_only(sentences[0]))
