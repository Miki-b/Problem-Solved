class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index=0
        L=len(nums)
        for i in nums:
            index=index+1
            if target <= i:
                break
        # return index
        if target <= nums[L-1]:
            return index-1 
        elif target >nums[L-1]:
            return index
        else:
            return index


        