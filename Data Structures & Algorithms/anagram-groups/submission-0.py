class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs=sorted(strs)
        str_map=defaultdict(list)
        for i in strs:
            sorted_str=tuple(sorted(i))
            str_map[sorted_str].append(i)
        return list(dict(str_map).values())
            
            
        