class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        r = []
        a = 0
        for i in accounts:
            for j in i:
                a += j
            r.append(a)
            a = 0
        return max(r)
        