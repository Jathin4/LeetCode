class Solution(object):
    def balancedStringSplit(self, s):
        res = cnt = 0
        for i in s:
            cnt+= i == 'L'
            cnt-= i == 'R'
            res+= cnt == 0
        return res 

        