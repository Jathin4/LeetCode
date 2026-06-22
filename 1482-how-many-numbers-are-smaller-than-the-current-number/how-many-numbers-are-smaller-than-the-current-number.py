class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        n = sorted(nums)

        d = {}

        for i in range(len(n)):
            if n[i] not in d:
                d[n[i]] = i

        ans = []

        for num in nums:
            ans.append(d[num])

        return ans