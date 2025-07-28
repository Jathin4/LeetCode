class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        b = "".join(word1)
        c = "".join(word2)
        
        # return True if both are equal
        return b == c
        