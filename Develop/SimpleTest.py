import json
from turtle import distance

def distancia(xa, xb, ya, yb):
    x = (xb - xa) ** 2
    y = (yb - ya) ** 2
    s = x + y 
    d = s ** 0.5
    return d 

def verify_dist():
    TARGETS = [
        [29,28,"I"],
        [9,20,"would"],
        [0,37,"like"],
        [9,35,"to"],
        [44,37,"present"],
        [4,30,"now"],
        [0,0,"EXTRA1"],
        [45,49,"EXTRA2"],
        [45,0,"EXTRA3"],
        [0,49,"EXTRA4"]
    ]
    BASE1 = [0,0]
    BASE2 = [45,49]

    for t in TARGETS:
        d1 = distancia(BASE1[0], t[0], BASE1[1], t[1])
        d2 = distancia(BASE2[0], t[0], BASE2[1], t[1])

        print("Até origem da palavra", t[2], "> ", int(d1))
        print("Até Limite da palavra", t[2], "> ", int(d2))
        print("Média da palavra", t[2], "> ", int((d1+d2)/2))
        print("------------------------------------------------")

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

def calculate_distance(limit, x, y):
    # Calculate distance of the point to the orgin
    d1 = distancia(0,x,0,y)
    # Calculate distance to the point above (max(X)+1, max(Y)+1)
    d2 = distancia(limit[0]+1,x,limit[1]+1,y)
    # Calculate difference between the distances
    d = d1 - d2

    return d

def count_distances(distances):
    counter = {}
    for d in distances:
        if str(d) in counter: 
            counter[str(d)] += 1
        else:
            counter[str(d)] = 1
    return counter

def equal_distances(points, distances):
    counter = {}
    for i in range(0,len(distances)):
        d = distances[i]
        if str(d) in counter: 
            counter[str(d)].append(points[i])
        else:
            counter[str(d)] = [points[i]]
    return counter
   

def table():
    X = list(range(0,45))
    Y = list(range(0,49))
    combinations = combine(X,Y)
    distances = calculate_all_distances(combinations)
    distances_sorted = sorted(distances)

    TARGETS = [
        [29,28,"I"],
        [9,20,"would"],
        [0,37,"like"],
        [9,35,"to"],
        [44,37,"present"],
        [4,30,"now"]        
    ]
    for t in TARGETS:
        # print(t[2])
        # print(distances_sorted[-1],"\n\n\n\n")
        tag = distances_sorted.index(calculate_distance([len(X)-1,len(Y)-1],t[0],t[1]))
        print(t[2], ">", tag)


table()