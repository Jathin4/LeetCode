class Solution(object):
    def maxProductDifference(self, nums):
        a = nums.sort()
        b = (nums[-1]*nums[-2])-(nums[0]*nums[1])
        return b

        """
        :type nums: List[int]
        :rtype: int
        """