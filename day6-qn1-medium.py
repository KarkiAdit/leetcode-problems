# 215. Kth Largest Element in an Array

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maximum = max(nums)
        minimum = min(nums)
        unique_nums = {}
        for num in nums:
            if num not in unique_nums:
                unique_nums[num] = 1
            else:
                unique_nums[num] += 1
        counter = 0
        for n in range(maximum, minimum - 1, -1):
            if n in unique_nums:
                if counter + unique_nums[n] >= k:
                    return n
                counter += unique_nums[n]
        # Indicate no such kth largest element found
        return -10 ** 4 - 1