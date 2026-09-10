class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, num in enumerate(nums):
            y = target - num
            if y in map:
                return [map[y], index]
            map[num] = index
        