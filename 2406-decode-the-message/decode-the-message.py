class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key = key.replace(" ", "")
        mp = {}
        a = 97  
        
        for ch in key:
            if ch not in mp:
                mp[ch] = chr(a)
                a += 1
        
        s = ''
        for ch in message:
            if ch == ' ':
                s += ' '
            else:
                s += mp[ch]
        
        return s
