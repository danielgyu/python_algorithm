# https://leetcode.com/problems/product-of-array-except-self/

def product_except_self(nums):
    """
    이 문제는 나눗셈을 사용하지 않고 O(N)에 풀어야 하는 제약이 있다.
    이럴 경우 투 포인터랑 비슷하게,
    왼쪽과 오른쪽으로 기준을 나누면 된다.
    """
    out = []

    p = 1
    # 이 for문은 자신보다 왼쪽에 있는 값들을 곱한 결과를 out에 추가한다
    # 따라서 out의 마지막 아이템은 최종 값이 나온다
    for i in range(len(nums)):
        out.append(p)
        p *= nums[i]

    p = 1
    # 여기선 거꾸로 for문을 돌면서 오른쪽 값들을 곱한다,
    # 자연스럽게 왼쪽과 오른쪽 값들을 전부 곱하게 된다
    for i in range(len(nums)-1, -1, -1):
        out[i] *= p
        p *= nums[i]

    return out

nums = [1,2,3,4]
print(product_except_self(nums))