class Solution(object):
    def twoSum(self, nums, target):
        for i, m in enumerate(nums):
            for j,n in enumerate(nums):
                if i!=j and m+n ==target:
                    return[i,j]
                
#second method
