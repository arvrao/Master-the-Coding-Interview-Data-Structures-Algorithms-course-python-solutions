Write a program to return list of index values that sum up to specified target value.

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            # print(i)
            for j in range(len(nums)):
                
                #print(j)
                
                if nums[i] + nums[j] == target:
                    return [i,j]

sol = Solution()
print(sol.twoSum(nums = [2,18,11,15], target = 17))


