class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        c = 0
        for i in range(len(details)):
            a = details[i][11] + details[i][12]
            if int(a) > 60:
                c += 1
        return c

        