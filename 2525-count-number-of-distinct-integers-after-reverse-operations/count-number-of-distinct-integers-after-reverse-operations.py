class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = set(nums)
        for i in nums:
            r = int(str(i)[::-1])
            n.add(r)
        return len(n)
        