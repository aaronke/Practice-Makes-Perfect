# [Word Pattern](https://leetcode.com/problems/word-pattern/)

## Description
Given a pattern and a string str, find if str follows the same pattern.

Examples:

1. pattern = "abba", str = "dog cat cat dog" should return true.
2. pattern = "abba", str = "dog cat cat fish" should return false.
3. pattern = "aaaa", str = "dog cat cat dog" should return false.
4. pattern = "abba", str = "dog dog dog dog" should return false.

**Notes:**  

1. patterncontains only lowercase alphabetical letters, and str contains words separated by a single space. Each word in str contains only lowercase alphabetical letters.
2. Both pattern and str do not have leading or trailing spaces.
3. Each letter in pattern must map to a word with length that is at least 1.
## Analysis
Use two hashtable to store `pattern` and `str` repectively. During the building process of hashtable, check if the freqency(value of hashtable)  are the same.

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

## Python Code
~~~
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strList = str.split(' ')
        
        l = len(pattern)
        strl = len(strList)
        
        if l != strl:
            return False
        
        count = 0
        strMap = {}
        patternMap = {}
        while count < l:
            if pattern[count] not in patternMap:
                patternMap[pattern[count]] = 1
            else:
                patternMap[pattern[count]] += 1
            if strList[count] not in strMap:
                strMap[strList[count]] = 1
            else:
                strMap[strList[count]] += 1
    
            if strMap[strList[count]] != patternMap[pattern[count]]:
                    return False
            count += 1
        
        return True
~~~
## Test Cases
~~~
1. "abba", "a a a a" -> False
2. "abba", "dog a a dog" -> True
3. "a","dog" -> True
4. "aaa" -> "dog dog dog" -> True
5. "aab" -> "dog dog see" -> True
~~~
