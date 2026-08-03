class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        results = []
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1
        sorted_map = sorted(map.items(), key=lambda item: item[1], reverse=True)

        for i in range(k):
            results.append(sorted_map[i][0])
        return results

        