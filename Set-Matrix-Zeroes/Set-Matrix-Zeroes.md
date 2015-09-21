# [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)

## Description
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

**Follow up:**
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea. A simple improvement uses O(m + n) space, but still not the best solution. Could you devise a constant space solution?
## Analysis
### Clarifications
1. Before showing the follow-up, what's the requirements for complexity

### Method
1. O(mn) -- Just copy a whole board and check on that copyed one and set value on the original board.

2. Method 1 -- Implemented. By doing first pass, use two arrays to collect columns and rows that need to be assigned to zero. And then assign then at second pass.

* Time Complexity: `O(mn)`
* Space Complexity: `O(m+n)`

3. Method 2 -- Implemented. Instead of creating two list arrays like Method 1. It treats the first column and first row as the two lists. So Firstly, it know whether first row and column need to be assigned to zeros. Then check other columns and rows and record the lines that need to be assigned. Then with the record, assign non-first column or row first and then do first column and row.

* Time Complexity: `O(mn)`
* Space Complexity: `O(1)`

**Implementation:**  
1. Assignation starts from non-first lines and so the range should be started from 1!!  
2. Since the implemetnation for row and column are very similar. Be consistant!! It should be `matrix[row][column]`. 

## Python Code

## Test Cases
## Notes

~~~
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        #O(m+n) space
        # if len(matrix) == 0 or len(matrix[0]) == 0:
        #     return
        # zeroRow = []
        # zeroColumn = []
        # for column in range(len(matrix)):
        #     for row in range(len(matrix[0])):
        #         if matrix[column][row] == 0:
        #             if column not in zeroColumn:
        #                 zeroColumn.append(column)
        #             if row not in zeroRow:
        #                 zeroRow.append(row)
        
        # for row in zeroRow:
        #     for column in range(len(matrix)):
        #         matrix[column][row] = 0
        
        # for column in zeroColumn:
        #     for row in range(len(matrix[0])):
        #         matrix[column][row] = 0
        
        # For empty column or row
        
        # Method 2 -- Constant space -- Idea is to used first column and row to store state!! 
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        
        rowFirst = False
        columnFirst = False
        
        # Check first column and first row
        for columnIndex in range(len(matrix[0])):
            if matrix[0][columnIndex] == 0:
                rowFirst = True
                break
        for rowIndex in range(len(matrix)):
            if matrix[rowIndex][0] == 0:
                columnFirst = True
                break
            
        # Check the non-first-column-row   
        for row in range(1, len(matrix)):
            for column in range(1, len(matrix[0])):
                if matrix[row][column] == 0:
                    matrix[row][0] = 0
                    matrix[0][column] = 0
        
         # Set non-first row --range start from 1
        for row in range(1, len(matrix)):
            if matrix[row][0] == 0:
                for columnIndex in range(1, len(matrix[0])):
                    matrix[row][columnIndex] = 0
         
         
         # Set non-first column -- range start from 1              
        for column in range(1, len(matrix[0])):
            if matrix[0][column] == 0:
                for rowIndex in range(1, len(matrix)):
                    matrix[rowIndex][column] = 0
                    
        # Set first Column and first row
        if rowFirst:
            for columnIndex in range(len(matrix[0])):
                matrix[0][columnIndex] = 0
        if columnFirst:
            for rowIndex in range(len(matrix)):
                matrix[rowIndex][0] = 0
                    
~~~        