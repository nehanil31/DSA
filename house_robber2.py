class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        prev1=nums[0]
        prev2=max(nums[0],nums[1])
        curr=prev2
        for i in range(2,n-1):
            curr=max(prev2,prev1+nums[i])
            prev1=prev2
            prev2=curr
        prev1=nums[1]
        prev2=max(nums[1],nums[2])
        curr1=prev2
        for i in range(3,n):
            curr1=max(prev2,prev1+nums[i])
            prev1=prev2
            prev2=curr1
        return max(curr,curr1)               

        
