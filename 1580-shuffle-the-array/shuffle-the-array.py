class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        r = []
        a = nums[0:n]
        b = nums[n:]
        for i in range(0,n):
            r.append(a[i])
            r.append(b[i])
            
            
        return r
