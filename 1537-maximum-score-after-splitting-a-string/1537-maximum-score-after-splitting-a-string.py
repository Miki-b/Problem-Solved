class Solution:
    def maxScore(self, s: str) -> int:
        max_score=0
        new=defaultdict(int)
        
        for i in range(len(s)-1):
            new=defaultdict(int)
            for j in s[:i+1]:
                if j=='0':
                    new[j]+=1
                    
            for k in s[i+1:]:
                if k=='1':
                    new[k]+=1
            max_score=max(max_score,new['0']+new['1'])
        return max_score
