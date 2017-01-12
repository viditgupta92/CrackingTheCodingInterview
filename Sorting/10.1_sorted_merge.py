def sorted_merge(a,b):
    ind_a = len(a) - 1
    ind_b = len(b) - 1
    ind = ind_a + ind_b + 1
    for i in range(ind_a+1,ind+1,1):
        a.append(-1)
    while ind_b >= 0:
        if a[ind_a] > b[ind_b]:
            a[ind] = a[ind_a]
            ind_a -= 1
        else:
            a[ind] = b[ind_b]
            ind_b -= 1
        ind -= 1
    sorted_array(a)

def sorted_array(arr):
    for i in range(len(arr)):
        print(arr[i], end = " ")

sorted_merge([1,3,5,7,9],[2,4])