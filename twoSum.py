Write a program to return list of index values that sum up to specified target value.

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):       
                if nums[i] + nums[j] == target:
                    return [i,j]

sol = Solution()
print(sol.twoSum(nums = [2,18,11,15], target = 17))

Output: [0,3]
