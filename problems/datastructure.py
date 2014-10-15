
class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    def attach_prev(self, prev_node):
        self.prev = prev_node
    def attach_next(self, next_node):
        self.next = next_node

class DLL:
    
    def __init__(self, head=None, last=None):
        self.head = head
        self.last = last
    
    def search(self, data):
        node = self.root
        while(node is not None):
            if(data == node.data):
                return node
            else:
                node = node.next
    
    def insert_before(self, node, ins_node):
        if(node.prev is None):
            self.head = ins_node
        node.prev = ins_node
    
    def insert_after(self, node, ins_node):
        if(node.next is None):
            self.last = ins_node
        node.next = ins_node
    
    def insert_beginning(self, node):
        node.next = self.head
        if(self.head is not None):
            self.head.prev = node
        self.head = node

    def remove(self, node):
        if(node.prev is None):
            self.head = node.next
        else:
            node.prev.next = node.next
        if(node.next is None):
            self.last = node.prev
        else:
            node.next.prev = node.prev


