class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length=float('inf')
        L,sum=0,0
        for R in range(len(nums)):
            sum+=nums[R]
            while sum>=target:
                min_length=min(min_length,R-L+1)
                sum-=nums[L]
                L+=1
            # if sum>=target:
            #     min_length=min(min_length,R-L+1)
        if min_length==float('inf'):
            return 0
        else:
            return min_length