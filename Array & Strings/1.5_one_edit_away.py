def insert_delete(str1,str2,l2):
    flag = 0
    i = 0
    for j in range(l2):
        if str1[i] != str2[j]:
            if flag == 1:
                flag = 0
                break
            flag = 1
            j += 1
        else:
            i += 1
    return flag

def replace(str1,str2,l1):
    flag = 0
    for i in range(l1):
        if str1[i] != str2[i]:
            if flag == 1:
                flag = 0
                break
            flag = 1
    return flag


def one_edit_away_1(str1,str2):
    l1 = len(str1)
    l2 = len(str2)
    if l2 - l1 == 1:
        print(insert_delete(str1,str2,l2))
    elif l1 - l2 == 1:
        print(insert_delete(str2,str1,l1))
    elif l1 - l2 == 0:
        print(replace(str1,str2,l1))
    else:
        return 0

def one_edit_away_2(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    ind1 = 0
    ind2 = 0
    flag = 0
    if abs(l1 - l2) != 0 and abs(l1 - l2) != 1:
        print(flag)
        exit()
    while ind1 < l1 and ind2 < l2:
        if str1[ind1] != str2[ind2]:
            if flag == 1:
                flag = 0
                break
            else:
                flag = 1
                if l1 > l2:
                    ind1 += 1
                else:
                    ind2 += 1
        else:
            ind1 += 1
            ind2 += 1
    print(flag)



#one_edit_away_1("ple","pale") #insert
#one_edit_away_1("pale","ple") #delete
#one_edit_away_1("pale","rale") #replace

#one_edit_away_2("ple","pale") #insert
#one_edit_away_2("pale","ple") #delete
one_edit_away_1("pale","rale") #replace
