def solution(array: list) -> bool:
    if len(array) == 1:
        return False

    seen = set()
    for a in array:
        if a in seen:
            return True
        else:
            seen.add(a)

    return False

print(solution([1,2,3,1]))
print(solution([1,2,3,4]))
print(solution([1,1,1,3,3,4,3,2,4,2]))
