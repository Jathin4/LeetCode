class Solution(object):
    def reverseDegree(self, s):
        c = []
        for i in range(0,len(s)):
            b = ord('z')-ord(s[i])+1
            d = b*(i+1)
            c.append(d)
        return sum(c)
        
        