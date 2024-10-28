class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        L=0
        count=0
        mini=k
        for i in range(len(blocks)):
            if blocks[i]=='W':
                count+=1
            if i-L+1==k:
                mini=min(mini,count)
                if blocks[L]=='W':
                    count-=1
                L+=1

        return mini