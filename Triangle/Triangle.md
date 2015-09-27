# [Triangle](https://leetcode.com/problems/triangle/)

## Description
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

~~~
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
~~~
The minimum path sum from top to bottom is `11` (i.e., `2 + 3 + 5 + 1 = 11`).

Note: Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
## Analysis
### Clarifications
1. What do you mean by `adjacent numbers`? Use example to clarify!
2. Is there negative number in the list? Yes!

### Methods 
**Methods 1 Recursion:** Based on definition. A classvariable `best` could be created. And then apply recursion, in each recursion, update the `level`, until finding it reaches the end. If the sum for one path is smaller than `best`. Then update it.

* Time Complexity: `O(n)`
* Space Complexity: `O(n)` -- Stack storage

**Method 2 Dynamic Programming:** Another method is to create an array to store the sum of triangle array at corrosponding postion. At the end, return the minimum value of final level of list. 

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

## Python Code
~~~
class Solution(object):
    best = 0
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # Recursion
    #     for i in range(len(triangle)):
    #         self.best += triangle[i][0]
    #     self.minmunTotalSub(0, 0, 0, len(triangle), triangle)
    #     return self.best
            
    # def minmunTotalSub(self,value ,level,index, target, triangle):
        
    #     if level == target:
    #         if value < self.best:
    #             self.best = value
    #         return
    
    #     newValue = value + triangle[level][index]
    #     self.minmunTotalSub(newValue, level+1, index, target, triangle)
    #     self.minmunTotalSub(newValue, level+1, index+1, target, triangle)
    
        # O(n) space
        sumTri = []
        for row in triangle:
            newRow = []
            for i in row:
                newRow.append(0)
            sumTri.append(newRow)
        sumTri[0][0] = triangle[0][0]
        
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                # Be careful about three cases
                if j == 0:
                    sumTri[i][j] = triangle[i][j] + sumTri[i-1][j]
                elif j == (len(triangle[i]) - 1):
                    sumTri[i][j] = triangle[i][j] + sumTri[i-1][j-1]
                else:
                    sumTri[i][j] = triangle[i][j] + min(sumTri[i-1][j-1], sumTri[i-1][j])
        return min(sumTri[len(sumTri) - 1])
        
~~~
## Test Cases
~~~
1. [ [2], [3,4]] -> 5
2. [[-1],[-2,-3]] -> -4
3. [[2], [3,4], [6,5,7],  [4,1,8,3]] -> 11
~~~