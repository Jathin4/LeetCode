class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a = set()
        for i in nums1:
            if i in nums2:
                a.add(i)
        return list(a)
        