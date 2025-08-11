class Solution(object):
    def findNumbers(self, nums):
        c = 0
        for i in nums:
            s = str(i)
            if len(s)%2 == 0:
                c+=1
        return c
        