# https://leetcode.com/problems/jewels-and-stones/
   
def numJewelsInStones(jewels: str, stones: str) -> int:
    answer, dic = 0, {}
    for j in stones:
        if j not in dic:
            dic[j] = 1
        else:
            dic[j] += 1

    for s in jewels:
        if s in dic:
            answer += 1

    return answer

def second(jewels, stones):
    return sum(s in jewels for s in stones)

jewels = "aA"
stones = "aAAbbbb"

print(numJewelsInStones(jewels, stones))
print(second(jewels, stones))