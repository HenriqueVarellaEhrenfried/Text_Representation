class LinearAlgebra():
    def __init__(self):
        # Parameters passed
        self.combinations = None     # self.combine(list(range(0,len(self.dep_types))),list(range(0,len(self.pos_types))))
        self.distances = None        # self.calculate_all_distances(self.combinations)
        self.distances_sorted = None # sorted(self.distances)

    def initialize(self, set1, set2):
        self.combine( set1, set2)
        self.calculate_all_distances(self.combinations)

    def combine(self, set1, set2):
        combinations = []
        for s1 in set1:
            for s2 in set2:
                combinations.append([s1,s2])
        self.combinations = combinations            

    def calculate_all_distances(self, combinations):
        distances = []

        for i in range(0,len(combinations)):
            comb = combinations[i]
            # Calculate distance of the point to the orgin
            distances1 = self.distance(0,(comb[0]),0,(comb[1]))
            # Calculate distance to the point above (max(X)+1, max(Y)+1)
            distances2 = self.distance((combinations[-1][0])+1,(comb[0]),(combinations[-1][1])+1,(comb[1]))
            # Calculate difference between the distances
            distances.append(distances1-distances2)

        self.distances = distances
        self.distances_sorted = sorted(distances)

    def distance_difference(self, x, y, point_a, point_b=[0,0]):
        # Calculate distance of the point to the orgin
        d1 = self.distance(point_b[0],x,point_b[1],y)
        # Calculate distance to the point above (max(X)+1, max(Y)+1)
        d2 = self.distance(point_a[0]+1,x,point_a[1]+1,y)
        # Calculate difference between the distances
        d = d1 - d2

        return d

    def distance(self, xa, xb, ya, yb):
        x = (xb - xa) ** 2
        y = (yb - ya) ** 2
        s = x + y 
        d = s ** 0.5
        return d 
    