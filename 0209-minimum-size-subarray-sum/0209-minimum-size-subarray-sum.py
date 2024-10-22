class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum=0
        L=0
       
        minimum=float('inf')
        for i in range(len(nums)):
            sum+=nums[i]
            if (sum<target) and (i==len(nums)-1) and (L==0):
                minimum=0
                
            while sum>=target:
                minimum= min(minimum,i-L+1)
                sum-=nums[L]
                L+=1
            
            
        
        return minimum