class Solution(object):
    def findDegrees(self, matrix):
        d =[]
        for i in range(len(matrix)):
            d.append(sum(matrix[i]))
        return d
         

        