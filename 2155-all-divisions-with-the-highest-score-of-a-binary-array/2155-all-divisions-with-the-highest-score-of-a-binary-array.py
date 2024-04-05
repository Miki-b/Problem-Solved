class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        al=0
        bl=0
        ar=0
        br=0
        sum=[]
        arr=[]
        max=0
        num1=nums.count(1)
        num0=nums.count(0)
        for i in range(len(nums)+1):
            if i==0:
                sum.append(num1)  
            if i<len(nums):
                if nums[i]==1:
                    al=al+1
                elif nums[i]==0:
                    bl=bl+1
                ar=num1-al           
                sum.append(bl+ar)
            if max<=sum[i]:
                max=sum[i] 
        for x in range(len(sum)):
            if sum[x]==max:
                arr.append(x)
        
        return arr
        
        