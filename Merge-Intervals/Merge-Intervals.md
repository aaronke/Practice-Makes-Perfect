# [Merge Intervals](https://leetcode.com/problems/merge-intervals/)

## Description
Given a collection of intervals, merge all overlapping intervals.

For example,
Given `[1,3],[2,6],[8,10],[15,18]`,
return `[1,6],[8,10],[15,18]`.

## Analysis
### Clarifications
1. Is the input interval list sorted? If yes, do it sorted based on the starting value of interval?
2. When it comes to merging, if A is [2,3] and b is [4,5], can they merged as [2,5]?

3. Is there any negative number in the interval?

### Method
So similar as insert interval, firstly sort list based on the start point of interval. And then merged one by one. 

* Time Complexity: `O(nlogn)`
* Space Complexity: `O(1)`

## Python Code
~~~
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        lenInter = len(intervals)
        if lenInter == 0:
            return intervals
        
        #Another sorting method: intervals = sorted(intervals, key=lambda inter: inter.start)
        intervals.sort(key=lambda inter: inter.start)

        rsIntervals = []
        
        curInterval = intervals[0]
        for i in range(1, lenInter):
            if intervals[i].start > curInterval.end:
                rsIntervals.append(curInterval)
                curInterval = intervals[i]
            else:
                curInterval.end = max(curInterval.end, intervals[i].end)
        
        rsIntervals.append(curInterval)
        
        return rsIntervals
~~~
## Test Cases
~~~
1. [[1,4],[0,3]] -> [[0,4]]
2. [[]] -> [[]]
3. [[2,5],[6,7]] -> [[2,5], [6,7]]
~~~