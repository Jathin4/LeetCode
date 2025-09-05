class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        s1 = 0
        s2 = 0
        for i in range(n+1):
            if i % m == 0:
                s2 += i
            else:
                s1 += i
        return s1 - s2
        