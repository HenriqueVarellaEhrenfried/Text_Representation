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

def handle_neighbors(sentence):
    print("Sentence:: ", sentence)
    token_number = 0
    num_tokens = len(sentence)
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


SPACY_MODEL = "en_core_web_lg"
nlp = spacy.load(SPACY_MODEL)

# https://explosion.ai/demos/displacy?text=I%20would%20like%20to%20present%20now.%20Could%20you%20make%20it%20happen%3F&model=en_core_web_sm&cpu=0&cph=0
# file_content = "I would like to present now. Could you make it happen?"
file_content = "I would like to present now"

doc = nlp(file_content)

sentences = separe_sentences(doc)  


handle_neighbors(sentences[0])