# Qn. Reverse array

def main(nums: list[int]) -> list[int]:
    start = 0
    end = len(nums) - 1
    while start < end:
        # Swap elements 
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
    return nums 