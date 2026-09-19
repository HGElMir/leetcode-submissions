class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        n = 0
        while n < len(nums) - 1:
            left.append(nums[n] * left[n])
            n += 1
        
        right = [1] * len(nums)
        n = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        return [x * y for x, y in zip(left, right)]