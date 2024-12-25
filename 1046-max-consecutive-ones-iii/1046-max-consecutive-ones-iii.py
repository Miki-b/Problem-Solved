class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = left = max_ones = 0
        for right in range(len(nums)):
            if not nums[right]:
                count += 1
            while count > k:
                if not nums[left]:
                    count -= 1
                left += 1

            max_ones = max(max_ones,right - left + 1)  

        return max_ones 