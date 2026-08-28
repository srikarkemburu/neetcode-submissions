class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        k = []
        for i in set(nums):
            k.append(i)
        if len(k) == len(nums):
            return False
        else:
            return True

            
        
