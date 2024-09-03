class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        missing=0
        while i < len(nums):
            correct_index = nums[i]
            length=len(nums)
            
            if correct_index<length and correct_index != i:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i:
                return i 
        
    
        return len(nums)
        



    
                
            


        
