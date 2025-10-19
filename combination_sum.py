class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        
        def backtracking(index,path,sum):
              
            if sum==target:
                res.append(path[:])
                return
            if sum>target:
                return     
            for i in range(index,len(candidates)):
                path.append(candidates[i])
                backtracking(i,path,sum+candidates[i])
                path.pop()

        backtracking(0,[],0)
        return res           
        
