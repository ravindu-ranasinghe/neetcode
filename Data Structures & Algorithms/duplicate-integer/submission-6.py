class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash1 = set()
        for num in nums:
            if num in hash1:
                return True
            else: 
                hash1.add(num)
        return False