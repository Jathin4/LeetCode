class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        r = [0] * n
        s = [0] * (n + 1)
        for i in range(n):
            s[0] += s[A[i]]
            s[A[i]] = 1
            s[0] += s[B[i]]
            s[B[i]] = 1
            r[i] = s[0]
        return r
        