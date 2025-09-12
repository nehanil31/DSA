class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[]
        j=0
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            if res[j][1]>=intervals[i][0]:
                res[j][1]=max(res[j][1],intervals[i][1])
            else:

                res.append(intervals[i])
                j+=1
        return res 
