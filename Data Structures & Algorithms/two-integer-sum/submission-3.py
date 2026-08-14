class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, x in enumerate(nums):
            y = target - x 
            if y in map:
                return [map[y], i]
            map[x] = i
        