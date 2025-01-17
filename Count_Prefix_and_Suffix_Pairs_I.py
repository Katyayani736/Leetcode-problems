#3042. Count Prefix and Suffix Pairs I
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        c=0
        def isPrefixAndSuffix(str1,str2):
            if len(str1)>len(str2):
                return False
            if str2[0:len(str1)]==str1 and str2[len(str2)-len(str1):len(str2)]==str1:
                return True
        for i in range(0,len(words)):
            for j in range(i+1,len(words)):
                if isPrefixAndSuffix(words[i],words[j]):
                    c+=1
        return c
