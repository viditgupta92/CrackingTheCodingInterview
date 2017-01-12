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

def reverse_list(l):
    head = None
    while l != None:
        n = node()
        n.data = l.data
        n.next = head
        head = n
        l = l.next
    return head


def palindrome_check(l):
    l1 = reverse_list(l)
    flag = 1
    while l != None or l1 != None:
        if l.data != l1.data:
            flag = 0
            break
        l = l.next
        l1 = l1.next
    print(flag)

l = linked_list()
# l.add_node(0)
# l.add_node(1)
# l.add_node(2)
# l.add_node(1)
# l.add_node(0)
l.add_node(0)
l.add_node(1)
l.add_node(2)
l.add_node(1)
l.add_node(0)
palindrome_check(l.head)