class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lol = set()
        for num in nums:
            if num in lol:
                return True
            lol.add(num)
        return False
        