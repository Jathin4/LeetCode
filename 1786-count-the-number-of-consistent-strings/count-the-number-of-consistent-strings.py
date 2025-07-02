class Solution(object):
    def countConsistentStrings(self, allowed, words):
        count = 0
        s = set(allowed)
        flag = True
        for word in words:
            flag=True
            for i in word:
                if i not in allowed:
                    flag=False
                    break
            if flag:
                count+=1
        return count
                     

        