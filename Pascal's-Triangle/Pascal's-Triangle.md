
# [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)

## Description
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

~~~
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
~~~
## Analysis
**Method 1:** Naive, based on the definition of Pascal's Triangle. 

**Method 2:** Get the next line based on the previous line. Add a 1 in each time and do a in-place change for the previous line. Remeber to do deep-copy when getting the new line.

The methods above have the same complexity.

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

## Python Code
~~~
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # Method 1 -- Naive --Based on definition 
        # if numRows < 1:
        #     return []
        # if numRows == 1:
        #     return [[1]]
        # if numRows == 2:
        #     return [[1],[1,1]]
        
        # rs = [[1],[1,1]]
        # preLevel = [1,1]
        # count = 3
        # while count <= numRows:
        #     oneRs = [1]
        #     for i in range(1,count-1):
        #         oneRs.append(preLevel[i-1]+preLevel[i])
        #     oneRs.append(1)
        #     rs.append(oneRs)
        #     preLevel = oneRs
        #     count += 1
        # return rs
        
        # Method 2 -- Refine the way to get next line
        count = 1
        oneRs = []
        rs = []
        while count <= numRows:
            oneRs.insert(0,1)
            for i in range(1, count-1):
                oneRs[i] = oneRs[i] + oneRs[i+1]
            copyRs = []
            for i in oneRs:
                copyRs.append(i)
            rs.append(copyRs)
            count += 1
        return rs
~~~

## Test Cases
~~~
1. 1 -> [[1]]
2. 2 -> [[1],[1,1]]
3. 4 -> [[1],[1,1],[1,2,1],[1,3,3,1]]
~~~
