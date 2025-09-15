# Given an array arr[], its starting position l and its ending position r. Sort the array using the merge sort algorithm.

class Solution:
    def quickSort(self, arr, low, high):
        #code here
        if low >= high: return
        partition_idx = self.partition(arr, low, high)
        # Sort the left half
        self.quickSort(arr, low, partition_idx - 1)
        self.quickSort(arr, partition_idx + 1, high)

    def partition(self, arr, low, high):
        #code here
        pivot = arr[high] # Take the high as the pivot
        partition_idx = low # Start from the low
        for idx in range(low, high):
            if (arr[idx] < pivot):
                arr[partition_idx], arr[idx] = arr[idx], arr[partition_idx] # Swap curr element with element at the partition idx
                partition_idx += 1
        arr[high], arr[partition_idx] = arr[partition_idx], arr[high]
        return partition_idx
        