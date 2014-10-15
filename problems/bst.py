
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None # left child
        self.right = None # right child

class BST:
    def __init__(self, data):
        self.root = Node(data);
    def insert(self, data):
        node = self.root
        while(node is not None):
            if(data < node.data):
                node = node.left
            else:
                node = node.right
        node = Node(data)
    
    def search(self, data):
        node = self.root
        while(node.data != data):
            if(data < node.data):
                node = node.left
            else:
                node = node.right
            if (node is None) :
                return None
        return node.data

bst = BST(0)
bst.insert(7)
bst.insert(9)
bst.insert(10)

print bst.search(10)
