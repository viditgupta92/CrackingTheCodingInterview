def binary_search(listy, low, high,x):
    while low <= high:
        mid = int((low + high) / 2)
        if x < listy[mid] or listy[mid] == -1:
            high = mid - 1
        elif x > listy[mid]:
            low = mid + 1
        else:
            return mid
    return -1

def sorted_search(listy,x):
    ind = 0
    while(ind < len(listy) and listy[ind] < x):
        if ind == 0:
            ind += 1
        else:
            ind *= 2
    print(binary_search(listy, 0, ind,x))

sorted_search([1,2,4,5,7,8,78],78)

