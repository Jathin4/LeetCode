class Solution(object):
    def alternatingSum(self, nums):
        e = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                e += nums[i]
            else:
                e -= nums[i]
        return e