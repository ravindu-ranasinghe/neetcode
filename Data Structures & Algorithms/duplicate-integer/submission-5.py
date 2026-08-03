class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        done = []
        for num in nums:
            if num in done:
                return True
            else:
                done.append(num)
        return False

        