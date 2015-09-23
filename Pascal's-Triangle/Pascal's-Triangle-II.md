# [Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/)

## Description
Given an index k, return the `kth` row of the Pascal's triangle.

For example, given `k = 3`,
Return `[1,3,3,1]`.

**Note:** Could you optimize your algorithm to use only `O(k)` extra space?
## Analysis
### Clarifications
1. Row index will start from 0, not 1, correct？

### Method
This is similar as the solution of Pascal's Triangle. Basically, use nth line to get n+1th line. Simple insert 1 into nth-line and then do `list[i] = list[i] + list[i+1]`.

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

## Python Code
~~~
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        count = 0
        oneRow = []
        while count <= rowIndex:
            oneRow.insert(0, 1)
            for i in range(1, count):
                oneRow[i] = oneRow[i] + oneRow[i+1]
            count += 1
        return oneRow
~~~
## Test Cases
~~~
1. 1 -> [1]
2. 2 -> [1,1]
3. 3 -> [1,2,1]
~~~