class Solution(object):
    def scoreOfString(self, s):
        score = 0
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))
        return score
        