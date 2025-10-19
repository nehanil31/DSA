class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def backtracking(index,path,sum):
            if sum>target:
                return
            if sum==target:
                res.append(path[:])

            for i in range(index,len(candidates)):
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                
                path.append(candidates[i])
                backtracking(i+1,path,sum+candidates[i])  
                path.pop()
        backtracking(0,[],0)   
        return res       
        
