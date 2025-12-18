class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        r = 0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                s = nums[i]+nums[j]
                if s < target:
                    r += 1
        return r