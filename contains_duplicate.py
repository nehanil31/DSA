class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        n=Counter(nums)
        for i in n.values():
            if i>1:
                return True
                break
        return False     