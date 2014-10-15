from random import *
import collections.abc

class BSTNode:
    
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val
    
    def setLeft(self, left):
        self.left = left
    
    def setRight(self, right):
        self.right = right
    
    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def __iter__(self):
        """
        Inorder traversal of a tree
        """
        if (self.left):
            for i in self.left:
                yield i
        
        yield self.value
        
        if (self.right):
            for i in self.right:
                yield i

    def __str__(self):
        return '{ Node : ' + str(self.value) + ', left : ' + str(self.left) + ', right : ' + str(self.right) + ' }\n'

class BST(collections.abc.Container):

    def __init__(self):
        self.root = None

    def insert(self, val):
        if(self.root == None):
            node = BSTNode(val)
            self.root = node
        else:
            node = self.root
            while (node != None):
                if (val < node.value):
                    if (node.left is None):
                        node.left = BSTNode(val)
                        break
                    node = node.left
                else:
                    if (node.right is None):
                        node.right = BSTNode(val)
                        break
                    node = node.right
    
    def __contains__(self, val):
        node = self.root
        while(node != None):
            if(val == node.value):
                return True
            elif(val < node.value):
                node = node.left
            else:
                node = node.right
        return False

    def __iter__(self):
        for i in self.root:
            yield i

    def __str__(self):
        return str(self.root)

def treesort(xs):
    bst = BST()
    for n in xs:
        bst.insert(n)
    return [i for i in bst]

if __name__ == '__main__':
    print(treesort(sample(range(200), 100)))
