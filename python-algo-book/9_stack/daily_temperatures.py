# https://leetcode.com/problems/daily-temperatures/

def daily_temperatures(T):
    """
    온도가 올라가기까지 몇일이 걸리는지 구하는 문제이다.
    풀수 있는 다양한 방법이 있다. 가장 간단하게 T의 각 숫자마다 loop을 돌려서
    높은 숫자가 나오면 카운팅된 숫자를 append할 수 있다.
    이런 방식은 "미리 내다보기"이다. 오늘 숫자를 기준으로 미래에 언제 올라갈지 계사한다.

    여기서 사용하는 방식은 "미래에서 돌아보기"라고 할 수 있다.
    오늘 숫자를 가지고 어제보다 높아졌는지 안 높아졌는지 확인해서 값을 구한다.
    """
    stack, answer = [], [0 for _ in range(len(T))]
    
    for i, cur in enumerate(T):
        # 만약 오늘 날씨가 스택의 최종 날씨보다 높으면 정답 하나가 나왔다는 뜻이다
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last

        # 1. 기본적으로 인덱스를 저장해 준다
        stack.append(i)

    return answer

T = [73, 74, 75, 71, 69, 72, 76, 73]
print(daily_temperatures(T))
