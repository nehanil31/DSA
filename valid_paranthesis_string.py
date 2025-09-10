class Solution:
    def checkValidString(self, s: str) -> bool:
        minc=0
        maxc=0
        for i in range(len(s)):
            if s[i]=='(':
                minc+=1
                maxc+=1
            elif s[i]==')':
                minc-=1
                maxc-=1
            else:
                minc-=1
                maxc+=1
            if minc<0:
                minc=0
            if maxc<0:
                return False
        return minc==0                        
