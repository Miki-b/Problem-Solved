class Solution:
    def firstUniqChar(self, s: str) -> int:
        new=list(s)
        for i in range(len(s)):
            new[i]=0
            if s[i] not in new:
                return i
            else:
                new[i]=s[i]
        return -1
        
            
            