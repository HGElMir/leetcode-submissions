# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:


        states = []
        n = len(pairs)

        if n == 0:
            return []
        

        # initial state
        states.append(pairs.copy())

        # standard, stable insertion sort
        for i in range(1, n):
            j = i
            while j > 0 and pairs[j].key < pairs[j-1].key:
                pairs[j-1], pairs[j] = pairs[j], pairs[j-1]
                j -= 1

            # snapshot after finishing the insertion of element i
            states.append(pairs.copy())

        return states
        