from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = Counter(nums)
        occurences = dict(sorted(occurences.items(), key=lambda x: x[1], reverse=True))
        vals = list(occurences.items())
        ans = []
        for i in range(k):
            ans.append(vals[i][0])

        return ans