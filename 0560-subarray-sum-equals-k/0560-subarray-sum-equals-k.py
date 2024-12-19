class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixCount=defaultdict(int)
        prefixCount[0]+=1
        sum,Result=0,0
        for i in range(len(nums)):
            sum+=nums[i]
            Result+=prefixCount.get(sum-k,0)
            prefixCount[sum]+=1
        return Result

        