class Solution(object):
    def minOperations(self, boxes):
        a = [0]*len(boxes)
        lc ,lt,rc,rt,n = 0,0,0,0,len(boxes)
        for i in range(1,n):
            if boxes[i-1] == '1':lc += 1
            lt += lc
            a[i] = lt
        for i in range(n-2,-1,-1):
            if boxes[i+1] == '1': rc += 1
            rt += rc
            a[i] += rt
        return a  
        