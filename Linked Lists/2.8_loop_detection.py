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

def loop_detection(h):
    slow = h
    fast = h
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if fast == None or fast.next == None:
        return False
    slow = h
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow
l = linked_list()
l.add_node('A')
l.add_node('B')
l.add_node('C')
l.add_node('D')
l.add_node('E')
l.add_node('C')
print(loop_detection(l.head))