#Python3 Code
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        res = 0
        n = len(s)
        for i in range(n):
            z = o = 0
            for j in range(i, n):
                if s[j] == '0':
                    z += 1
                else:
                    o += 1
                if z <= k or o <= k:
                    res += 1
        return res