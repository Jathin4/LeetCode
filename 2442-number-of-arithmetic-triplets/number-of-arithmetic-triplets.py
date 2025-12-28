class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        r = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                for k in range(j,len(nums)):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        r += 1
        return r