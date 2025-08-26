import math
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diag=[]
        for i in range(len(dimensions)):
            l=dimensions[i][0]
            w=dimensions[i][1]
            diagonol=sqrt((l*l)+(w*w))
            diag.append(diagonol)
        print(diag)    
        big=diag[0]    
        
        area=0       
        for d in range(len(diag)):
            a=dimensions[d][0]*dimensions[d][1]
            if diag[d]>big:
                big=diag[d]
                
                area=a
            elif diag[d]==big:
                
                area=max(area,a)
            else:
                continue
        return area                



        