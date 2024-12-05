class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix=defaultdict(int)
        prefix[0]=1
        sum=0
        res=0
        for i in range(len(nums)):
            sum+=(nums[i])
            
            res+=prefix.get((sum%k),0)
            prefix[sum%k]+=1
            
        return res