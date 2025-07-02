class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        s=0
        for i in operations:
            if i=="++X" or i=="X++":
                s += 1
            elif i=="--X" or i=="X--":
                s -= 1
        return s