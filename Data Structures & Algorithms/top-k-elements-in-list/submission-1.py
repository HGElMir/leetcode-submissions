from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency = Counter(nums)

        return [n[0] for n in list(frequency.most_common(k))]