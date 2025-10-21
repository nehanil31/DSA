class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        l=2*n
        #c1 is count of open brackets,c2 is closed brackets
        def backtracking(path,c1,c2):
            if c1==n and c2==n:
                res.append("".join(path))
            if c1<n:
                path.append('(')
                backtracking(path,c1+1,c2)
                path.pop()
            if c2<c1:
                path.append(')')
                backtracking(path,c1,c2+1)
                path.pop()
        backtracking([],0,0)
        return res   
