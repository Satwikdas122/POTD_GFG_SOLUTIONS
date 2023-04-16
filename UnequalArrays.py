from typing import List
class Solution:
    def solve(self, N : int, A : List[int], B : List[int]) -> int:
        # code here
        if sum(A) != sum(B):
            return -1

        A.sort()
        B.sort()

        ae, ao, be, bo = [], [], [], []
        for i in A:
            if i % 2 == 0:
                ae.append(i)
            else:
                ao.append(i)

        for i in B:
            if i % 2 == 0:
                be.append(i)
            else:
                bo.append(i)

        if len(bo) != len(ao) or len(be) != len(ae):
            return -1

        count = 0
        for i in range(len(ae)):
            if be[i] > ae[i]:
                count += (be[i] - ae[i]) // 2
        for i in range(len(ao)):
            if bo[i] > ao[i]:
                count += (bo[i] - ao[i]) // 2

        return count
