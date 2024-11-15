class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        L=0
        ans=mini=float('inf')
        for i in range(len(nums)):
            if i-L+1==k:
                mini=nums[i]-nums[L]
                L+=1
            ans=min(ans,mini)
        return ans