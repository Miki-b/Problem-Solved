class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i=0
        missing=[]
        while i<len(nums):
            correct_index=nums[i]-1
            if nums[i]!=nums[correct_index]:
                nums[i],nums[correct_index]=nums[correct_index],nums[i]
            else:
                i+=1
        print(nums)
        for i in range(len(nums)):
            if nums[i]-1!=i:
                missing.append(nums[i])
                missing.append(i+1)
        return missing