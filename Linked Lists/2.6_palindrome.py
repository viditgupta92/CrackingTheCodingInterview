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

def reverse_list(h):
    head = None
    while h != None:
        n = node()
        n.data = h.data
        n.next = head
        head = n
        h = h.next
    return head

def compare_list(h,nh):
    flag = 1
    while h != None and nh != None:
        if h.data != nh.data:
            flag = 0
            break
        h = h.next
        nh = nh.next
    return flag

def palindrome_1(head):
    new_head = reverse_list(head)
    print(compare_list(head,new_head))

def palindrome_2(head):
    slow_runner = head
    fast_runner = head
    top = None
    flag = 1
    # copy first half of list elements to a stack
    while fast_runner != None and fast_runner.next != None:
        n = node()
        n.data = slow_runner.data
        if top == None:
            n.next = None
        else:
            n.next = top
        top = n
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next
    # in case number of elements in list are odd, skip middle element
    if fast_runner != None:
        slow_runner = slow_runner.next
    # compare each element of remaining list with the elements of stack
    while slow_runner != None and top!= None:
        if slow_runner.data != top.data:
            flag = 0
            break
        slow_runner = slow_runner.next
        top = top.next
    print(flag)

l  = linked_list()
l.add_node(0)
l.add_node(1)
l.add_node(3)
l.add_node(1)
l.add_node(0)
#palindrome_1(l.head)
palindrome_2(l.head)