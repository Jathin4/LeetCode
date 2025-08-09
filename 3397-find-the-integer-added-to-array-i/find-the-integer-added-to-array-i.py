class Solution(object):
    def addedInteger(self, nums1, nums2):
        a = (sum(nums2)-sum(nums1))//len(nums1)
        return a
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        