class Solution:
    def wifiRange(self, N, S, X): 
        c=0
        for i in S :
            if i=='0' :
                c +=1
            else :
                if c > X :
                    return False
                c = -X
        if c>0 :
            return False
        else :
            return True
