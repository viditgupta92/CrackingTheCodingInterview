# Given a string A which is a key of alphanumeric characters with dashes in between and an integer K.
# Rearrange the dashes in the string so that the whole string(should be uppercase) is divided into groups of K length each, and in case
# the whole alphanumeric string can't be divided into groups of K, then only the first group should be of a shorter length

# e.g "2-4AOr7-4k", 3  --> "24-AOR-74K"
# e.g "2-4AOr7-4k", 4  --> "24AO-R74K"
# e.g "r",1 -> "R"

def Solution(A,K):
    A = A.upper()
    length = len(A)
    ctr = 0
    lst = []
    for i in range(length):
        if A[i] == "-":
            ctr += 1
        else:
            lst.append(A[i])
    div = int(len(lst)/K)
    diff = -1
    if len(lst)%K == 0:
        dash = div - 1
    else:
        dash = div
        diff = len(lst) % K
    l = len(lst) + dash
    grp_l = 0
    j = 0
    res = []
    for i in range(l):
        if dash > 0 and (i == diff or (grp_l / K == 1)):
            res.append("-")
            grp_l = 0
            dash -= 1
        else:
            grp_l += 1
            res.append(lst[j])
            j += 1
    return "".join(res)

print(Solution("2-4AOr7-4k", 3))
print(Solution("r", 1))
print(Solution("-------4tye2-90", 3))
