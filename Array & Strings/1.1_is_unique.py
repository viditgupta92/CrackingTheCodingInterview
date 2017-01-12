import collections
def is_unique(str):
    dict = collections.OrderedDict()
    flag = 1
    for i in range(len(str)):
        if str[i] in dict:
            flag = 0
        dict[str[i]] = True
    print(flag)

is_unique("terabyte")