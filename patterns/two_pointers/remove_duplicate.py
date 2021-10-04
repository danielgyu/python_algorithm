def solution(array: list) -> int:
    non_dup, runner = 1, 1

    while runner < len(array):
        if array[non_dup - 1] != array[runner]:
            array[non_dup] = array[runner]
            non_dup += 1
        runner += 1

    return non_dup

def example_one(array: list, n: int) -> int:
    next_element = 0
    for i in range(len(array)):
        if array[i] != n:
            array[next_element] = array[i]
            next_element += 1

    print(f"ex one array: {array}")
    return next_element


print(solution([2, 3, 3, 3, 6, 9, 9]))
assert solution([2, 3, 3, 3, 6, 9, 9]) == 4

print(example_one([3, 2, 3, 6, 3, 10, 9, 3], 3))
assert example_one([3, 2, 3, 6, 3, 10, 9, 3], 3) == 4
