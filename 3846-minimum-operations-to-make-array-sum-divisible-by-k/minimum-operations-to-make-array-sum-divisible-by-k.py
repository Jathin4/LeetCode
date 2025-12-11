class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        a = 0
        for i in nums:
            a += i
        return a%k
        