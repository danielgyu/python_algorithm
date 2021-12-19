def find_subsets(nums):
    # sort the numbers to handle duplicates
    breakpoint()
    list.sort(nums)
    subsets = []
    subsets.append([])
    startIndex, endIndex = 0, 0

    for ii in range(len(nums)):
        startIndex = 0
        # if current and the previous elements are same, 
        # create new subsets only from the subsets
        # added in the previous step
        if ii > 0 and nums[ii] == nums[ii - 1]:
            startIndex = endIndex + 1

        endIndex = len(subsets) - 1

        for jj in range(startIndex, endIndex+1):
            # create a new subset from the existing subset
            # and add the current element to it
            set1 = list(subsets[jj])
            set1.append(nums[ii])
            subsets.append(set1)

    return subsets

print(find_subsets([1, 2, 2]))
