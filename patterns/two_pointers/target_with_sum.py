def solution(array: list, target: int) -> list:
    res = []
    lp, rp = 0, len(array) - 1

    while lp < rp:
        if array[lp] + array[rp] == target:
            return [lp, rp]
        elif array[lp] + array[rp] > target:
            rp -= 1
        else:
            lp += 1

    return res


array, target = [1, 2, 3, 4, 6], 6
print(solution(array, target))
assert solution(array, target) == [1, 3]
array, target = [2, 5, 9, 11], 11
print(solution(array, target))
assert solution(array, target) == [0, 2]
