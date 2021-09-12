#https://leetcode.com/problems/minimum-size-subarray-sum/solution/

import math


def solution(nums: list, target: int) -> int:
    window_start = 0
    min_length = math.inf
    cur_sum = 0

    for window_end in range(len(nums)):
        cur_sum += nums[window_end]

        while cur_sum >= target:
            min_length = min(min_length, window_end - window_start + 1)

            cur_sum -= nums[window_start]

            window_start += 1

    return min_length if min_length != math.inf else 0


nums, target = [2,3,1,2,4,3,], 7
print(solution(nums, target))
assert solution(nums, target) == 2
nums, target = [1,4,4], 4
print(solution(nums, target))
assert solution(nums, target) == 1
nums, target = [1,1,1,1,1,1,1], 11
print(solution(nums, target))
assert solution(nums, target) == 1
