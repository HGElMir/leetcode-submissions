class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        eq = {}

        for n in range(len(nums)):
            candidate = target - nums[n]
            if candidate in eq:
                return [eq[candidate], n]
            eq[nums[n]] = n

        return []