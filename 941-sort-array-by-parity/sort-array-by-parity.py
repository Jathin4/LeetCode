class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = []
        b = []
        c = []
        for i in nums:
            if i%2 == 0:
                a.append(i)
            else:
                b.append(i)
        return a+b 