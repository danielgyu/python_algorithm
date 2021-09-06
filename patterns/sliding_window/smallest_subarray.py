def solution(array: list, k: int) -> int:
    window_start = 0
    window_sum = 0
    min_length = 100

    for window_end in range(len(array)):
        window_sum += array[window_end]
    
        while window_sum >= k:
            min_length = min(min_length, window_end - window_start + 1)

            window_sum -= array[window_start]
            window_start += 1

    return min_length

print(solution([2, 1, 5, 2, 3, 2], 7))
print(solution([2, 1, 5, 2, 8], 7))
print(solution([3, 4, 1, 1, 6], 8))
