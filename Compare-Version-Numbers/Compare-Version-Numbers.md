# [Compare Version Numbers](https://leetcode.com/problems/compare-version-numbers/)

## Description
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, `2.5` is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:
~~~
0.1 < 1.1 < 1.2 < 13.37
~~~
## Analysis
### Clarifications
1. Do both of inputs has the same number of dots? No!

### Method
So based on the dots, split the two inputs into two arrays. And then compare the integer value of the elements with the same index.

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

## Python Code
~~~
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split('.')
        version2 = version2.split('.')
        point = 0
        l1 = len(version1)
        l2 = len(version2)
        end1 = min(l1, l2)
        end2 = max(l1, l2)
        while point < end1:
            num1 = int(version1[point])
            num2 = int(version2[point])
            if num2 > num1:
                return -1
            if num2 < num1:
                return 1
            point += 1
        if end1 == end2:
            return 0
        remain = []
        if end2 == l2:
            remain = version2[point:]
        elif end2 == l1:
            remain = version1[point:]
        for i in remain:
            if int(i) > 0:
                if end2 == l2:
                    return -1
                elif end2 == l1:
                    return 1
        
        return 0
        
~~~
## Test Cases
~~~
1. "1.1"
   "1.1.0.0.0"  -> 0
2. "1"
   "0"   -> 1
3. "1.1"
   "1.2.0.0.0" -> -1
~~~
