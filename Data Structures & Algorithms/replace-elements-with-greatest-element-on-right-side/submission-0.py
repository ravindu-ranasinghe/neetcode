class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        size = len(arr)
        result = [0] * size
        max1 = -1
        for i in range(len(arr) - 1, -1, -1):
            result[i] = max1
            max1 = max(arr[i], max1)
        return result




            

        