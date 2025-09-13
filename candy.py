class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        sum=0
        left=[0]*(len(ratings))
        left[0]=1
        right=[0]*(len(ratings))
        right[-1]=1
        
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                left[i]=left[i-1]+1
            else:
                left[i]=1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                right[i]=right[i+1]+1
            else:
                right[i]=1
        for i in range(len(left)):
            sum+=max(left[i],right[i])
        return sum
        """
        sum=1
        i=1
        while i<len(ratings):
            if ratings[i]==ratings[i-1]:
                sum+=1
                i+=1
                continue
            peak=1
            while i<len(ratings) and ratings[i]>ratings[i-1]:
                peak+=1
                sum+=peak
                i+=1
            down=1
            while i<len(ratings) and ratings[i]<ratings[i-1]:
                down+=1
                sum+=down
                i+=1
              
            if down>=peak:

                sum+=max(down,peak)-peak
        return sum"""                   


        
