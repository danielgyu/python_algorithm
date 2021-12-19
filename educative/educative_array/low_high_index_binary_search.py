def find_low_index(arr, key):
    index = -1
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] >= key:
            high = mid - 1
        else:
            low = mid + 1
        
        if arr[mid] == key:
            index = mid

    return index

def find_high_index(arr, key):
    index = -1
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] <= key:
            low = mid + 1
        else:
            high = mid - 1

        if arr[mid] == key:
            index = mid

    return index

def solution_low_index(arr, key):
  low = 0
  high = len(arr) - 1
  mid = int(high / 2)

  while low <= high:

    mid_elem = arr[mid]

    if mid_elem < key:
      low = mid + 1
    else:
      high = mid - 1

    mid = low + int((high - low) / 2)

  if low < len(arr) and arr[low] == key:
    return low

  return -1

def solution_high_index(arr, key):
    low = 0
    high = len(arr) - 1
    mid = high // 2

    while low <= high:
        
        if arr[mid] <= key:
            # high = mid - 1
            low = mid + 1
        else:
            # low = mid + 1
            high = mid - 1

        mid = (low + high) // 2

    if high < len(arr) and arr[high] == key:
        return high

    return - 1


if __name__ == "__main__":
    array = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
    print("low index: ", array.index(5))
    print(find_low_index(array, 5))

    # print(find_high_index(array, 0, len(array) - 1, 5))

    array2 = [1, 2, 2, 3, 3, 4, 5, 5, 6]
    print("low index: ", array2.index(5))
    print(find_low_index(array2, 5))

    array3 = [1, 3, 4, 5, 5, 6]
    print("low index: ", array3.index(3))
    print(find_low_index(array3, 3))

    array4 = [1, 2, 2]
    print("low index: ", array4.index(2))
    print(find_low_index(array4, 2))

    array5 = [1, 2, 4, 5, 5, 9, 10]
    print("low index: ", array5.index(5))
    print(find_low_index(array5, 5))
    print("high index:  4")
    print(find_high_index(array5, 5))
