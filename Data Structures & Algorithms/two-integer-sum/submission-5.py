class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map= {}
        for i , x in enumerate(nums):
            ans = target - x
            if ans in map:
                return [map[ans], i]
            map[x] = i
        