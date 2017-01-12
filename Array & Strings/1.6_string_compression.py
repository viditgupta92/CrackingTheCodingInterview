def string_compression_1(arr):
    res = []
    num = 0
    for i in range(len(arr)):
        num += 1
        if i+1 == len(arr) or arr[i] != arr[i+1] :
            res.append(arr[i])
            res.append(str(num))
            num = 0
    if len(res) > len(arr):
        return(arr)
    else:
        return(''.join(res))

def compression_length(arr):
    ctr = 0
    num = 0
    for i in range(len(arr)):
        num += 1
        if i + 1 == len(arr) or arr[i] != arr[i + 1]:
            ctr += 1 + len(str(num))
            num = 0
    return ctr

def string_compression_2(arr):
    length = compression_length(arr)
    if length > len(arr):
        return arr
    else:
        res = []
        num = 0
        for i in range(len(arr)):
            num += 1
            if i + 1 == len(arr) or arr[i] != arr[i + 1]:
                res.append(arr[i])
                res.append(str(num))
                num = 0
        return (''.join(res))


#print(string_compression_1("aabcccccaaa"))
#print(string_compression_1("abcd"))
#print(string_compression_2("abcd"))
print(string_compression_2("aabcccccaaa"))
