def replace_spaces(str,length):
    ctr = 0
    arr = []
    for i in range(len(str)):
        arr.append(str[i])
    for i in range(length):
        if arr[i] == " ":
            ctr += 1

    ind = length + (ctr*2) - 1
    for i in range(length - 1,-1,-1):
        if arr[i] == " ":
            arr[ind] = '0'
            arr[ind - 1] = '2'
            arr[ind - 2] = '%'
            ind -= 3
        else:
            arr[ind] = arr[i]
            ind -= 1

    print(''.join(arr))

replace_spaces("Mr John Smith    ",13)