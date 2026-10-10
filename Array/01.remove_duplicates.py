"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.
"""

import utils.session
nums = [1,1,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,5,5]

class Solution :
    def remove_duplicates(self,nums):
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if(nums[i] == nums[j]):
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
        return i + 1


solution = Solution()
result = solution.remove_duplicates(nums)

print(result)

# Time Complexity -> O(n)
