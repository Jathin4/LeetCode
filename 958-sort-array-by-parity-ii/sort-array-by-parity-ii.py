class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        e,o = 0,1
        r = [0]*len(nums)
        for i in nums:
            if i % 2 == 0:
                r[e] = i
                e += 2
            else:
                r[o] = i
                o += 2
        return r
        