def merge(arr, helper, low, mid, high):
    for i in range(low, high+1, 1):
        helper[i] = arr[i]
    helper_left = low
    helper_right = mid + 1
    current = low
    while helper_left <= mid and helper_right <= high:
        if helper[helper_right] < helper[helper_left]:
            arr[current] = helper[helper_right]
            helper_right += 1
        else:
            arr[current] = helper[helper_left]
            helper_left += 1
        current += 1
    rem = mid - helper_left
    for i in range(rem+1):
        arr[current+i] = helper[helper_left + i]

def merge_sort(arr, helper, low, high):
    if low < high:
        mid = int((low + high)/2)
        merge_sort(arr, helper, low, mid)
        merge_sort(arr, helper, mid + 1, high)
        merge(arr, helper, low, mid, high)

def sorted_array(arr):
    low = 0
    high = len(arr) - 1
    helper = []
    for i in range(high + 1):
        helper.append(0)
    merge_sort(arr, helper, low, high)
    return arr

def peak_and_valleys(arr):
    sort = sorted_array(arr)
    ind = 1
    for i in range(ind,len(sort),2):
        t = arr[i]
        arr[i] = arr[i-1]
        arr[i-1] = t
    for each in range(len(arr)):
        print(arr[each], end = " ")

peak_and_valleys([5,4,3,2,1])


