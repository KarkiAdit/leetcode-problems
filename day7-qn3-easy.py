# kth smallest element

class Solution:
    def kthSmallest(self, arr, k):
        minimum = min(arr)
        maximum = max(arr)
        unique_nums = {}
        for num in arr:
            if num not in unique_nums:
                unique_nums[num] = 1
            else:
                unique_nums[num] += 1
        counter = 0
        for n in range(minimum, maximum + 1):
            if n in unique_nums:
                if counter + unique_nums[n] >= k:
                    return n
                counter += unique_nums[n]
        return minimum