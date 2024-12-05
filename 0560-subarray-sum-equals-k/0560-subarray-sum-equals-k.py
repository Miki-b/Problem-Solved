class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=defaultdict(int)
        prefix[0]=1
        sum=0
        res=0
        for i in range(len(nums)):
            sum+=(nums[i])
            diffrence=sum-k
            res+=prefix.get((diffrence),0)
            prefix[sum]+=1
            
        return res



        