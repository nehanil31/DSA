class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """bit manipulation
        l=2**(len(nums))
        subset=[]
        for n in range(0,l):
            res=[]
            for i in range(0,len(nums)):
                if n & (1<<i):
                    res.append(nums[i])
            subset.append(res)    
        return subset"""

        """recursion """
        res=[]
        def backtrack(start,path):
            res.append(path[:])
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()
        backtrack(0,[])
        return res        



        
