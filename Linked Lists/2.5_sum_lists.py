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

def sum_lists_backward_order(n1, n2,carry):
    if n1 == None and n2 == None:
        return None
    res = node()
    val = carry
    if n1 != None:
        val += n1.data
    if n2 != None:
        val += n2.data
    res.data = val % 10
    if n1 != None or n2 != None:
        temp = sum_lists_backward_order(None if n1 == None else n1.next, None if n2 == None else n2.next, 1 if val >= 10 else 0)
        res.next = temp
    return res

#def sum_lists_forward_order(n1, n2, carry):


def print_list(h):
    while h != None:
        print(h.data, end = " ")
        h = h.next

l1 = linked_list()
l1.add_node(7)
l1.add_node(1)
l1.add_node(6)
l2 = linked_list()
l2.add_node(5)
l2.add_node(9)
l2.add_node(2)
h = sum_lists_backward_order(l1.head, l2.head, 0)
print_list(h)
