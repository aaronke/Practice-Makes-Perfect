# [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)

## Description
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = `[2,1,5,6,2,3]`.

The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example, Given height = `[2,1,5,6,2,3]`, return `10`.

## Analysis

### Methods
**Method 1 Divide and Conquer:** Search the min value first -- `minValue`. Therefore, if the length of list is `n`, there mush be a rectangle whose size is `n * minValue`. and also the problem will be divided into 2 `n/2` problems. And the cost to combine those three results will be constant. 

* Time Complexity: `O(nlogn)`
* Space Complexity: `O(n)`

**Method 2 Constant array:** Use hashtable to store the current accumulation of each numbers(all the number is from the input list). So if moving to A, A is smaller than last number -B. Then we need to set value with key (between A and B) as `0`. If A is larger than B, then set values with key (between A and B) as the value of key. For all the value whose key is below A, increase all of them by their keys.

* Time Complexity: `O(n^2)`
* Space Complexity: `O(n)`

Unfortunately, these two methods above  exceed the time limit!! Need update in the  future!!

## Python Code
~~~
class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Binary Method
        # l = len(height)
        # if l == 0:
        #     return 0
        # minH = min(height)
        # index = height.index(minH)
        # maxValue = minH * l
        
        # maxLeft = self.largestRectangleArea(height[:index])
        # maxRight = self.largestRectangleArea(height[index+1:])
        
        # return max(maxValue, maxLeft, maxRight)
        
        l = len(height)
        if l == 0:
            return 0
        maxH = max(height)
        status = {}
        for value in height:
            if value not in status:
                status[value] = 0
        
        former = 0
        for i in range(l):
            if height[i] <= former:
                for value in height:
                    if value > height[i]:
                        status[value] = 0
            else:
                for value in height:
                    if value > former and  value <= height[i]:
                        status[value] = value
            
            for value in height:
                if value < former and value < height[i]:
                    status[value] += value 
                if status[value] > maxH:
                    maxH = status[value]
            former = height[i]
            
        return maxH
~~~

## Test Cases
~~~
1. [1,1] -> 2
2. [1,1,4] -> 4
3. [1,1,1,3] -> 4
4. [2,1,5,6,2,3,7] -> 10
5. [] -> 0
~~~