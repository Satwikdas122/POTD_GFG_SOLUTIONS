class Solution:
    def findNumber(self, n : int) -> int:
        # code here
        if n<=5 :
            if n==1 :
                return 1
            if n==2 :
                return 3
            if n==3 :
                return 5
            if n==4 :
                return 7
            if n==5 :
                return 9
        if n%5==0 :
            return self.findNumber(n//5 -1)*10 + 9
        return (self.findNumber(n//5)*10 + self.findNumber(n%5))
