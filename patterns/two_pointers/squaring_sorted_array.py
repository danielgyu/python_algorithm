from collections import deque

def solution(array: list) -> list:
    left, right = 0, len(array) - 1
    result = deque()

    while left <= right:
        if array[left] ** 2 > array[right] ** 2:
            result.appendleft(array[left] ** 2)
            left += 1
        else:
            result.appendleft(array[right] ** 2)
            right -= 1

    return list(result)


print(solution([-2, -1, 0, 2, 3]))
print(solution([-3, -1, 0, 1, 2]))
