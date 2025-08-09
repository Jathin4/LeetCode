class Solution(object):
    def maxProduct(self, nums):
        a = nums.sort()
        b = len(nums)-1
        c = len(nums)-2
        d = (nums[b]-1)*(nums[c]-1)
        return d

        """
        :type nums: List[int]
        :rtype: int
        """
        