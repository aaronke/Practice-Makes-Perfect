# [Rotate Image](https://leetcode.com/problems/rotate-image/)

## Description
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:Could you do this in-place?
## Analysis
### Clarifications
1.

### Memthod 
**Method 1** -- simple math solution. The disadvantage of it is to require extra arraylist with the same size of input arraylist.

~~~
newX = oldY
newY = n-oldX -1
~~~

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

**Method 2** -- Do two-pass conversions.

~~~
/*
 * clockwise rotate
 * first reverse up to down, then swap the symmetry 
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
*/
~~~

* Time Complexity: `O(n)`
* Space Complexity: `O(1)`

## Python Code
~~~
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # Naive -- O(n) place solution
        # n = len(matrix)
        # if n == 0:
        #     return
        
        # newMatrix = []
        # for i in range(n):
        #     newRow = []
        #     for j in range(n):
        #         newRow.append(matrix[n-j-1][i])
        #     newMatrix.append(newRow)
            
        
        # for i in range(n):
        #     for j in range(n):
        #         matrix[i][j] = newMatrix[i][j]
        
        # convert rotate into two process:
        
        # Rotation Trick Method
        n = len(matrix)
        start = 0
        end = n-1
        while start < end:
            temp = matrix[start] 
            matrix[start] = matrix[end]
            matrix[end] = temp
            start += 1
            end -= 1
        
        for i in range(n):
            for j in range(n):
                if i > j:
                    temp = matrix[j][i] 
                    matrix[j][i] = matrix[i][j]
                    matrix[i][j] = temp
~~~
## Test Cases
~~~
1.[[1,2],
   [3,4]]
          =>
             [[3,1],
              [4,2]]
~~~

## Notes
1. when trying to reverse the array list, I tried to use following code. However, `list` method will create a complete new variable of matrix. Therefore the old matrix will has no change. This is figured out by using [pythontutor](http://www.pythontutor.com/visualize.html#mode=edit).

~~~
# Wrong
matrix =  list(reversed(matrix))
~~~ 
Instead, a safe way is to assign the value with two pointer.

~~~
# Correct
start = 0
end = n-1
while start < end:
    temp = matrix[start] 
    matrix[start] = matrix[end]
    matrix[end] = temp
    start += 1
    end -= 1
~~~
 