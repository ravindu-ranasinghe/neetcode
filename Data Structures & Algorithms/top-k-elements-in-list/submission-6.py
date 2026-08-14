class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = []
        counter = defaultdict(int)
        for num in nums:
            if num in counter:
                counter[num] +=1
            else:
                counter[num] = 1
        sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse= True)

        for i in range(k):
            freq.append(sorted_counter[i][0])
        return freq
