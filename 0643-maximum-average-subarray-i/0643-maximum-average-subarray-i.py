class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum=0
        max_sum=float('-inf')
        L=0
        for i in range(len(nums)):
            sum+=nums[i]
            if i-L+1==k:
                
                sum-=nums[L]
                L+=1
            print(sum)
            max_sum=max(max_sum,sum)    
        print(max_sum)
        return float(max_sum)/float(k)

        