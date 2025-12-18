class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        r = [0]*len(pref)
        r[0] = pref[0]
        for i in range(1,len(pref)):
            r[i] = pref[i] ^ pref[i-1]
        return r