"Link : Binary search"

def binary_search(arr, target):
    s, e = 0, len(arr) - 1
    
    while s <= e:
        mid = (s+e) // 2
        
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            s = mid + 1
        else:
            e = mid - 1
    return False

def binary_search_recursive(arr, target):
    if not len(arr):
        return False
        
    mid = (len(arr) -1) // 2

    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        return binary_search_recursive(arr[mid + 1:], target)
    else:
        return binary_search_recursive(arr[:mid], target)

print(binary_search_recursive([1,2], 2))
