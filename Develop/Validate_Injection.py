import spacy 
import json 

def distancia(xa, xb, ya, yb):
    x = (xb - xa) ** 2
    y = (yb - ya) ** 2
    s = x + y 
    d = s ** 0.5
    return d 

def combine(set1, set2):
    combinations = []
    for s1 in set1:
        for s2 in set2:
            combinations.append([s1,s2])
    return combinations

def calculate_all_distances(combinations):
    offset = combinations[-1][0] + combinations[-1][1]
    offset = 0
    distances = []
    distances1 = []
    distances2 = []

    for i in range(0,len(combinations)):
        comb = combinations[i]
        # Calculate distance of the point to the orgin
        distances1.append(distancia(0,comb[0]+offset,0,comb[1]))
        # Calculate distance to the point above (max(X)+1, max(Y)+1)
        distances2.append(distancia(combinations[-1][0]+1,comb[0]+offset,combinations[-1][1]+1,comb[1]))
        # Calculate difference between the distances
        distances.append((distances1[i]-distances2[i]))

    return distances

def verify(lang, X, Y):
    combinations = combine(X,Y)
    distances = calculate_all_distances(combinations)
    len_comb = len(combinations)
    len_dist = len(distances)
    print("%s | Combination size = %d, Distance size = %d" % (lang, len_comb, len_dist))

def view_positions(lang, X, Y, VECTORS):
    combinations = combine(X,Y)
    distances = calculate_all_distances(combinations)
    distances_sorted = sorted(distances)
    


    results = {}

    for comb in combinations:
        current_x = VECTORS[lang]['X'][comb[0]]
        current_y = VECTORS[lang]['Y'][comb[1]]
        difference = distances[combinations.index(comb)]
        position = distances_sorted.index(difference)

        if not(current_x) in results:
            results[current_x] = {current_y: {'x': comb[0], 'y': comb[1], 'sorted position': position, 'difference': difference}}
        else:
            results[current_x][current_y] = {'x': comb[0], 'y': comb[1],'sorted position': position, 'difference': difference}

    return json.dumps(results,indent=2)

def to_file(json, file):
    file1 = open(file, "w")
    file1.write(json)
    file1.close()


SPACY_MODEL_EN = "en_core_web_lg"
SPACY_MODEL_PT = "pt_core_news_lg"
SPACY_MODEL_DE = "de_core_news_lg"

nlp_en = spacy.load(SPACY_MODEL_EN)
nlp_pt = spacy.load(SPACY_MODEL_PT)
nlp_de = spacy.load(SPACY_MODEL_DE)

pos_types_en = list(nlp_en.get_pipe("tagger").labels)
pos_types_de = list(nlp_de.get_pipe("tagger").labels)
pos_types_pt = ['ADP', 'VERB', 'AUX', 'DET', 'X', 'INTJ', 'NUM', 'SCONJ', 'PROPN', 'CCONJ', 'NOUN', 'ADJ', 'SYM', 'PUNCT', 'PRON', 'PART', 'ADV']
dep_types_en = list(nlp_en.get_pipe("parser").labels)    
dep_types_pt = list(nlp_pt.get_pipe("parser").labels)    
dep_types_de = list(nlp_de.get_pipe("parser").labels)    

pos_types_en.append('_SP')
pos_types_de.append('_SP')
pos_types_pt.append('SPACE')

VECTORS={
    "English":{'X': dep_types_en, 'Y': pos_types_en},
    "Portuguese":{'X': dep_types_pt, 'Y': pos_types_pt},
    "German":{'X': dep_types_de, 'Y': pos_types_de}
}


VERIFY_VALUES = [
    ["English", (list(range(0,len(dep_types_en)))), (list(range(0,len(pos_types_en))))],
    ["Portuguese", (list(range(0,len(dep_types_pt)))), (list(range(0,len(pos_types_pt))))],
    ["German", (list(range(0,len(dep_types_de)))), (list(range(0,len(pos_types_de))))]
]
for v in VERIFY_VALUES:
    verify(v[0],v[1],v[2])
    r = view_positions(v[0],v[1],v[2], VECTORS)
    to_file(r, v[0]+'_positions.json')