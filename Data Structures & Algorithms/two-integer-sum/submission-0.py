class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h1 = {}
        for i, n in enumerate(nums):
            answer = target - n
            if answer in h1:
                return [h1[answer], i]
            h1[n] = i
                    