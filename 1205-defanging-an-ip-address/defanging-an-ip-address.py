class Solution(object):
    def defangIPaddr(self, address):
        s = ""
        for i in address:
            if i == ".":
                i = "[.]"
                s += i
            else:
                s += i
        return s
                 
        