class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n=len(s)
        ps=[0]*(n+1)
        for start,end,direction in shifts:
            value=1 if direction==1 else -1
            ps[start]+=value
            ps[end+1]-=value
        for i in range(1,n):
            ps[i]+=ps[i-1]
        res=list(s)
        for i in range(n):
            ts=ps[i]
            ts=((ts%26)+26)%26
            c=(ord(s[i])-ord('a')+ts)%26
            res[i]=chr(ord('a')+c)
        return ''.join(res)
