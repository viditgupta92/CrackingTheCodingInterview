class node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def in_order_print(root):
    if root != None:
        in_order_print(root.left)
        print(root.data)
        in_order_print(root.right)

def create_minimum_BST(arr, low, high):
    if low > high:
        return None
    mid = int((low+high)/2)
    n = node(arr[mid])
    n.left = create_minimum_BST(arr, low, mid-1)
    n.right = create_minimum_BST(arr, mid+1, high)
    return n

def create_min_tree(arr):
    n =create_minimum_BST(arr, 0, len(arr) - 1)
    return n

in_order_print(create_min_tree([2,4,6,8,10,12]))

