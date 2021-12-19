# https://leetcode.com/problems/array-partition-i/submissions/

def arrayPairSum(nums):
    """
    짝수 배열이 주어지는데,
    2개씩 짝으로 묶고 그 짝에서 작은 숫자로 만들 수 있는 가장 큰 합을 구하라.
    """
    # 정렬 후 두번째 값만 구하면 된다
    return sum([num for num in sorted(nums)[::2]])