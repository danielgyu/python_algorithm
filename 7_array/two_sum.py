def two_sum1(nums, target):
    """
    Brute Force보다 해쉬를 통해 더 빨리 값을 찾아낼 수 있다
    딕셔너리로 만든 후에도 i,v enumerate로 값을 찾는 이유는,
    하나의 숫자가 여러 인덱스를 가질 수 있기 때문이다(예: nums = [3,3])
    """
    dic = {}
    for i, v in enumerate(nums):
        dic[v] = i
    for i, v in enumerate(nums):
        if target - v in dic and i != dic[target-v]:
            return [i, dic[target-v]]
        
        
def two_sum2(nums, target):
    """
    조금 더 깔끔하게 만들면서 찾는 방식
    """
    nums_map = {}
    for i, v in enumerate(nums):
        if target - v in nums_map:
            return [nums_map[target - v], i]
        nums_map[v] = i


nums = [3,2,4]
target = 6
print(two_sum1(nums, target))
nums = [3,3]
target = 6
print(two_sum2(nums, target))