class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L1=0
        L2=L1+1
        while L2<len(nums):
            if nums[L1]==0 and nums[L2]!=0:
                nums[L1],nums[L2]=nums[L2],nums[L1]
                L1+=1   
            if nums[L1]!=0:
                L1+=1
            L2+=1
        