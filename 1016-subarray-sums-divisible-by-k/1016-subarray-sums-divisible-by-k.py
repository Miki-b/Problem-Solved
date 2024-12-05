class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix=defaultdict(int)
        prefix[0]=1
        sum=0
        res=0
        for i in range(len(nums)):
            sum+=(nums[i])
            reminder=sum%k
            res+=prefix.get((reminder),0)
            prefix[reminder]+=1
            
        return res