class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        a = 0
        b = 0
        for i in commands:
            if i == "UP":
                a -= 1
            elif i == "RIGHT":
                b += 1
            elif i == "DOWN":
                a += 1
            elif i == "LEFT":
                b -= 1
        return a*n+b
        """
        :type n: int
        :type commands: List[str]
        :rtype: int
        """
        