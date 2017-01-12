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


def remove_dups_1(head):
    cur = head
    while cur != None:
        temp = cur
        while temp.next != None:
            if cur.data == temp.next.data:
                temp.next = temp.next.next
            else:
                temp = temp.next
        cur = cur.next

def remove_dups_2(head):
    cur = head
    while cur != None:
        temp = cur
        if temp.next.data == temp.data:
            temp = temp.next
        cur = cur.next



l1 =linked_list()
l1.add_node(1)
l1.add_node(2)
l1.add_node(2)
l1.add_node(3)
remove_dups_1(l1.head)
l1.list_print()