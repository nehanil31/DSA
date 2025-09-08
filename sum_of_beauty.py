class Solution:
    def beautySum(self, s: str) -> int:
        """
        sum=0
        res=[]
        for i in range(len(s)):
            for j in range(i,len(s)):
                res.append(s[i:j+1])
        
       
        
        for s in res:
            diff=max(Counter(s).values())-min(Counter(s).values())
            if diff!=0:
                sum+=diff
        return sum"""

        sum=0
        for i in range(len(s)):
            freq={}
            for j in range(i,len(s)):
                if s[j] not in freq:
                    freq[s[j]]=1
                else:
                    freq[s[j]]+=1
                diff=max(freq.values())-min(freq.values())
                if diff!=0:
                    sum+=diff
        return sum 

        """
        total = 0
        for i in range(len(s)):

            freq = [0] * 26
            for j in range(i, len(s)):
                idx = ord(s[j]) - ord('a')
                freq[idx] += 1
                # Get non-zero frequencies
                non_zero = [f for f in freq if f > 0]
                total += max(non_zero) - min(non_zero)
        return total
        """                  





        
