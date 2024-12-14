class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L,max_length=0,0
        for R in range(len(s)):
            if s[R] in s[L:R]:
                while s[L]!=s[R]:
                    L+=1
                L+=1
            max_length=max(max_length,R-L+1)
        return max_length      

        