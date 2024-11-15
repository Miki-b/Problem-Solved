class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        count=0
        max_length=0
        sub={}
        for _ in s:
            sub[_]=0
        for i in range(len(s)):
            for key in sub: sub[key] = 0
            print(sub)
            for j in range(i,len(s)):
                if sub[s[j]]<2:
                    sub[s[j]]+=1
                    count+=1
                    print(count)
                else:
                    
                    break
            print(count)
            max_length=max(max_length,count)
            count=0
        return max_length