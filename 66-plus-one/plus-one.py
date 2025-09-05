class Solution(object):
    def plusOne(self, digits):
        a = "".join(map(str, digits)) 
        a = str(int(a) + 1)           
        b = [int(i) for i in a]       
        return b
