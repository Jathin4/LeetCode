class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        b=[]
        for ch in s:            
            if ch.isdigit():
                b.pop()
            else:
                b.append(ch)
    
        return "".join(b)