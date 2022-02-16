import math

class Tags():
    def __init__(self, tag_mode, la, pos_types, dep_types):
        # Parameters passed
        self.tag_mode = tag_mode
        self.pos_types = pos_types
        self.dep_types = dep_types
        # Initialize Linear Algebra
        self.la = la
    def build_tag(self, token):
        if self.tag_mode == "none":
            TAG = str(self.default())
        elif self.tag_mode == "dep":
            TAG = str(self.DEP_as_tag(token))
        elif self.tag_mode == "pos":
            TAG = str(self.POS_as_tag(token))
        elif self.tag_mode == "dep-pos":
            TAG = str(self.composition_as_tag(token))
        elif self.tag_mode == "pos-dep":
            TAG = str(self.composition_as_tag_inverted(token))
        elif self.tag_mode == "sqrt_product":
            TAG = str(self.sqrt_of_product_node_tag(token))
            #### New Addition (After NAACL 2022 Submission) ####
        elif self.tag_mode == "distance":
            TAG = str(self.distance_as_tag(token))
        return(TAG)

    def POS_as_tag(self, token):
        index = self.pos_types.index(token.tag_) if token.tag_ in self.pos_types else 99
        return index

    def DEP_as_tag(self, token):
        index = self.dep_types.index(token.dep_) if token.dep_ in self.dep_types else 99
        return index

    def composition_as_tag(self, token):
        dep = self.dep_types.index(token.dep_) if token.dep_ in self.dep_types else 99
        pos = self.pos_types.index(token.tag_) if token.tag_ in self.pos_types else 99
        
        composition = (dep * 100) + pos
        return composition

    def composition_as_tag_inverted(self, token):
        dep = self.dep_types.index(token.dep_) if token.dep_ in self.dep_types else 99
        pos = self.pos_types.index(token.tag_) if token.tag_ in self.pos_types else 99
        
        composition = (pos * 100) + dep
        return composition

    def sqrt_of_product_node_tag(self, token):
        dep = self.dep_types.index(token.dep_) if token.dep_ in self.dep_types else 99
        pos = self.pos_types.index(token.tag_) if token.tag_ in self.pos_types else 99
        
        composition = math.ceil((dep*pos)**1/2)
        return composition

    def distance_as_tag(self, token):
        dep = self.dep_types.index(token.dep_)
        pos = self.pos_types.index(token.tag_)

        tag = self.la.distances_sorted.index(self.la.distance_difference(dep,pos,[len(self.dep_types)-1,len(self.pos_types)-1]))
        return tag
    
    def default(self):
        return "0"