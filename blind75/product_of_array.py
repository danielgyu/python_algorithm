def solution(nums: list) -> list:
    p = 1
    output = []
    for i in range(len(nums)):
        output.append(p)
        p *= nums[i]

    p = 1
    for i in range(len(nums)-1, -1, -1):
        output[i] *= p
        p *= nums[i]

    return output


print(solution([1,2,3,4]))
print(solution([-1, 1, 0, -3, 3]))
