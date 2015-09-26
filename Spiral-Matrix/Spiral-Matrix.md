# [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)

## Description
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

~~~
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
~~~
You should return `[1,2,3,6,9,8,7,4,5]`.
## Analysis
Just based on the definition and apply four cases discussions until the 2D array is empty. The thing should be careful that there are cases where empty list will be created, so before doing further, clear emtpy list should be done! 

* Time Complexity: `O(n)`
* Space Complexity: `O(1)`

##Notes
1. When I tried to delete pop out emtpy list in for loop, it always gives me error, because when list length change, the index will also change. It will get out of range error. In a word, don't pop elements when list is used dynamically.

## Python Code
~~~
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rs = []
        
        while matrix:
            top = matrix.pop(0)
            
            right = []
            if matrix:
                column = len(matrix[0])
                for i in range(len(matrix)):
                    right.append(matrix[i][column-1])
                    matrix[i].pop()
            
            # Clear empty row
            matrix = self.clearEmpty(matrix)
      
            bottom = []
            print matrix
            if matrix:
                bottom = list(reversed(matrix.pop()))
            
            left = []
            if matrix:
                for i in range(len(matrix)):
                    left = [matrix[i][0]] + left
                    matrix[i].pop(0)
            
            # Clear empty row
            matrix = self.clearEmpty(matrix)

            rs += top + right + bottom + left
        return rs
    def clearEmpty(self, matrix):
        newMatrix = []
        for i in range(len(matrix)):
            if len(matrix[i]) != 0:
                newMatrix.append(matrix[i])
        return newMatrix  
~~~

## Test Cases
~~~
[[1,2],
 [3,4]]
        -> 
           [1,2,4,3]     
~~~
