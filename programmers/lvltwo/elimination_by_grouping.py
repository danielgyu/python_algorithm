def solution(word: str) -> int:
    i = 0
    while True:
        if i >= len(word) - 1:
            return 0 if word else 1
        if word[i] == word[i+1]:
            word = word[:i] + word[i+2:]
            i = 0
            continue
        i += 1

print(solution("baabaa"))
print(solution("cdcd"))
print(solution("bcdeaaedcb"))
