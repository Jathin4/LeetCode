class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        a = []
        b = []
        c = 0
        for i in nums:
            if i == pivot:
                c += 1
        d = c*[pivot]
        for j in nums:
            if j < pivot:
                a.append(j)
            elif j > pivot:
                b.append(j)
        
        return a+d+b