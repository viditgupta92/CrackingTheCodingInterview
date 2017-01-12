def sparse_search(arr,item,first,last):
    if first > last:
        return -1
    mid = int((first + last)/2)
    if arr[mid] == "":
        left = mid - 1
        right = mid + 1
        while True:
            if left < first and right > last:
                return -1
            elif right <= last and arr[right] != "":
                mid = right
                break
            elif left >= first and arr[left] != "":
                mid = left
                break
            right += 1
            left -= 1
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            return sparse_search(arr, item, mid + 1, last)
        else:
            return sparse_search(arr, item, first, mid - 1)

def search(arr,item):
    if arr == "" or item == "":
        return  -1
    print(sparse_search(arr, item, 0, len(arr) - 1))

search(["at","","ball","","","","cat","","","dog"], "cat")
