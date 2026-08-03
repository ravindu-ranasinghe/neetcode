class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = []
        j = defaultdict(int)
        for num in nums:
            j[num]+=1
        s = sorted(j.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            x.append(s[i][0])
        return x