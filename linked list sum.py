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

def sum_lists(l1,l2,carry):
    if l1 == None or l2 == None:
        return None
    value = carry
    if l1 != None:
        value += l1.data
    if l2 != None:
        value += l2.data
    result = node()
    result.data = value % 10
    if l1 != None or l2 != None:
        temp = sum_lists(None if l1 == None else l1.next,None if l2 == None else l2.next,
                         1 if value >= 10 else 0)
        result.next = temp
    return result

l1 = linked_list()
l1.add_node(1)
l1.add_node(2)
l1.add_node(3)

l2 = linked_list()
l2.add_node(4)
l2.add_node(5)
l2.add_node(6)

sum_lists(l1.head,l2.head,0)


