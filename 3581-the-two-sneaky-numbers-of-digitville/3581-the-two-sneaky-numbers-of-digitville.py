class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        new={}
        for i in nums:
            new[i]=0
        ans=[]
        
        for i in nums:
            new[i]+=1
        print(new[0])
        for j in new:
            if new[j]>1:
                ans.append(j)
        return ans

        