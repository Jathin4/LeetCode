class Solution(object):
    def reverseWords(self, s):
        words = s.split(" ")
        result = []
        
        for word in words:
            a = 0
            b = len(word) - 1
            chars = list(word)  # convert to list to allow swapping
            
            while a < b:
                chars[a], chars[b] = chars[b], chars[a]
                a += 1
                b -= 1
            
            result.append("".join(chars))
        
        return " ".join(result)

                    

                
        """
        :type s: str
        :rtype: str
        """
        