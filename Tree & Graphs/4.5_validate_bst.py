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

def in_order_traversal(root,arr):
    if root != None:
        in_order_traversal(root.left, arr)
        arr.append(root.data)
        in_order_traversal(root.right, arr)

def check_sorting(arr):
    flag = 1
    for i in range(1,len(arr),1):
        if arr[i] < arr[i-1]:
            flag = 0
            break
    return flag

def check_balanced_1(root):
    arr = []
    in_order_traversal(root,arr)
    print(check_sorting(arr))

last_val = None
def check_balanced_2(root):
    global last_val
    if root == None:
        return True
    if not check_balanced_2(root.left):
        return False
    if last_val != None and root.data <= last_val:
        return False
    last_val = root.data
    if not check_balanced_2(root.right):
        return False
    return True

def check_bst(n, min, max):
    if n == None:
        return True

    if (min != None and n.data <= min) or (max != None and n.data >= max):
        return False

    if (not check_bst(n.left, min, n.data)) or (not check_bst(n.right, n.data, max)):
        return False

    return True

def check_balanced_3(root):
    res = check_bst(root, None, None)
    return res

n = node(8)
bin_add(n,node(2))
bin_add(n,node(4))
bin_add(n,node(6))
bin_add(n,node(10))
bin_add(n,node(12))

#check_balanced_1(n)
#print(check_balanced_2(n))
print(check_balanced_3(n))