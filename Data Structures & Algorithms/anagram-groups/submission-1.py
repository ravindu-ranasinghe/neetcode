class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            sorted_word = sorted(word)
            k = "".join(sorted_word)
            if k not in map:
                map[k] = []
            map[k].append(word)
        return list(map.values())

        