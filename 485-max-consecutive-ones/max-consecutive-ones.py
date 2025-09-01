class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0

        b = []
        for i in range(len(nums)):
            if nums[i] == 1:
                c += 1
            b.append(c)    
            if nums[i] != 1:
                c = 0    
        return max(b)     