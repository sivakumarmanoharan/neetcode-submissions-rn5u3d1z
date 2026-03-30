class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict=Counter(nums)
        return heapq.nlargest(k,frequency_dict.keys() ,key=frequency_dict.get)
