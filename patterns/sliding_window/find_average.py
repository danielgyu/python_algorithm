from collections import deque

def find_averages_of_subarrays(k: int, array: list) -> list:
    res, window = [], deque()
    
    # initialize window
    for i in range(k):
        window.append(array[i])
    res.append(sum(window) / k)

    # calculate rest of the array
    for j in range(1, len(array) - k + 1):
        window.popleft()
        window.append(array[j + k - 1])
        res.append(sum(window) / k)

    return res

print("array: [1, 3, 2, 6, -1, 4, 1, 8, 2]")
print(find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]))
