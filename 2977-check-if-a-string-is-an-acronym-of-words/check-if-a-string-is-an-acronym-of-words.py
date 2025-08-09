class Solution(object):
    def isAcronym(self, words, s):
        b = ''
        for i in words:
            b += i[0]
        if b == s:
            return True
        else:
            return False
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        