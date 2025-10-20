class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def backtracking(ind,path,sum):
            
            if sum==n and len(path)==k:
                res.append(path[:])
            if sum>n or len(path)>k:
                return      

            for i in range(ind,10):
                
                path.append(i)
                backtracking(i+1,path,sum+i)    
                path.pop()
        backtracking(1,[],0)
        return res      
