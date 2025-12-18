class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        l,h = 0,len(nums) - 1
        r = 0

        while l < h:
            if nums[l] + nums[h] < target:
                r += h - l
                l += 1
            else:
                h -= 1

        return r