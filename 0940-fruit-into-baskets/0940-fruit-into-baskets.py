class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count=defaultdict(int)
        L,max_num=0,0
        for R in range(len(fruits)):
            count[fruits[R]]+=1
            while len(count)>2:
                if count[fruits[L]]>1:
                    count[fruits[L]]-=1
                else:
                    count.pop(fruits[L])
                L+=1
            max_num=max(max_num,R-L+1)
        return max_num          