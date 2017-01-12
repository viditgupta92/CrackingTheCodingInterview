import collections

dic_1 = collections.OrderedDict()
dic_2 = collections.OrderedDict()

dic_1 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
       11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
       18: 'eighteen', 19: 'nineteen'}

dic_2 = {2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninty'}

def num_to_string(num):
    temp = num
    if int(temp/1000) > 0:
        if int(temp/1000) < 10:
            print(dic_1[int(temp/1000)], end = " ")
            temp = int(str(temp)[1:])
        elif int(temp / 1000) < 20:
            print(dic_1[int(temp / 1000)], end=" ")
            temp = int(str(temp)[2:])
        else:
            num_to_string(int(str(temp)[:2]))
            temp = int(str(temp)[2:])
        print("thousand", end = " ")
    if int(temp/100) > 0:
        print(dic_1[int(temp/100)], end = " ")
        print("hundred", end = " ")
        if temp%100 != 0:
            temp = int(str(temp)[1:])
        else:
            return
    if int(temp/10) > 0:
        if temp < 20:
            print(dic_1[temp], end = " ")
        elif temp % 10 == 0:
            print(dic_2[int(temp/10)], end = " ")
        else:
            print(dic_2[int(temp/10)], end  = " ")
            if temp%10 != 0:
                temp = int(str(temp)[1:])
            else:
                return
    if temp < 10 and temp > 0:
        print(dic_1[temp], end = " ")

num_to_string(99999)