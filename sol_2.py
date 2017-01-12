# Given a binary search tree T and a range [A..B] find subtrees which are contained in the range [A .. B]
# Tree T is of the format:
# x(data), l(left node/tree), r(right node/tree)

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

n = node(25)
bin_add(n,node(19))
bin_add(n,node(12))
bin_add(n,node(4))
bin_add(n,node(22))
bin_add(n,node(23))
bin_add(n,node(37))
bin_add(n,node(29))
bin_add(n,node(30))

def check_bst(n, min, max, lst):
    if n == None:
        return True

    l = check_bst(n.left, min, max, lst) if n.left != None else True
    r = check_bst(n.right, min, max, lst) if n.right != None else True

    if l and r and (n.data >= min and n.data <= max):
        lst.append(n.data)
        return True

    return False

def solution(A,B,T):
    lst = []
    l = check_bst(T,A,B,lst)
    return lst

res = solution(15, 29, n)
for each in res:
    print(each, end =" ")