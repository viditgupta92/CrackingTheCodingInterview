# Given an array A with 0<= ind < N, find any index P such that the sum of all elements to the left of P is equal to
# sum of all elements to the right of P. In case no such index exists return -1.
# Consider sum of non-existing elements as 0 i.e. for 0 or N-1 element
# e.g. [1,2,3,4,3,2,1] -> 3
# e.g. [1, -3, 2, 1] -> 0
def sum(arr, low, high):
    if low <0 or high <0:
        return 0
    else:
        s = 0
        for i in range(low, high + 1,1):
            s += arr[i]
        return s

def solution(A):
    # write your code in Python 2.7
    length = len(A)
    low = 0
    high = length - 1
    pivot = 0
    while pivot <= high:
        s1 = sum(A, low, pivot - 1)
        s2 = sum(A, pivot + 1, high)
        if s1 == s2:
            return pivot
        pivot += 1
    return -1

