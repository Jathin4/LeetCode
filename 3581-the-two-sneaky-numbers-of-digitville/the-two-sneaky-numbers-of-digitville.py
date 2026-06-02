class Solution(object):
    def getSneakyNumbers(self, nums):
        s = set()
        a = []
        for i in nums:
            if i in s:
                a.append(i)
            else :
                s.add(i)
        return a
        