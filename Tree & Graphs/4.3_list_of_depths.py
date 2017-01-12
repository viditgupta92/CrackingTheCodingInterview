class node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def bin_add(root,item):
    if root == None:
        root = item
    else:
        if item.data < root.data:
            if root.left == None:
                root.left = item
            else:
                bin_add(root.left, item)
        else:
            if root.right == None:
                root.right = item
            else:
                bin_add(root.right, item)

class node_l:
    def __init__(self):
        self.data = None
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = node_l()
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


def create_level_linked_lists(root, lst, lev):
    if root == None:
        return
    if len(lst) == lev:
        l = linked_list()
        lst.append(l)
    else:
        l = lst[lev]
    l.add_node(root.data)
    create_level_linked_lists(root.left, lst, lev+1)
    create_level_linked_lists(root.right, lst, lev+1)

def list_of_depths_1(root):
    lst = []
    create_level_linked_lists(root, lst, 0)
    return lst

def list_of_depths_2(root):
    lst = []
    cur = linked_list()
    if root != None:
        cur.add_node(root)
    temp = cur.head
    ctr = 0
    while temp:
        ctr += 1
        temp = temp.next
    while ctr > 0:
        lst.append(cur)
        par = cur
        cur = linked_list()
        while par != None:
            if par.left != None:
                cur.add_node(par.left)
            if par.right != None:
                cur.add_node(par.right)
            par = par.next
    return lst

def print_lists(lst):
    for ind,val in enumerate(lst):
        print("Level %d:" %(ind))
        val.list_print()

n = node(8)
bin_add(n,node(2))
bin_add(n,node(4))
bin_add(n,node(6))
bin_add(n,node(10))
bin_add(n,node(12))
print_lists(list_of_depths_2(n))