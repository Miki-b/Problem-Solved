class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum,L=0,0
        maxi=float('-inf')
        for R in range(len(nums)):
            sum+=nums[R]
            if R-L+1>k:
                sum-=nums[L]
                L+=1
            if R-L+1==k:
                maxi=max(maxi,sum/k)
                print(maxi)
        return maxi