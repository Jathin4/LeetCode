class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        b = ''
        for i in range(len(s)-1,-1,-1):
            b += s[i]
        return s == b