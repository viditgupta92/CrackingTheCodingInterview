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

def return_kth_to_last(head,k):
    p1 = head
    p2 = head
    for i in range(k):
        if p1 != None:
            p1 = p1.next
        else:
            return(False)
    while p1 != None:
        p1 = p1.next
        p2 = p2.next
    return(p2.data)

l = linked_list()
l.add_node(1)
l.add_node(2)
l.add_node(3)
l.add_node(4)
print(return_kth_to_last(l.head,4))