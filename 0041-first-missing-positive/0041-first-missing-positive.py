class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums):
            correct_index = nums[i]-1
            if nums[i]>0 and nums[i]<= len(nums) and nums[i]!=nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i+= 1
        print(nums)
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return nums[len(nums)-1]+1
        
       