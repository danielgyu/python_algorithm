# https://leetcode.com/problems/trapping-rain-water/

def trap_pointers(height):
    """
    포인터를 이용한 풀이 방법이다.
    이 풀이법에서 가장 중요한 개념은 바로 "가장 높은 막대"이다.
    가장 높은 막대가 하나 있다고 가정하면, 그 막대를 중심으로 왼쪽과 오른쪽 포인터를 나눠서
    투 포인터를 계속 움직이다 가장 높은 막대에서 만날때 까지 물을 채우면 된다.
    """
    if not height:
        return 0
    
    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    # 만날 때 까지 while 문을 돌린다
    while left < right:
        """
        물을 채우는 기준은 다음과 같다.
        각 사이드마다(left/right) 현재 자기 최대 높이(_max)에서 현재 높이를 뺀다.
        이 뺀 값이 volume으로 추가될 수 있는 이유는(왼쪽을 기준으로),
        현재 왼쪽 맥스는 물을 가두는 왼쪽 벽이다. 그리고 이 차이만큼 물을 더할 수 있는건
        오른쪽 벽은 지금 왼쪽 벽보다 더 높기 때문이다.
        """
        
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)

        # 더 낮은 벽의 사이드에서 물을 채워온다 - 반대편 벽이 더 높은 상태라는 걸 인지
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1

    return volume


def trap_stack(height):
    """
    스택을 이용한 풀이 방법이다.
    """
    stack = []
    volume = 0
    
    for i in range(len(height)):

        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()

            if not len(stack):
                break

            distance = i - stack[-1] - 1
            water = min(height[i], height[stack[-1]]) - height[top]
            volume += distance * water

        stack.append(i)

    return volume

height = [0,1,0,2,1,0,1,3,2,1, 2, 1]
index  = [0,1,2,3,4,5,6,7,8,9,10,11]

print(trap_pointers(height))