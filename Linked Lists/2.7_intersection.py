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

class result():
    def __init__(self, size, tail):
        self.tail = tail
        self.size = size

def get_length_and_tail(n):
    ctr = 0
    while n != None:
        ctr += 1
        if n.next == None:
            tail = n
        n = n.next
    r = result(ctr, tail)
    return r

def intersection(n1,n2):
    res1 = get_length_and_tail(n1)
    res2 = get_length_and_tail(n2)

    if res1.tail != res2.tail:
        return False

    shorter = n1 if res1.size < res2.size else n2
    longer = n2 if res1.size > res2.size else n1

    diff = abs(res1.size - res2.size)
    ctr = 0
    while(ctr < diff):
        longer = longer.next
        ctr += 1

    while longer != shorter:
        shorter = shorter.next
        longer = longer.next

    print(longer.data)

l1 = linked_list()
l1.add_node(1)
l1.add_node(2)
l1.add_node(3)

l2 = linked_list()
l2.add_node(4)
l2.add_node(5)
l2.add_node(6)
l2.head.next.next.next = l1.head

l3 = linked_list()
l3.add_node(7)
l3.add_node(8)
l3.add_node(9)
l3.head.next.next.next = l1.head

intersection(l2.head,l3.head)