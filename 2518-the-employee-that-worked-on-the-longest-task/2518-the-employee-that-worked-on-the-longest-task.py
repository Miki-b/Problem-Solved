class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        max=logs[0][1]
        maxi=logs[0][0]
        for i in range(1,len(logs)):
            if logs[i][1]-logs[i-1][1]>max:
                max= logs[i][1]-logs[i-1][1]
                maxi=logs[i][0]
            elif logs[i][1]-logs[i-1][1]==max and logs[i][0]<maxi:
                max= logs[i][1]-logs[i-1][1]
                maxi=logs[i][0]
            print(max)
            print(maxi)
        return maxi
                

        