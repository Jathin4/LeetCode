class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """

        a = []
        b = []
        c = []
        for i in range(len(rings)):
            if rings[i] == 'B':
                a.append(rings[i+1])
            elif rings[i] == 'G':
                b.append(rings[i+1])
            elif rings[i] == 'R':
                c.append(rings[i+1])
        d = set(a) & set(b) & set(c)
        return len(d)
        