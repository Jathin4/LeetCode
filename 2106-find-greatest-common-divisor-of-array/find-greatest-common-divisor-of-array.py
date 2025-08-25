class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a = nums[0]
        b = nums[-1]
        while b:
            a,b = b,a%b
        return a
        