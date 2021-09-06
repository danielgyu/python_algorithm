from collections import deque


def solution(array:list, k: int) -> int:
    window_start = 0
    window_sum, max_sum = 0, 0

    for window_end in range(len(array)):
        window_sum += array[window_end]

        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum) 
            window_sum -= array[window_start]
            window_start += 1
            
    return max_sum

print(solution([2, 1, 5, 1, 3, 2], 3))
print(solution([2, 1, 4, 3, 9, 10], 3))
