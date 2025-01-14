#2657. Find the Prefix Common Array of Two Arrays
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n=len(A)
        C=[]
        m=0
        for i in range(0,n):
            if A[i]==B[i]:
                m+=1
                C.append(m)
                continue
            if A[i] in B[0:i+1]:
                m+=1
            if B[i] in A[0:i+1]:
                m+=1
            C.append(m)
        return C
