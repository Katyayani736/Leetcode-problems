class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1: return False
        if n == 1: return True
        sett = set([2, 3, 5])
        def ugly(a, base):
            if a in sett:
                return True
            if a % base != 0:
                return False
            n1 = a // base
            return ugly(n1, 2) or ugly(n1, 3) or ugly(n1, 5)
        return ugly(n, 2) or ugly(n, 3) or ugly(n, 5)
