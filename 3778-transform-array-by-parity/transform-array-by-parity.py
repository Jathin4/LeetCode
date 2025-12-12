class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        r = []
        for i in nums:
            if i%2 == 0:
                r.append(0)
            else:
                r.append(1)
        return sorted(r)