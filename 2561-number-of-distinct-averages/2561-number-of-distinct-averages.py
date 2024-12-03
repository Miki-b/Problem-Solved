class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        distinct=defaultdict(int)
        nums.sort()
        i,j=0,len(nums)-1
        while i<j:
            average = (nums[i] + nums[j]) / 2 
            distinct[average] += 1
            i+=1
            j-=1
        return len(distinct)