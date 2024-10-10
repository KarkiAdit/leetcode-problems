# Chocolate distribution problem
# Given an array of N integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 
# Each student gets one packet.
# The difference between the number of chocolates in the packet with maximum chocolates and the packet with minimum chocolates given to the students is minimum.

def main(chocolate_list: list[int], m: int) -> int:
    # Handle the empty list case
    if len(chocolate_list) < m:
        return 0
    chocolate_list.sort();
    minimum = float('inf')
    p1 = 0
    p2 = m - 1
    while p2 < len(chocolate_list):
        minimum = min(minimum, chocolate_list[p2] - chocolate_list[p1])
        p1 += 1
        p2 += 1
    return minimum