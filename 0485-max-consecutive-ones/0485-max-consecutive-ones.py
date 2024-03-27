class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a=0
        b=0
        count=0
        for x in nums:
            count=count+1
            a=a+x
            if x==0 or count==(len(nums)):
                if b<a:
                    b=a
                    a=0
                else:
                    a=0
        return b
        