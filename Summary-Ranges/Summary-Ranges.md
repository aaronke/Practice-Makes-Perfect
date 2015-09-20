# [Summary Ranges](https://leetcode.com/problems/summary-ranges/)

## Description
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given `[0,1,2,4,5,7]`, return `["0->2","4->5","7"]`.
## Analysis
### Clarifications
1. Use a new simple example to clarify if you understand correctly.

### Method
Use the most intuitive method. However, at the beginning, I am totally lost. Why? I choose a wrong datastructure -- Only one variable to check the number that need to be shown. In reality, I need start and end number to get a number range. Otherwise, the problem will be way complicated!

So the idea is to firstly set the start and end number as the first number of list. And then check the next number to see whether start and end need be updated or displayed as string. A very easy trap is to forget converting last pair of start and end number into string. Never forget last Pair!!

* Time Complexity: `O(n)`
* Space Complexity: `O(1)`

## Python Code

~~~
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return nums
        if  len(nums) == 1:
            return [str(nums[0])]
        
        # Really Important to choose the right datastructure!!    
        rs = []
        start = nums[0]
        end = nums[0]
        
        for i in nums[1:]:
            if end+1 == i:
                end += 1
            else:
                if end == start:
                    rs.append(str(end))
                else:
                    rs.append(str(start) + '->' + str(end))
                start, end = i, i
        
        if end == start:
            rs.append(str(end))
        else:
            rs.append(str(start) + '->' + str(end))
        
        return rs
~~~
## Test Cases
~~~
1. 1-2-5-6 -> ['1->2', '5->6']
2. 1-3-4-6 -> ['1','3->4', '6']
3. [] -> []
4. 1  ->  ['1']
~~~
