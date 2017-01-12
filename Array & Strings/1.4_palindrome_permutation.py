import collections
def palindrome_permutation(str):
    dict = collections.OrderedDict()
    str = str.lower()
    str = str.replace(" ","")
    ctr = 0
    for i in range(len(str)):
        if str[i] not in dict:
            dict[str[i]] = 1
        else:
            dict[str[i]] += 1
        if dict[str[i]] %2 == 1:
            ctr += 1
        else:
            ctr -= 1
    if ctr == 1:
        print(1)
    else:
        print(0)

#palindrome_permutation("tactcoapapa")
palindrome_permutation("Tact Coa")