class Solution(object):
    def findArray(self, pref):
        n = len(pref)
        r = [0] * n
        r[0] = pref[0]

        for i in range(1, n):
            r[i] = pref[i] ^ pref[i - 1]

        return r
        