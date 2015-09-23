# [Insert Interval](https://leetcode.com/problems/insert-interval/)

## Description
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals `[1,3],[6,9]`, insert and merge `[2,5]` in as `[1,5],[6,9]`.

Example 2:
Given `[1,2],[3,5],[6,7],[8,10],[12,16]`, insert and merge `[4,9]` in as `[1,2],[3,10],[12,16]`.

This is because the new interval `[4,9]` overlaps with `[3,5],[6,7],[8,10]`.
## Analysis
### Clarifications
1. Do the return interval list need to be sorted? Yes!
2. Are the group of input intervals sorted? Yes!
3. So when combining [1,2] and [3,4], whch one is the result [1,4] or [[1,2],[3,4]]? The result should be [[1,2],[3,4]].

### Method
**Brute Force Method:**
Think about three cases when it comes to two intervals.

1. { Target Interval } ... \[ Merged Interval ] (left)
2. [ Merged Interval ] ... \{ Target Interval } (right)
3. [merge { Inteval ..Target ] Inerval }

So for the first two cases are easy and just move one of the intervals into results. But for the third one, the new merged interval should be created, based on two input intervals. 

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

## Python Code
~~~
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        rs = []
        for interval in intervals:
            if (interval.end) < newInterval.start: # [-2,-1] [1,3]
                rs.append(interval)
                continue
            if (interval.end) == newInterval.start: # [-2,0] [1,3]
                newInterval.start = interval.start
                continue
            if (interval.start) == newInterval.end: # [1,3] [4,5]
                newInterval.end = interval.end
                continue
            if (interval.start) > newInterval.end:  # [1,3] [7,8]
                rs.append(newInterval)
                newInterval = interval
                continue
            newInterval.start = min(interval.start, newInterval.start)
            newInterval.end = max(interval.end, newInterval.end)
    
        rs.append(newInterval)
    
        return rs
~~~
## Test Cases
~~~
1. [[1,2]], [0,0] -> [[0,0], [1,2]] (left)
2. [[2,4]], [7,8] -> [[2,4], [7,8]] (right)
3. [[3,5]], [2,4] -> [[2,5]]        (mixed)
4. [[3,8]], [4,5] -> [[3,8]]        (covered)
~~~