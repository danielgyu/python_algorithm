def binary_search(lst: list, start: int, end: int, key: int) -> int:

    mid = end // 2
    
    if lst[mid] == key:
        return mid
    
    if (lst[start] <= lst[mid] and
            key <= lst[mid] and
            key >= lst[start]):
        return binary_search(lst, start, mid - 1, key)

    elif (lst[mid] <= lst[end] and
            key >= lst[mid] and
            key <= lst[end]):
        return binary_search(lst, mid + 1, end, key)

    elif lst[start] >= lst[mid]:
        return binary_search(lst, start, mid - 1, key)

    elif lst[end] <= lst[mid]:
        return binary_search(lst, mid + 1, end, key)

    return -1

def solution(lst: list, k: int) -> int:
    return binary_search(lst, 0, len(lst) - 1, k)

if __name__ == "__main__":
    v1 = [176, 188, 199, 200, 210, 222, 1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162]
    v2 = [6, 7, 1, 2, 3, 4, 5]
    print(solution(v2, 6))

