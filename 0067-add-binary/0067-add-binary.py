class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1=0
        num2=0
        L1=len(a)
        L2=len(b)
        for i in a:
            num1=num1+(int(i)*pow(2,L1-1))
            L1=L1-1
        for j in b:
            num2=num2+(int(j)*pow(2,L2-1))
            L2=L2-1
        num3=num1+num2
        ans=""
        for k in range(num3+1):
            if num3%2==0:
                ans=ans+"0"
                num3=num3//2
            elif num3==1:
                ans=ans+"1"
                break
            else:
                ans=ans+"1"
                num3=num3//2
        ans2=""
        for l in range(1,len(ans)+1):
            ans2=ans2+ans[-l]
        return ans2

