class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s=dict(Counter(s))
        dict_t=dict(Counter(t))
        return dict_s==dict_t