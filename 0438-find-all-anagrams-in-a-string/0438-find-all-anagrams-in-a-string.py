class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagrams=defaultdict(int)
        target=defaultdict(int)
        for i in p:
            anagrams[i]+=1
        L=0
        count=0
        answer=[]
        for R in range(len(s)):
            count=0
            target[s[R]]+=1
            if R-L+1>len(p):
                target[s[L]]-=1
                if target[s[L]]<=0:
                    target.pop(s[L],None)
                L+=1
            
            if target==anagrams:
                answer.append(L)
           
                
        return answer