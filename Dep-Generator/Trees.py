from dataclasses import dataclass

@dataclass
class BinaryNode:
    left: any = None
    right: any = None
    data: any = None
    id: any = None

class Tree():
    def __init__(self, type="Binary"):
        self.type = type
        self.root = BinaryNode()

    
    def insert(self, data):
        print("Inserting: ", data)
        if self.type == "Binary":
            self.insertBinaryTree(self.root, data)
        
    def insertBinaryTree(self, node, data):
        print(">> Debugging (node, data): ",  node, " |", data )
        if node.data == None:
            node.data = data["value"]
            node.id = data["id"]
            node.left = BinaryNode()
            node.right = BinaryNode()  
            print("Node inserted !",node)          
        else:
            if data["value"] < node.data:
                self.insertBinaryTree(node.left, data)
            else:
                self.insertBinaryTree(node.right, data)
    
    def defineNeighborsByData(self, node, neighbors={}):
        """
        Returns a dictionary where the value of the node is the
        """
        if node.data != None:
            neighbors[node.data] = []
            neighbors[node.data].append({"id":node.left.id, "data": node.left.data})
            neighbors[node.data].append({"id":node.right.id, "data": node.right.data})
            self.defineNeighborsByData(node.left, neighbors)
            self.defineNeighborsByData(node.right, neighbors)
        return neighbors
    def defineNeighborsByID(self, node, neighbors={}):
        """
        Returns a dictionary where the id of the node is the
        """
        if node.data != None:
            neighbors[node.id] = []
            neighbors[node.id].append({"id":node.left.id, "data": node.left.data})
            neighbors[node.id].append({"id":node.right.id, "data": node.right.data})
            self.defineNeighborsByID(node.left, neighbors)
            self.defineNeighborsByID(node.right, neighbors)
        return neighbors


# tree = Tree()
# tree.setType("Binary")
# # elements = [5,2,6,1,10,8,7]

# elements = [
#     {"id":1, "value": 5},
#     {"id":2, "value": 2},
#     {"id":3, "value": 6},
#     {"id":4, "value": 1},
#     {"id":5, "value": 10},
#     {"id":6, "value": 8},
#     {"id":7, "value": 7},
# ]

# for element in elements:
#     print(">> Inserting element:", element)
#     tree.insert(element)

# other_rep2 = tree.defineNeighborsByID(tree.root, {})
# print("\n\n_____________________________________\n\n")
# print(other_rep2)

