class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs= sorted(strs)
        str_map = defaultdict(list)
        for s in strs:
            sorted_str=tuple(sorted(s))
            str_map[sorted_str].append(s)
        return list(dict(str_map).values())