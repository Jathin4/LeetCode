class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        r = []
        for i in nums:
            c = 0
            for j in nums:
                if i > j:
                    c += 1
            r.append(c)
        return r
        