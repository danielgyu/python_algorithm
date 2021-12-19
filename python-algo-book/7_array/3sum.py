# https://leetcode.com/problems/3sum/

def threeSum(nums):
    """
    주어진 배열에서 세 아이템의 합이 0이 되는 유니크한 조합들을 찾는 문제.
    간단하게 n^3로 풀 수 있지만, 타임아웃이 발생하기 때문에 n^2로 접근해야 한다.
    n^3도 세개의 포인터(i, j, k)가 움직이고, n^2도 세개의 포인터가 움직이지만,
    정렬 시킨 후에 진행을 하면 불필요한 탐색은 안해도 되게 된다.
    """
    answer = []
    nums.sort()
    
    for i in range(len(nums) - 2):
        # 유니크한 조합이 필요하기 때문에 같은 숫자는 스킵한다
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # i를 기준으로 바로 옆이 왼쪽 끝, 그리고 배열의 끝이 오른쪽 끝으로 지정
        left, right = i+1, len(nums)-1
        # 그러고 하나씩 좁혀들어간다 - 정렬필수
        while left < right:
            sum = nums[i] + nums[left] + nums[right]

            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                answer.append([nums[i], nums[left], nums[right]])
                # 유니크한 조합을 찾기 때문에 계속 같은 숫자가 나올 경우 스킵한다
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
            left += 1
            right -= 1
    return answer

nums1 = [-1,0,1,2,-1,-4, -1]
nums2 = []
nums3 = [0]
print(threeSum(nums1))