class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s, count_t = dict(Counter(s)), dict(Counter(t))
        for key, value in count_s.items():
            if key not in count_t or count_s[key] != count_t[key]:
                return False
        return True