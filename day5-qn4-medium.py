# 31. Next Permutation

class Solution:
    def swap(self, nums, p1, p2):
        temp = nums[p1]
        nums[p1] = nums[p2]
        nums[p2] = temp
    def reverse(self, nums, p1, p2):
        while p1 < p2:
            self.swap(nums, p1, p2)
            p1 += 1
            p2 -= 1
    def nextPermutation(self, nums: List[int]) -> None:
        # Find the pivot position
        p1 = len(nums) - 2
        while p1 >= 0 and nums[p1] >= nums[p1 + 1]:
            p1 -= 1
        # Handle no pivot case
        if p1 == -1:
            self.reverse(nums, 0, len(nums) - 1)
            return
        pivot_num = nums[p1]
        for i in range(len(nums) - 1, p1, -1):
            # Swap the pivot to biggest number from right
            if nums[i] > pivot_num:
                self.swap(nums, p1, i)
                break
        # Reverse the elements to right from the pivot
        self.reverse(nums, p1 + 1, len(nums) - 1)

            