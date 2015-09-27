
# [ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)

## Description
The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

~~~
P   A   H   N
A P L S I I G
Y   I   R
~~~
And then read line by line: `"PAHNAPLSIIGYIR"`
Write the code that will take a string and make this conversion given a number of rows:

~~~
string convert(string text, int nRows);
~~~
`convert("PAYPALISHIRING", 3)` should return `"PAHNAPLSIIGYIR"`.
## Analysis
### Clarifications
1. Run small example to make sure understand correctly. At the beginning, I though if iput is `"ABCDE",4`, we should get `ABECD`. But the fact is that it should be `ABCED`. 

### Method
Instead of getting a big string at the first, it is better to create `numRows` lists and join them at the end.

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

## Python Code
~~~
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rs = []
        for i in range(numRows):
            oneRow = []
            rs.append(oneRow)
        
        currentRow = 0
        isLong = True
        count = 0
        for i in s:
            if count < numRows and isLong:
                rs[count].append(i)
                count += 1

            if count < numRows-2 and not isLong:
                rs[numRows-2-count].append(i)
                count += 1
                
            if count == numRows and isLong:
                count = 0
                isLong = False
            if count == numRows-2 and not isLong:
                count = 0
                isLong = True

        rsString = ""
        for row in rs:
            rsString += "".join(row)
        
        return rsString
~~~
## Test Cases
~~~
1. "ABCDE", 4 -> "ABCED"
2. "A", 1 -> "A"
3. "PAYPALISHIRING", 3 -> "PAHNAPLSIIGYIR"
~~~
