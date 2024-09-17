# 56. Merge Intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        size  = len(intervals)
        if size == 1:
            return intervals
        # Sort the intervals based on the start value of each interval
        intervals = sorted(intervals, key=lambda x: x[0])
        p1 = 0
        merged_intervals = []
        while p1 < size - 1:
            upper_bound = intervals[p1][1]
            p2 = p1 + 1
            while p2 < size and intervals[p2][0] <= upper_bound:
                upper_bound = max(upper_bound, intervals[p2][1])
                p2 += 1
            merged_intervals.append([intervals[p1][0], upper_bound])
            p1 = p2
        # Check if last element was not merged
        if p2 == size - 1:
            merged_intervals.append(intervals[p1])
        return merged_intervals
            
            

        