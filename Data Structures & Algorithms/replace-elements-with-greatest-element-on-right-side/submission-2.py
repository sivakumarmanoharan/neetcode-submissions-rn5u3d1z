class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        '''
        1. For i from 0 to len(arr)-1, find the max element from i+1th index to len(array)
        2. Replace at the ith index
        3. arr[len(arr)-1]= -1
        4. Return the array
        '''
        n = len(arr)
        for i in range(n-1):
            arr[i]=max(arr[i+1:])
        arr[n-1] = -1
        return arr