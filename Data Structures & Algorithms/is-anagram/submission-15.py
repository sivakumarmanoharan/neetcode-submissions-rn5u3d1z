class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        count = [0]*26
        for c1,c2 in zip(s,t):
            count[self.idx(c1)]+=1
            count[self.idx(c2)]-=1
        return all(c == 0 for c in count)

    def idx(self,c):
        if 'a' <= c <= 'z':
            return ord(c)-ord('a')
        elif 'A' <= c <='Z':
            return 26 + ord(c)-ord('A')
        else:
            return 52 + ord(c)-ord('0') 