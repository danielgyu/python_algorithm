def solution(word: str) -> int:
    left, right = list(word), []
    
    while left:
        if right and left[-1] == right[-1]:
            left.pop()
            right.pop()
        else:
            p = left.pop()
            right.append(p)

    return 0 if right else 1


print(solution("baabaa"))
print(solution("cdcd"))
print(solution("bcdeaaedcb"))
print(solution("bcdeaaedcbf"))
