# [Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)

## Description
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

~~~
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
~~~ 
 
## Analysis
### Clarifications
1. are all the inputs uppercase?
2. Besides the example, do you still have the cases such as `AAA = (26*26*1 + 26*1 + 1)` ?

### Method
Basically, it is just a number system based on 26. 

* Time Complexity: `O(n)`
* Space Complexity: `O(1)`

## Python Code
~~~
import math
class Solution(object):
    base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        rs = 0
        count = len(s) - 1
        for i in s:
            index =  self.base.index(i)
            rs += (index+1)*math.pow(26, count)
            count -= 1 
        return int(rs)
~~~
