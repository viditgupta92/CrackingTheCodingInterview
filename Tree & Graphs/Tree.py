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

def in_order_print(root):
    if root != None:
        in_order_print(root.left)
        print(root.data)
        in_order_print(root.right)

def pre_order_print(root):
    if root != None:
        print(root.data)
        pre_order_print(root.left)
        pre_order_print(root.right)

def post_order_print(root):
    if root != None:
        post_order_print(root.left)
        post_order_print(root.right)
        print(root.data)

# n = node(4)
# bin_add(n,node(3))
# bin_add(n,node(6))
# bin_add(n,node(5))
# bin_add(n,node(8))
# bin_add(n,node(1))
# bin_add(n,node(7))
n = node(25)
bin_add(n,node(19))
bin_add(n,node(12))
bin_add(n,node(4))
bin_add(n,node(22))
bin_add(n,node(23))
bin_add(n,node(37))
bin_add(n,node(29))
bin_add(n,node(30))

in_order_print(n)
#pre_order_print(n)
#post_order_print(n)

