# Qn. Given an array arr[] of distinct elements size N that is sorted and then rotated around an unknown point, the task is to check if the array has a pair with a given sum X.

def pairInSortedRotated(arr, n, x):
    """
    Function to find if there is a pair in a sorted and rotated array 
    that adds up to a specific value x.

    Parameters:
    arr (list): The sorted and rotated array.
    n (int): Length of the array.
    x (int): The target sum to find.

    Returns:
    bool: True if a pair is found with the sum equal to x, otherwise False.
    """
    pivot_index = -1
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            pivot_index = i
            break
    left = (pivot_index + 1) % n
    right = pivot_index
    while left != right:
        current_sum = arr[left] + arr[right]
        if current_sum == x:
            return True
        elif current_sum < x:
            left = (left + 1) % n
        else:
            right = (n + right - 1) % n
    return False
