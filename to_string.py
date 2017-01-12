import collections
dic = collections.OrderedDict()
two_digit_dic = collections.OrderedDict()
dic = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
       11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
       18: 'eighteen', 19: 'nineteen'}
two_digit_dic = {2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninty'}
def two_digits(num,lst):
    if num < 20:
        return dic[num]
    else:
        if num % 10 == 0:
            res = two_digit_dic[lst[1]]
        else:
            res = two_digit_dic[lst[1]] + " " + dic[lst[0]]
        return res

def three_digits(num,lst):
    res = dic[lst[2]] + " hundred " + two_digits(int(str(num)[1:]), lst[:(len(lst) - 1)])
    return res

def num_to_string(num):
    temp = num
    ctr = 0
    lst = []
    while temp != 0:
        lst.append(temp % 10)
        temp = int(temp/10)
        ctr += 1

    digits = len(lst)
    if digits ==1:
        res = dic[lst[0]]
    elif digits == 2:
        res = two_digits(num,lst)
    elif digits == 3:
        res = three_digits(num,lst)
    # elif digits == 4:
    #     four_digits(lst)
    # elif digits == 5:
    #     five_digits(lst)
    return res

#num_to_string(4)
print(num_to_string(659))