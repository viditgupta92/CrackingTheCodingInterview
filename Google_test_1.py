# def solution(S, K):
#     # write your code in Python 2.7
#     S = S.upper()
#     length = len(S)
#     lst = []
#     for i in range(length):
#         if S[i] == "-":
#             j = i - 1
#             ctr = 0
#             while j >= 0 or S[j] != "-":
#                 ctr += 1
#                 j -= 1
#             lst.append(ctr)
#     ctr = 0
#     for k in range(i, -1, -1):
#         ctr += 1
#         if S[k - 1] == "-":
#             break
#     lst.append(ctr)
#     num = sum(lst)
#     grps = int(num / K)
#     if num % K != 0:
#         diff = num % K
#     high = num + (grps - 1)
#     res = ""
#     for i in range(high):
#         if diff > 0:
#             res[i] =


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
    for i in range(high):
        if i == diff or (i + 1) % K == 0:
            res[i] == "-"
        else:
            res[i] = lst[j]
            j += 1
    return "".join(res)

solution("2-4AOr7-4k",4)

if grps - 1 > 0 and (i == diff or (i % K == ind and i!= 0)):


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
        grps += 1
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

