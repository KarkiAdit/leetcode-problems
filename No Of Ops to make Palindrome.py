# Qn. Given an array of positive integers. We need to make the given array a ‘Palindrome’. The only allowed operation is”merging” (of two adjacent elements). Merging two adjacent elements means replacing them with their sum. The task is to find the minimum number of merge operations required to make the given array a ‘Palindrome’.
# Input : arr[] = {15, 4, 15}
# Output : 0
# Array is already a palindrome. So we
# do not need any merge operation.
# Input : arr[] = {1, 4, 5, 1}
# Output : 1
# We can make given array palindrome with
# minimum one merging (merging 4 and 5 to
# make 9)
# Input : arr[] = {11, 14, 15, 99}
# Output : 3
# We need to merge all elements to make
# a palindrome.

def main(nums: list) -> int:
    left = 0
    right = len(nums) - 1
    no_of_ops = 0
    while left < right:
        if nums[left] == nums[right]:
            right -= 1
            left += 1
        elif nums[left] > nums[right]:
            right -= 1
            nums[right] += nums[right + 1]
            no_of_ops += 1
        else:
            left += 1
            nums[left] += nums[left - 1]
            no_of_ops += 1
    return no_of_ops