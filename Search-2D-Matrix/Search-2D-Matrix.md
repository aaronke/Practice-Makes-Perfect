# [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

## Description
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

~~~
[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
~~~
Given **target = 3**, return `true`.
## Analysis
**Brute Force Methods:** One-by-one checking would be the first idea. It's time complexity is `O(mn)` and space is `O(1)`. 

* Time Complexity: `O(mn)`
* Space Complexity: `O(1)`

Another refined method is to get the row firstly(cost `O(m)` time) and then do one-by-one search on that row(list). Its time complexity is `O(m+n)` and space complexity `O(1)`.

* Time Complexity: `O(m + n)`
* Space Complexity: `O(1)`

**Binary search** So basically implement two level of binary search. One search is to get row list and another is to get number within row. Be really careful about how to implement binary search!!

The first level of binary search is to get a interval while the second one is to get a exact number. So tere is small difference on it.

* Time Complexity: `O(logm + logn)`
* Space Complexity: `O(1)`

## Python Code
~~~
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Brute Force        
        # for nums in matrix:
        #     for i in nums:
        #         if i == target:
        #             return True
        # return False
        
        # Refine Brute Force
        # l = len(matrix)
        # if l == 0:
        #     return False
            
        # rsList = matrix[0]
        # for i in range(l-1):
        #     if matrix[i][0] <= target and  matrix[i+1][0] > target:
        #         rsList = matrix[i]
        # # Don't forget about the case when i = l-1
        # if matrix[l-1][0] <= target:
        #     rsList = matrix[l-1]
        
        # for i in rsList:
        #     if i == target:
        #         return True
        # return False
        
        if (len(matrix) == 0) or (len(matrix[0]) == 0):
            return False
        
        startRow = 0
        endRow = len(matrix) - 1
        
        startColumn = 0
        endColumn = len(matrix[0]) - 1

        while endRow - startRow > 1:
            middleRow = (endRow + startRow)/2
            if matrix[middleRow][0] == target:
                return True
            elif matrix[middleRow][0] > target:
                endRow = middleRow
            else:
                startRow = middleRow
        
        if matrix[endRow][0] > target:
            return self.binarySearch(matrix[startRow], target)
        elif matrix[endRow][0] == target:
            return True
        return self.binarySearch(matrix[endRow], target)
        
    def binarySearch(self, nums, target):
        end = len(nums) - 1
        start = 0
        while start <= end:
            middle = (start + end)/2
            if target == nums[middle]:
                return True
            elif target > nums[middle]:
                start = middle+1
            else:
                end = middle-1
        return False
~~~

## Test Cases
~~~
Input: [[1,2],
       [3,4,5]
       [8, 9, 10, 11]]  
Expected Outcomes      			
				 Find 1  -> True
    		    Find 4  -> True
    		    Find 6  -> False
    		    FInd 10 -> True	    
~~~