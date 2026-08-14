class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = []
        c = defaultdict(int)
        for num in nums:
            if num in c:
                c[num] += 1
            else:
                c[num] = 1
        sorted_c = sorted(c.items(), key=lambda x:x[1], reverse=True)

        for i in range(k):
            f.append(sorted_c[i][0])
        return f
        