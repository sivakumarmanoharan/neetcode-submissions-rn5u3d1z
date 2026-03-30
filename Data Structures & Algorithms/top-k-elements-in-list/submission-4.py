class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict=Counter(nums)
        min_heap = []
        for val,freq in frequency_dict.items():
            heapq.heappush(min_heap,(freq,val))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [val[1] for val in min_heap]
