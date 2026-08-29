class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            temp[n] = 1 + temp.get(n, 0)
        for n, v in temp.items():
            freq[v].append(n)

        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
