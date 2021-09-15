def solution(array: list) -> int:
    non_dup, runner = 1, 1

    while runner < len(array):
        if array[non_dup - 1] != array[runner]:
            array[non_dup] = array[runner]
            non_dup += 1
        runner += 1

    return non_dup
    

print(solution([2, 3, 3, 3, 6, 9, 9]))
assert solution([2, 3, 3, 3, 6, 9, 9]) == 4
