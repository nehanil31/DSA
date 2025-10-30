class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def backtrack(index,s,path):
            if index==len(s):
                res.append(path[:])
                return
            for i in range(index,len(s)):
                if s[index:i+1:]==s[index:i+1][::-1]:
                    path.append(s[index:i+1])
                    backtrack(i+1,s,path)
                    path.pop()  
        backtrack(0,s,[])
        return res
