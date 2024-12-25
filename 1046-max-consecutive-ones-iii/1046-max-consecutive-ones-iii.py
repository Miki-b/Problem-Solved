class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        maxm = 0
        l = 0
        count = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                count+=1
            if count > k or r+1==len(nums):
                if count >k:
                    maxm = max(maxm,r-l)
                    while l<r and nums[l]:
                        l+= 1
                    l+=1
                    count -=1
                else:
                    maxm = max(maxm,r-l+1)
        return maxm