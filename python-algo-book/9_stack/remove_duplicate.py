# https://leetcode.com/problems/remove-duplicate-letters/

def remove_duplicates(s):
    """
    Lexicographical order를 찾아야 하는 문제이다.
    재배치하는 것이 아니라, 주어진 s에서 알파벳을 제거해서 완성을 해야한다.
    순서를 제대로 만들기 위해 우리는,
    I) 포함된 알파벳 모두 한번씩 포함되야 하고,
    II) 전체적인 s의 순서를 제일 작게 해야 한다(e.g. 'adcb' > 'aczz')
    """
    from collections import Counter
    
    counter, stack, seen = Counter(s), [], set()

    for char in s:
        counter[char] -= 1
        if char in seen:
            continue
        
        """
        가장 핵심적인 while 문이다. 조건들을 살펴보자.
        1) stack 
        -> index out of range를 방지하기 위한 사전 확인
        2) char < stack[-1]
        -> 전체적인 순서를 위해, 자신보다 큰 알파벳들은 제거한다(II조건).
        3) counter[stack[-1]] > 0
        -> 하지만 조건은 해당 알파벳이 추후에도 나와야한다(I조건).
        """
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)

    return ''.join(stack)


s = 'cbacdcbc'
s1 = 'bcabc'

print(remove_duplicates(s))

"""추가
'cbacdcbc'를 언뜻보면, 답인 'acdb'가 이해 안될 수 있다.
c가 가장 많이 출현하는데, 두번째에 위치한다.
그 이유는 아무리 네번 나온다 하더라도, d가 한번 나오기 때문에,
d가 스택에 추가되고 한번 밖에 존재하지 않는 이상,
d앞에 알파벳은 그 앞에 나온걸로 끝이다. 왜냐하면 d의 자리는 고정이기 때문이다.
"""