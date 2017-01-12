def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - (i+1)):
            if arr[j] > arr[j+1]:
                t = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = t
    sorted_array(arr)

def selection_sort(arr):
    for i in range(len(arr)):
        small = i
        for j in range(i+1,len(arr),1):
            if arr[j] < arr[small]:
                small = j
        t = arr[i]
        arr[i] = arr[small]
        arr[small] = t
    sorted_array(arr)

def merge(arr, helper, low, mid, high):
    for i in range(low,high+1,1):
        helper[i] = arr[i]
    helper_left = low
    helper_right = mid + 1
    current = low

    while helper_left <= mid and helper_right <= high:
        if helper[helper_left] < helper[helper_right]:
            arr[current] = helper[helper_left]
            helper_left += 1
        else:
            arr[current] = helper[helper_right]
            helper_right += 1
        current += 1

    rem = mid - helper_left
    for i in range(rem+1):
        arr[current + i] = helper[helper_left + i]

def merge_sort_halves(arr, helper, low, high):
    if low < high:
        mid = int((low + high) / 2)
        merge_sort_halves(arr, helper, low, mid)
        merge_sort_halves(arr, helper, mid+1, high)
        merge(arr, helper, low, mid, high)

def merge_sort(arr):
    helper = []
    length = len(arr)
    for i in range(length):
        helper.append(0)
    merge_sort_halves(arr, helper, 0, length - 1)
    sorted_array(arr)

def swap(arr,left,right):
    t = arr[left]
    arr[left] = arr[right]
    arr[right] = t

def partition(arr, left, right):
    pivot = arr[int((left + right) / 2)]
    while(left <= right):
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        swap(arr, left, right)
        left += 1
        right -=1
    return left

def quick_sort(arr, left, right):
    ind = partition(arr, left, right)
    if left < ind - 1:
        quick_sort(arr, left, ind - 1)
    if ind < right:
        quick_sort(arr, ind, right)
    sorted_array(arr)

def radix_sort(arr):
    RADIX = 10
    max_length = False
    tmp = -1
    placement = 1
    while not max_length:
        max_length = True
        buckets = [[] for _ in range(RADIX)]

        for each in arr:
            tmp = int(each/placement)
            buckets[tmp % RADIX].append(each)
            if max_length and tmp > 0:
                max_length = False

        ind = 0
        for each in range(RADIX):
            buck = buckets[each]
            for each in buck:
                arr[ind] = each
                ind += 1
        placement *= RADIX
    sorted_array(arr)

def sorted_array(arr):
    for i in range(len(arr)):
        print(arr[i], end = " ")

def binary_search(arr,item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if item < arr[mid]:
            high = mid -1
        elif item > arr[mid]:
            low = mid +1
        else:
            return mid+1
    return -1

#quick_sort([5,4,3,2,1],0,len([5,4,3,2,1]) - 1)
#print(binary_search([1,2,3,4,5],5))
#radix_sort([5,4,3,2,1,18,23,65])
#bubble_sort(['t','s','r','q'])