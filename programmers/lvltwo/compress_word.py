import math

def solution(word):
    answer = math.inf if len(word) > 1 else 1

    for idx in range(1, len(word) // 2 + 1):
        left, compressed = 0, ""

        while left < len(word) - idx:
            count = 1

            while word[left:left+idx] == word[left+idx:left+idx+idx]:
                #breakpoint()
                count += 1
                left += idx

            if count > 1:
                compressed += f"{count}{word[left:left+idx]}"
            else:
                compressed += word[left:left+idx]
            
            left += idx

        compressed += word[left:]
        answer = min(answer, len(compressed))

    return answer

#print(solution("aabbaccc"))
#print(solution("ababcdcdababcdcd"))
#print(solution("abcabcdede"))
#print(solution("abcabcabcabcdededededede"))
#print(solution("xababcdcdababcdcd"))
print(solution("a"))
