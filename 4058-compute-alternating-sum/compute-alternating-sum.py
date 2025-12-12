class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        r = 0
        for i in range(0,len(nums)):
            if i%2 == 0 or i == 0:
                r += nums[i] 
            else:
                r -= nums[i]
        return r