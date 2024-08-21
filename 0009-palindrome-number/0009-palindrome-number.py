class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=str(x)
        num2=''
        for i in range(len(num)-1,-1,-1):
            num2=num2+num[i]
        print(num)
        print(num2)
        if num==num2:
            return 1
        else:
            return 0



        