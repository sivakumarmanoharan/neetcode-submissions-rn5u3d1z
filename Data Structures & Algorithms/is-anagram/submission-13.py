class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        
        freq = [0] * 26  # 26 letters in english alphabet
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] +=1
            freq[ord(t[i]) - ord('a')] -=1
        for val in freq:
            if val !=0:
                return False
        return True