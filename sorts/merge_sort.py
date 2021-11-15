# merge sort
# https://leetcode.com/problems/sort-an-array/

def merge_sort(nums: list) -> list:
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j] 
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

    return nums

def sort_array(nums: list) -> list:
    return merge_sort(nums)


if __name__ == "__main__":
    #print(sort_array([5, 1, 1, 2, 0, 0]))
    #print(sort_array([-2, 3, -5]))
    print(sort_array([-1, 2, -8, -10]))
