class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in map:
                map[sorted_word] = []
            map[sorted_word].append(word)
        return list(map.values())