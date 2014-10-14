class SLLNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class SLL:

    def __init__(self):
        self.root = None

    def insert(self, val):
        if(self.root is None):
            self.root = SLLNode(val)
        else:
            node = SLLNode(val)
            node.next = self.root
            self.root = node

    def delete(self, val):
        node = self.root
        prev = None
        while (node):
            if (node.val == val):
                if (prev):
                    prev.next = node.next
                else:
                    self.root = node.next
                break
            prev = node    
            node = node.next
        else:
            raise Exception("Value not found in list")

    def __str__(self):
        node = self.root
        l = []
        while(node):
            l.append(node.val)
            node = node.next
        return str(l)

if __name__ == '__main__':
    sll = SLL()
    for n in range(0, 10):
        sll.insert(n)
    sll.delete(1)
    print(sll)