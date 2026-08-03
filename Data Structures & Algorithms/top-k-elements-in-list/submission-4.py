class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in sorted(nums):
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1

        sortedlist = max_to_low = sorted(map.keys(), key=lambda x: map[x], reverse=True) 
        answer = []
        for i in range(k):
            answer.append(max_to_low[i])
        
        return answer
        