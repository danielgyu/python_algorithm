# https://leetcode.com/problems/valid-parentheses/

def is_valid(s):
    """
    스택을 사용하는 아주 기본적인 문제라고 한다.
    이해 자체는 쉬운데, 몇가지 주의사항이 있다.
    """
    stack = []
    dic = {')':'(', ']':'[', '}':'{'}

    for st in s:
        if st in ['(', '{', '[']:
            stack.append(st)
        # stack이 없는 경우도 확인해줘야 한다
        elif (not stack) or (stack.pop() != dic[st]):
            return False

    # stack에 안 남아있는지도 확인해줘야 한다
    return len(stack) == 0
            

s = "{[]}"
print(is_valid(s))