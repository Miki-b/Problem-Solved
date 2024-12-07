class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=[]
        s2=[]
        for i in s:
            if i=="#":
                if s1:
                    s1.pop()
            else:
                s1.append(i)
        for j in t:
            if j=="#":
                if s2:
                    s2.pop()
            else:
                s2.append(j)
        print(s1)
        print(s2)
        if "".join(s1)=="".join(s2):
            return True 
        else:
            return False