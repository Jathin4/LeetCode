import sys
class Solution(object):
    def truncateSentence(self, s, k):
        b = s.split()
        return " ".join(b[:k])
        