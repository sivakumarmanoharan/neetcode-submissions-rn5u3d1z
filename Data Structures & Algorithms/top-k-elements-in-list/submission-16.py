class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = Counter(nums)
        pairs = list(num_dict.items())
        pairs.sort(key=lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(pairs[i][0])
        return res
