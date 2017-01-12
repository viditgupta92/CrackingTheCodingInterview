def sub_string(s,item):
    ctr = 0
    i = 0
    sub = [each for each in item]
    while i < len(s):
        if s[i] == sub[ctr]:
            while i < len(s) and ctr < len(item) and (s[i] == sub[ctr]):
                i += 1
                ctr += 1
            if ctr == len(item):
                return True
            else:
                return False
        i += 1

def string_rotation(s1,s2):
    if len(s1) != len(s2):
        flag = 0
    s = s1 + s1
    flag = sub_string(s,s2)
    print(flag)

string_rotation("waterbottle","erbottlewat")