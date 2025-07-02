class Solution(object):
    def interpret(self, command):
        
        v = ""
        i = 0
        for _ in range(len(command)):
            if i >= len(command):
                break
            if command[i] == "G":
                v += "G"
                i += 1
            elif command[i:i+2] == "()":
                v += "o"
                i += 2
            elif command[i:i+4] == "(al)":
                v += "al"
                i += 4
        return v
        