from dataclasses import dataclass
import sys

@dataclass
class BinaryNode:
    def __init__ (self, value, id):
        self.left: any = None
        self.right: any = None
        self.value: any = value
        self.id: any = id

class AVLNode:
    def __init__(self, value, id):
        self.left: any = None
        self.right: any = None
        self.height: any = 0
        self.value: any = value
        self.id: any = id


class Tree():
    def __init__(self, type):
        self.type = type

    def insert(self, root, data):
        # print("Inserting: ", data)
        if self.type == "Binary":
            return self.insertBinaryTree(root, data)
        if self.type == "AVL":
            return self.insertAVLTree(root, data)
        
    def insertBinaryTree(self, node, data):
        # print(">> Debugging (node, data): ",  node, " |", data )
        if not node:
            # print("Node inserted !",node)   
            return BinaryNode(data["value"], data["id"])     
        else:
            if data["value"] < node.value:
                node.left = self.insertBinaryTree(node.left, data)
            else:
                node.right = self.insertBinaryTree(node.right, data)
        return node

#################################    

    def rightRotate(self, node):
        y = node.left
        T3 = y.right

        y.right = node
        node.left = T3

        node.height = self.nodeHeight(node)
        y.height = self.nodeHeight(y)

        return y
        
    def leftRotate(self, node):
        y = node.right
        T2 = y.left

        y.left = node
        node.right = T2

        node.height = self.nodeHeight(node)
        y.height = self.nodeHeight(y)

        return y
        
    def nodeHeight(self, node):
        if(node == None):
            return 0
        return 1+max(self.nodeHeight(node.right), self.nodeHeight(node.left))

    def insertAVLTree(self, node, data):
        if not node:
            return AVLNode(data["value"], data["id"])      
        else:
            if data["value"] < node.value:
                node.left = self.insertAVLTree(node.left, data)
            else:
                node.right = self.insertAVLTree(node.right, data)

            node.height = self.nodeHeight(node)

            balance = self.nodeHeight(node.left) - self.nodeHeight(node.right)
            if(balance > 1):
                # Left Left
                if(data["value"] < node.left.value):
                    return self.rightRotate(node)
                # Left Right
                else:
                    node.left = self.leftRotate(node.left)
                    return self.rightRotate(node)
            elif (balance < -1):
                # Right Right
                if(data["value"] > node.right.value):
                    return self.leftRotate(node)
                # Right Left
                else:
                    node.right = self.rightRotate(node.right)
                    return self.leftRotate(node)
            return node

    def defineNeighborsByValue(self, node, neighbors={}):
        """
        Returns a dictionary where the value of the node is the key
        """
        if node != None:
            neighbors[node.value] = []
            if(node.left != None):
                neighbors[node.value].append({"id":node.left.id, "data": node.left.value})
            else:
                neighbors[node.value].append({"id": None, "data": None})
            if(node.right != None):
                neighbors[node.value].append({"id":node.right.id, "data": node.right.value})
            else:
                neighbors[node.value].append({"id": None, "data": None})
            self.defineNeighborsByValue(node.left, neighbors)
            self.defineNeighborsByValue(node.right, neighbors)
        return neighbors
    def defineNeighborsByID(self, node, neighbors={}):
        """
        Returns a dictionary where the id of the node is the key
        """
        if node != None:
            neighbors[node.id] = []
            if(node.left != None):
                neighbors[node.id].append({"id":node.left.id, "data": node.left.value})
            else:
                neighbors[node.id].append({"id": None, "data": None})
            if(node.right != None):
                neighbors[node.id].append({"id":node.right.id, "data": node.right.value})
            else:
                neighbors[node.id].append({"id": None, "data": None})
            self.defineNeighborsByID(node.left, neighbors)
            self.defineNeighborsByID(node.right, neighbors)
        return neighbors


if __name__=='__main__':
        
    tree = Tree("Binary")
    # elements = [5,2,6,1,10,8,7]

    elements = [
        {"id":1, "value": 5},
        {"id":2, "value": 2},
        {"id":3, "value": 6},
        {"id":4, "value": 1},
        {"id":5, "value": 10},
        {"id":6, "value": 8},
        {"id":7, "value": 7},
    ]

    root = None

    for element in elements:
        print(">> Inserting element:", element)
        root = tree.insert(root, element)

    tree.root = root

    other_rep2 = tree.defineNeighborsByValue(tree.root, {})
    print("\n\n_____________________________________\n\n")
    print(other_rep2)
    #########################
    tree = Tree("AVL")

    # elements = [
    #     {"id":1, "value": 7},
    #     {"id":2, "value": 6},
    #     {"id":3, "value": 5},
    #     {"id":4, "value": 4},
    #     {"id":5, "value": 3},
    #     {"id":6, "value": 2},
    #     {"id":7, "value": 1},
    # ]

    elements = [
        {"id":1, "value": 5},
        {"id":2, "value": 2},
        {"id":3, "value": 6},
        {"id":4, "value": 1},
        {"id":5, "value": 10},
        {"id":6, "value": 8},
        {"id":7, "value": 7},
    ]


    root = None

    for element in elements:
        print(">> Inserting element:", element)
        root = tree.insert(root, element)

    tree.root = root

    other_rep2 = tree.defineNeighborsByValue(tree.root, {})
    print("\n\n_____________________________________\n\n")
    print(other_rep2)