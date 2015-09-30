# [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

## Description
Write a function to find the longest common prefix string amongst an array of strings.
## Analysis
### Clarifications
1. What do you mean prefix?
2. If there is one string, should I return that string directly?
3. What should I return when input is empty list?

### Method
Just naive and assume that the first one is longest prefix string. And update it by checking other strings one by one. Specifically, be careful when you set `aa` as a longest prefix. But if you get second string as `a` and you can update longest prefix instantly as `a` , because the prefix should be the minimum length among two.

* Time Complexity: `O(n)`
* Space Complexity: `O(1)`

## Python Code
~~~
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        l = len(strs)
        if l == 0:
            return ''
        longString = strs[0]
        
        for i in range(1,l):
            l_long = len(longString)
            l_str = len(strs[i])
            if l_str < l_long:
                longString = longString[:l_str]
                l_long = l_str
            
            for j in range(l_long):
                if longString[j] != strs[i][j]:
                    longString = longString[:j]
                    break
            if len(longString) == 0:
                return longString
        
        return longString
~~~
## Test Cases
~~~
1. ['aa','aac','ab'] -> 'a'
2. ['aa','a'] -> 'a'
3. ['abdfd'] -> 'abdfd'
~~~