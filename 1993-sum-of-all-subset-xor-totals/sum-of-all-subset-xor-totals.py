class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = 0
        for mask in range(1 << n):
            subset_xor = 0
            for i in range(n):
                if mask & (1 << i):
                    subset_xor ^= nums[i]
            total += subset_xor
        return total
        