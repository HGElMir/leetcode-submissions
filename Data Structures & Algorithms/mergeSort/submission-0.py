# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:

    def merge(self, left, right):
        result = []
        l = r = 0

        while l < len(left) and r < len(right):
            if left[l].key < right[r].key:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1

        result.extend(left[l:])
        result.extend(right[r:])

        return result

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        if (len(pairs) <= 1):
            return pairs

        n = len(pairs)

        mid = n // 2
        left_merge = self.mergeSort(pairs[mid:])
        right_merge = self.mergeSort(pairs[:mid])

        return self.merge(left_merge, right_merge)
