class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        c = 0
        for i in operations:
            if i == "--X":
                c -= 1
            elif i == "X--":
                c -= 1
            else:
                c += 1
        return c