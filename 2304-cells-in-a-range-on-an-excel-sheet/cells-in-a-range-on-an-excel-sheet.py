class Solution(object):
    def cellsInRange(self, s):
        s = s.split(":")  
        c = []
        for i in range(ord(s[0][0]), ord(s[1][0]) + 1):
            for j in range(int(s[0][1]), int(s[1][1]) + 1):
                c.append(chr(i) + str(j))
        return c

        """
        :type s: str
        :rtype: List[str]
        """
        