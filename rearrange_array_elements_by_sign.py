class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        pos=[]
        neg=[]
        
        for num in nums:
            if num>0:
                pos.append(num)
            else:
                neg.append(num)
         
        p=0
        n=0
        for i in range(0,len(nums),2):
            nums[i]=pos[p]
            p=p+1
           
        for i in range(1,len(nums),2):
            nums[i]=neg[n]
            n=n+1
          
        return nums

            

        