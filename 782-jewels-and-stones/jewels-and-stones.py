class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        s = 0
        for i in stones:
            if i in jewels:
                s+= 1
        return s