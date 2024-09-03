class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i=0
        Missing_duplicate=[]
        while i<len(nums):
            correct_index=nums[i]-1
            if nums[i]!=nums[correct_index]:
                nums[i],nums[correct_index]=nums[correct_index],nums[i]
            else:
                i+=1
        
        for i in range(len(nums)):
            if nums[i]-1!=i:
                Missing_duplicate.append(nums[i])
                Missing_duplicate.append(i+1)
        return Missing_duplicate