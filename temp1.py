# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S, K):
    # write your code in Python 2.7
    S = S.upper()
    length = len(S)
    lst = []
    ctr = 0
    for i in range(length):
        if S[i] == "-":
            ctr += 1
        else:
            lst.append(S[i])
    l = length - ctr
    grps = int(l / K)
    diff = -1
    if l % K != 0:
        diff = l % K
    high = l + (grps - 1)
    res = []
    j = 0
    ind = 0

    for i in range(high):
        if grps - 1 > 0 and (i == diff
                             or (i % K == ind and i != 0)):
            res.append("-")
            grps -= 1
            ind += 1
        else:
            res.append(lst[j])
            j += 1
    return "".join(res)

