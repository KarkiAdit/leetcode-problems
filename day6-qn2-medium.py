# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # As the array is given to have atleast two elements
        pref_prod_left = [nums[0]]
        pref_prod_right = [nums[-1]]
        # Construct the prefix product array
        j = len(nums)
        for i in range(1, j):
            pref_prod_left.append(pref_prod_left[i - 1] * nums[i])
            pref_prod_right.append(pref_prod_right[i - 1] * nums[j - i - 1])
        # Calculate the product
        prod_except_self = []
        for i in range(j):
            if i == 0:
                prod_except_self.append(pref_prod_right[-2])
            elif i == j - 1:
                prod_except_self.append(pref_prod_left[i - 1])
            else:
                prod_except_self.append(pref_prod_left[i - 1] * pref_prod_right[j - i - 2])
        return prod_except_self