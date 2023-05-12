from typing import List


class Solution:
    def arrayOperations(self, n : int, arr : List[int]) -> int:
        c=0
        i=0
        if 0 not in arr:
            return -1
        while i<n:

            if arr[i]!=0:
                c+=1
                while i<n and arr[i]!=0:
                    i+=1
            i+=1
        return c
