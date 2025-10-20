class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        res=[]
        h1 = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz' }
        
        def backtrack(ind,path):
            if ind==len(digits):
                res.append("".join(path))
                return 
            for ch in h1[digits[ind]]:
                path.append(ch)
                backtrack(ind+1,path)
                path.pop()
        backtrack(0,[])        
        return res        
