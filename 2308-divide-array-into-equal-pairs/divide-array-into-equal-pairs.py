class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import Counter
        c = Counter(nums)
        
        for i in c.values():
            if i % 2 != 0:   
                return False
        return True
