import collections
def check_permutation_1(str1, str2):
    flag = 1
    if len(str1) != len(str2):
        flag = 0
    str1 = sorted(str1)
    str2 = sorted(str2)
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            flag = 0
            break
    print(flag)

def check_permutation_2(str1, str2):
    flag = 1
    dict = collections.OrderedDict()
    if len(str1) != len(str2):
        flag = 0
    for i in range(len(str1)):
        if str1[i] not in dict:
            dict[str1[i]] = 1
        else:
            dict[str1[i]] += 1
    for i in range(len(str2)):
        dict[str2[i]] -= 1
        if dict[str2[i]] < 0:
            flag = 0
            break
    print(flag)


check_permutation_2("vidit","tidiv")


