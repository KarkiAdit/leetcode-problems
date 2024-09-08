# 53. Maximum Subarray

# This solution exceeded time limit and failed 8 test cases out of 210
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Assuming nums always has atleast one element
        max = nums[0]
        for p1 in range(len(nums)):
            curr = 0
            for p2 in range(p1, len(nums)):
                curr += nums[p2]
                if max < curr:
                    max = curr
        return max

# This is the optimized O(n) solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Assuming the given array always has atleast one element
        maximum = nums[0]
        curr_window_sum = maximum
        for idx in range(1, len(nums)):
            if curr_window_sum < 0 and nums[idx] > curr_window_sum:
                maximum = max(maximum, nums[idx])
                curr_window_sum = nums[idx]
            else:
                curr_window_sum += nums[idx]
                maximum = max(maximum, curr_window_sum)
        return maximum