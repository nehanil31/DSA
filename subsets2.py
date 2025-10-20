class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtracking(ind,path):
            res.append(path[:])
            nums.sort()
            for i in range(ind,len(nums)):
                if i>ind and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                backtracking(i+1,path)
                path.pop()




        backtracking(0,[])   
        return res 
        
