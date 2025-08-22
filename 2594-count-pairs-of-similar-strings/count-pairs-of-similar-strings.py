class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        c = 0
        n = len(words)
        for i in range(n):
            for j in range(i+1, n):
                if set(words[i]) == set(words[j]):
                    c += 1
        return c  

        