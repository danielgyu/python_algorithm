from typing import Optional

# https://leetcode.com/problems/two-sum/

def two_sum(nums: list, target: int) -> list:
    length = len(nums)

    for i in range(length - 1):
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                return [i, j]                

print(two_sum([3,2,4], 6))
