class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        '''
        Breaking condition:
        1. If len(sentence1)!=len(sentence2), return False
        
        Main condition
        1. For each word in sentence 1, if the corresponding pair is not present in sentence2's same position, return False
        2. Remaining cases return True 
        '''
        s1_len, s2_len = len(sentence1), len(sentence2)
        if s1_len != s2_len:
            return False
        
        pairs = set()
        for u, v in similarPairs:
            pairs.add((u, v))
            pairs.add((v, u))
            
        for i in range(s1_len):
            w1, w2 = sentence1[i], sentence2[i]
            if w1 != w2 and (w1, w2) not in pairs:
                return False
        return True