class Solution(object):
    def hasSameDigits(self, s):
        while len(s) > 2:
            a = ""
            for i in range(len(s) - 1):
                j = i + 1
                a += str((int(s[i]) + int(s[j])) % 10)
            s = a
        return s[0] == s[1]       
        """
        :type s: str
        :rtype: bool
        """
        