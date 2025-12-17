class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        r = []
        for i in range(0,len(accounts)):
            r.append(sum(accounts[i]))
        return max(r)
        