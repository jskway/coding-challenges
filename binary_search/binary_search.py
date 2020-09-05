def binary_search(arr, target):
    if len(arr) == 0:
        return -1

    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + high) // 2

        if arr[middle] == target:
            return middle

        if arr[middle] < target:
            low = middle + 1

        if arr[middle] > target:
            high = middle - 1

    return -1
