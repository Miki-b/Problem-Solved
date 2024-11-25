class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        L=0
        max_length=0
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            elif nums[i]==0:
                #max_length=max(max_length,count)
                count=0  
            max_length=max(max_length,count)
        return max_length  
