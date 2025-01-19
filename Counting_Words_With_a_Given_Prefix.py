#2185. Counting Words With a Given Prefix
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        c=0
        for i in words:
            if len(i)>=len(pref) and i[:len(pref)]==pref:
                c+=1
        return c
