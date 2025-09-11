class Solution(object):
    def countTestedDevices(self, batteryPercentages):
        """
        :type batteryPercentages: List[int]
        :rtype: int
        """
        k = 0
        for i in batteryPercentages:
            k += i > k
        return k