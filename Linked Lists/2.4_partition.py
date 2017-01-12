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

def partition_1(n, x):
    before_start = None
    before_end = None
    after_start = None
    after_end = None

    while n != None:
        if n.data < x:
            if before_start == None:
                before_start = node()
                before_start.data = n.data
                before_end = before_start
            else:
                new_node = node()
                before_end.next = new_node
                new_node.data = n.data
                before_end = new_node

        else:
            if after_start == None:
                after_start = node()
                after_start.data = n.data
                after_end = after_start
            else:
                new_node = node()
                after_end.next = new_node
                new_node.data = n.data
                after_end = new_node
        n = n.next

    if before_start.data == None:
        return after_start

    before_end.next = after_start
    return before_start

def partition_2(n,x):
    head = None
    tail = None
    while n != None:
        if head == tail == None:
            head = node()
            head.data = n.data
            tail = head
        elif n.data < x:
            new_node = node()
            new_node.data = n.data
            new_node.next = head
            head = new_node
        else:
            new_node = node()
            new_node.data = n.data
            tail.next = new_node
            tail = new_node
        n = n.next
    return head

def print_list(h):
    while h != None:
        print(h.data, end = " ")
        h = h.next

l = linked_list()
l.add_node(3)
l.add_node(5)
l.add_node(8)
l.add_node(5)
l.add_node(10)
l.add_node(2)
l.add_node(1)

#h = partition_1(l.head,5)
h = partition_2(l.head,2)
print_list(h)