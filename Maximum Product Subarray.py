# 152. Maximum Product Subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize the values to the first element
        max_prod = max_pos_prod = min_neg_prod = nums[0]
        for i in range(1, len(nums)):
            temp_max_pos_prod = max_pos_prod
            temp_min_neg_prod = min_neg_prod
            max_pos_prod = max(nums[i], temp_max_pos_prod * nums[i], temp_min_neg_prod * nums[i])
            min_neg_prod = min(nums[i], temp_max_pos_prod * nums[i], temp_min_neg_prod * nums[i])
            # Update the overall maximum product
            max_prod = max(max_prod, max_pos_prod)   
        return max_prod
