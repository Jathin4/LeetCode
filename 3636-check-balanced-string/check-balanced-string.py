class Solution(object):
    def isBalanced(self, num):
        a = []
        b = []
        for i in range(len(num)):
            if i%2==0:
                a.append(int(num[i]))
            else:
                b.append(int(num[i]))
        if sum(a) == sum(b):
            return True
        else:
            return False
        