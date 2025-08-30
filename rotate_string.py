class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        r=s+s
        """if goal in r:
            return True
        else:
            return False"""
        if r.find(goal)!=-1:
            return True


                    
        else:
            return False
