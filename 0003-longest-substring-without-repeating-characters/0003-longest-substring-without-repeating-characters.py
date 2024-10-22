class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash= set()
        max_length=0
        L=0
        
        for i in range(len(s)):
            if s[i] not in hash:
                hash.add(s[i])
                max_length=max(max_length,i-L+1)
            else:
                while s[i] in hash:
                    hash.remove(s[L])
                    L+=1
                hash.add(s[i])
        return max_length


        