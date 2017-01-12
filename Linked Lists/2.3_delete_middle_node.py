class node:
    def __init__(self):
        self.data = None
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = node()
        new_node.data = data
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node

    def list_print(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

def delete_middle_node(node):
    if node == None or node.next == None:
        return False
    else:
        n = node.next
        node.data = n.data
        node.next = n.next

l = linked_list()
l.add_node(1)
l.add_node(2)
l.add_node(3)
l.add_node(4)
l.add_node(5)
delete_middle_node(l.head.next.next)
l.list_print()