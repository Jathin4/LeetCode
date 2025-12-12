class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        count = Counter()
        for x in nums:
            good_pairs += count[x]
            count[x] += 1
        return good_pairs