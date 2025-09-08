class Solution(object):
    def reverse(self, x):
        sign = (x > 0) - (x < 0)   
        x *= sign                  
        res = 0
        while x:
            res = res * 10 + x % 10
            x //= 10
        res *= sign
        return res if -2**31 <= res <= 2**31 - 1 else 0
