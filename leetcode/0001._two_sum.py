"""
Two sum
Given an array of integers,return indices of the two numbers such that add up to a specific target.
You may assume that each input would have exactly one solution,and you may not use the same element
twice.

Example：
Given nums = [2,7,11,15],target = 9
return [0,1]
"""
class Solution(object):
    #Idea 1 - time complexity：O(N^2) - space complexity: O(1)
    def twoSum1(self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
    #Idea 2 - time complexity: O(N) - space complexity: O(N)
    def twoSum2(self,nums,target):
        lookup = {}
        for i,num in enumerate(nums):
            if target-num in lookup:
                return [lookup[target-num],i]
            else:
                lookup[num] = i


test = Solution()
method1 = test.twoSum1([2,7,11,15],9)
method2 = test.twoSum2([2,7,11,15],9)
print(method1)
print(method2)