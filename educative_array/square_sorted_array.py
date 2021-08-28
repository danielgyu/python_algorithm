from collections import deque


def get_target_index(arr: list) -> int:
    i = 0
    while i < len(arr) - 1:
        if arr[i] < 0:
            i += 1
        else:
            break
    return i


def solution(arr: list) -> list:
    target_idx = get_target_index(arr)
    left = target_idx - 1
    right = target_idx
    res = []

    while left > 0 and right < len(arr):
        ln = arr[left] ** 2
        rn = arr[right] ** 2

        if ln < rn:
            res.append(ln)
            left -= 1
        else:
            res.append(rn)
            right += 1

    while left >= 0:
        res.append(arr[left] ** 2)
        left -= 1
    while right < len(arr):
        res.append(arr[right] ** 2)
        right += 1

    return res
        

if __name__ == "__main__":
    arr1 = [-3, -1, 0, 1, 2]
    arr2 = [-9, -6, -3]
    arr3 = [1, 3, 5]
    print(solution(arr1))
    print(solution(arr2))
    print(solution(arr3))
