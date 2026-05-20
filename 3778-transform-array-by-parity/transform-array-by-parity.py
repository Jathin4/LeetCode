class Solution(object):
    def transformArray(self, nums):
        even = sum(1 for i in nums if i % 2 == 0)
        odd = len(nums) - even
        
        return [0] * even + [1] * odd