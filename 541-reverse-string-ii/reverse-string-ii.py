class Solution(object):
    def reverseStr(self, s, k):
        a = len(s)
        s = list(s)

        for i in range(0, a, 2 * k):
            s[i:i + k] = reversed(s[i:i + k])

        return "".join(s)