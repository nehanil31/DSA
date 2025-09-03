class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        if not s:
            return 0
        i=0
        sign=1
        if s[0]=='-':
            sign=-1
            i+=1
        elif s[0]=='+':
            i+=1    

        num=0
        while i<len(s):
            if s[i].isdigit():
                num=num*10+int(s[i])  
            else:
                break
            i+=1        
        num=num*sign 
        min=-2**(31) 
        max=2**(31)-1
        if num<min:
            return min
        if num>max:
            return max
        return num             

          
                

        return 
