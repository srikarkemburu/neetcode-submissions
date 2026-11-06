class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        freqSort = sorted(count, key=lambda x: count[x], reverse=True)

        return freqSort[:k]

        