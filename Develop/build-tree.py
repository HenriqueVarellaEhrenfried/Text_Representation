import networkx as nx
import matplotlib.pyplot as plt
import pydot
from networkx.drawing.nx_pydot import graphviz_layout


# btree = ['1', '3 2', '6', '4', '8 5', '7', '', '', '']
# sentence = ['Could', 'you', 'please', 'help', 'me', 'with', 'my', 'homework', '?']
btree = ['1 16', '3 2', '4 5', '8 33', '9 7', '6 10', '11', '13 71', '118 21', '19 35', '12', '17', '14 36', '22 15', '20', '28 27', '62', '18 93', '23', '67 26', '24', '25', '75 31', '32', '52', '34', '70', '30 29', '59 38', '37 182', '61 184', '127', '44', '40', '39', '42', '58 43', '81 94', '56 53', '41 76', '45', '46', '47', '48', '49', '50', '66', '105', '55', '54', '51', '68', '60', '80 82', '57', '106', '74', '64', '208', '138', '65', '63', '91 108', '90 163', '72', '69', '104', '247 152', '79', '73', '78', '207 110', '77', '83', '195 116', '98 117', '137', '84', '86', '87', '95 175', '194', '', '89', '85', '96', '97', '88', '92', '99', '107', '126', '103', '', '161', '162', '100', '109', '159', '101', '102', '112', '111', '114', '122', '123', '135', '125', '143', '120', '128', '113', '115', '119', '121', '124', '129', '', '249', '133', '144', '134', '131', '', '149', '142', '', '132 173', '145', '130', '191 185', '136', '233', '139', '140', '141', '157', '165', '214 203', '146', '148', '190', '171', '172 164', '147', '174 180', '150', '151', '155', '153', '154', '168', '254', '156', '158', '169', '160', '231', '166', '178', '170', '', '210', '', '', '', '167', '176', '177', '189', '179', '206', '', '211', '200', '', '183', '181', '218', '187', '', '193', '196', '186 209', '197', '205', '188', '198', '192', '225', '227', '199', '212', '204', '', '236', '235', '201', '202', '220', '248', '217', '215', '', '216', '', '256', '257', '213', '', '', '', '224', '', '', '219', '221', '222', '226', '223', '230', '232', '238', '229', '228', '239', '242', '246', '234', '240', '', '', '251', '', '241', '237', '', '', '', '245', '243', '244', '', '252', '250', '', '255', '', '', '', '253', '', '', '', '', '', '', '']
sentence =['\n        ', 'Characteristics', 'of', 'cholinergic', 'neuroeffector', 'transmission', 'of', 'ganglionic', 'and', 'aganglionic', 'colon', 'in', 'Hirschsprung', "'s", 'disease', '.', '\n        ', 'Differences', 'in', 'the', 'release', 'and', 'content', 'of', 'acetylcholine', 'and', 'the', 'alpha', '2', 'adrenoceptor', 'mediated', 'interaction', 'between', 'noradrenergic', 'and', 'cholinergic', 'neurons', 'were', 'investigated', 'by', 'neurochemical', 'and', 'pharmacological', 'methods', 'in', 'aganglionic', 'and', 'ganglionic', 'segments', 'of', 'isolated', 'human', 'colon', 'taken', 'from', 'children', 'suffering', 'from', 'Hirschsprung', "'s", 'disease', '.', '\n        ', 'Both', 'at', 'rest', 'and', 'during', 'transmural', 'stimulation', 'the', 'release', 'of', 'acetylcholine', 'was', 'significantly', 'higher', 'in', 'the', 'spastic', '(', 'aganglionic', ')', 'segment', 'than', 'in', 'the', 'proximal', 'dilated', 'bowel', '.', '\n        ', 'Significant', 'differences', 'were', 'found', 'in', 'the', 'tissue', 'concentration', 'of', 'acetylcholine', 'between', 'ganglionic', 'and', 'aganglionic', 'specimens', '.', '\n        ', 'The', 'pattern', 'of', 'response', 'to', 'transmural', 'stimulation', 'was', 'also', 'different', 'in', 'the', 'spastic', 'and', 'dilated', 'bowel', '.', '\n        ', 'Transmural', 'stimulation', 'induced', 'relaxation', 'and', 'contraction', 'in', 'ganglionic', 'specimens', 'but', 'only', 'contractions', 'in', 'aganglionic', 'specimens', '.', '\n        ', 'The', 'sensitivity', 'of', 'the', 'smooth', 'muscle', 'in', 'the', 'aganglionic', 'portion', 'to', 'exogenous', 'acetylcholine', 'and', 'to', 'field', 'stimulation', 'was', 'found', 'to', 'be', 'higher', 'than', 'in', 'the', 'ganglionic', 'portion', '.', '\n        ', 'While', 'noradrenaline', 'added', 'to', 'the', 'organ', 'bath', 'reduced', 'the', 'stimulation', '-', 'evoked', 'release', 'of', 'acetylcholine', 'from', 'spastic', 'segments', ',', 'via', 'an', 'alpha', '2', 'adrenoceptor', 'mediated', 'process', ',', 'yohimbine', 'did', 'not', 'enhance', 'the', 'release', '.', '\n        ', 'It', 'is', 'suggested', 'that', 'in', 'Hirschsprung', "'s", 'disease', 'the', 'increased', 'acetylcholine', 'release', ',', 'the', 'enhanced', 'sensitivity', 'of', 'smooth', 'muscle', 'cells', 'to', 'acetylcholine', ',', 'and', 'the', 'lack', 'of', 'alpha', '2', 'adrenoceptor', 'mediated', 'noradrenergic', 'modulation', 'of', 'acetylcholine', 'release', 'from', 'cholinergic', 'interneurons', 'might', 'be', 'responsible', 'for', 'the', 'spasm', 'of', 'aganglionic', 'segments', '.', '\n        ']

G = nx.Graph()

for i in range(0,len(sentence)):
    s = sentence[i]
    node = "[%s] [%s]" % (str(i), str(s))
    G.add_node(node)

for i in range(0,len(btree)):
    current_node = "[%s] [%s]" % (str(i), str(sentence[i]))
    neighbors = btree[i].split(" ")
    if len(neighbors) >= 1:
        for n in neighbors:
            if n != '':
                current_neighbor = "[%s] [%s]" % (str(n), str(sentence[int(n)]))
                G.add_edge(current_node, current_neighbor)



f = plt.figure(3,figsize=(12,12)) 
# nx.draw(G, pos=nx.spectral_layout(G), node_color='r', edge_color='b', ax=f.add_subplot(111))
# f.savefig("graph.png")


pos = graphviz_layout(G, prog="dot")
nx.draw(G, pos, node_color='r', edge_color='b', ax=f.add_subplot(111), with_labels=True, node_size=60, font_size=2)
f.savefig("graph.png", dpi=1000)
# plt.show()