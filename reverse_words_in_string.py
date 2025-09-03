class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        res=""
        for w in range(len(s)-1,-1,-1):
            res+=s[w]
            res+=" "
        return res.strip()
