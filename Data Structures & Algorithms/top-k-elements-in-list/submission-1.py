class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict={}
        for i in nums:
            frequency_dict[i]=nums.count(i)
        k_most=heapq.nlargest(k, frequency_dict.keys(), key=frequency_dict.get)
        return k_most
