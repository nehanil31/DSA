class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        ##nlogn solution
        """
        longest=1
        curr=1
        
        nums.sort()
        
        min=float('-inf')
        for n in nums:
            if n-1 == min:
                min=n
                curr+=1
            elif n==min:
                continue    
                
            else:
                min=n
                curr=1 
            longest=max(curr,longest)    
                 
        return longest"""  
        ##optimal solution
        longest=1
        
        nums=set(nums)
        for n in nums:
            if n-1 not in nums:
                start=n
                curr=1
                while (start+1) in nums:
                    curr+=1
                    start+=1
                longest=max(longest,curr) 

        return longest         


        


