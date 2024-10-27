class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        L=0
        count=0
        sub=[]
        for i in range(len(s)):
            if s[i] not in sub and len(set(sub))==2:
                    count+=1      
            sub.append(s[i])
            print(sub)
            print(count)
            if len(sub)>=3:
                sub.remove(s[L])
                L+=1
        return count  