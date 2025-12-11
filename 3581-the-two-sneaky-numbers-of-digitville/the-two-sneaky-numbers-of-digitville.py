class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hash_map = {}
        n = len(nums)
        r = []
        for i in range(n):
            hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
        for k , v in hash_map.items():
            if v % 2 == 0:
                r.append(k)
        return r
        