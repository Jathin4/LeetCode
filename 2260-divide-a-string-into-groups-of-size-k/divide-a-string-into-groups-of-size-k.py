class Solution(object):
    def divideString(self, s, k, fill):
        a = []
        i = 0

        while i < len(s):
            c = s[i:i+k]
            if len(c) < k:
                c += fill * (k - len(c))
            a.append(c)
            i += k

        return a