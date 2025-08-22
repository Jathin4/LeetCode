class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = []
        for i in s:
            if len(r) >= 2 and r[-1] == r[-2] == i:
                continue
            r.append(i)
        return "".join(r)


        