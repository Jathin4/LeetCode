class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        a = num[::-1]
        for i in range(len(a)):
            if a[i] != '0':
                b = i
                break
        c = a[b::1]
        return c[::-1]
                

        