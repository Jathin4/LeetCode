class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        a = {}
        for i in arr:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1

        b = []
        for i in arr:  
            if a[i] == 1:
                b.append(i)

        return b[k - 1] if k <= len(b) else ""
