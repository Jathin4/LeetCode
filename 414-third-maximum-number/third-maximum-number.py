class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = sorted(set(nums), reverse=True)  # remove duplicates, sort descending
        if len(n) < 3:
            return n[0]   # maximum
        return n[2]       # third maximum
