class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        r = 0
        s = defaultdict(int)
        for i in nums:
            r += s[i-k]+s[i+k]
            s[i] += 1
        return r