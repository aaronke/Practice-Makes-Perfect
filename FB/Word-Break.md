# [Word Break](http://www.lintcode.com/en/problem/word-break/)

## Description
Given a string s and a dictionary of words dict, determine if s can be break into a space-separated sequence of one or more dictionary words.

**Example**  
Given s = `"lintcode"`, dict = `["lint", "code"]`.

Return true because "lintcode" can be break as "lint code".
## Analysis
### Clarifications
1. Is the input`dict` a dictionary in python? It looks like it is just a list of string.
2. Can a element from the list be used for multiple times?
3. What if input `s` is an empty string? What should I return?
4. What if there is white space within the input `s` ? Do we consider about that situation?

## Methods
DFS -- Deepth First Search. So use recursion and once finding one result, then update with a shorter string. Start a new wordbreak method until the input string is empty one, then return True.

* Time Complexity: `O(n^2)`
* Space Complexity: `O(n)`

DF -- Dynamic Programming. Use a array to store the status of each character. If the value with index `A` is true, then it means all the chracters before `A` are the reachable now. If the value associating the index `len(s)` is `True`, it means the whole list is reachable now and return `True`.

* Time Complexity: `O(n^2)`
* Space Complexity: `O(n)`

## Python Code
~~~
class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        # Exceed Time Limit
        if len(s) == 0:
            return True


        for c in dict:
            ls = len(s)
            lc = len(c)
            if lc > ls:
                continue
            count = 0
            while count < lc:
                if c[count] == s[count]:
                    count += 1
                    continue
                break
            if count == lc and self.wordBreak(s[lc:], dict):
                    return True
        
        return False
~~~

~~~
class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        # write your code here
        if len(s) == 0:
            return True
        targetS = [s]
        
        while targetS:
            s = targetS.pop()
            for c in dict:
                ls = len(s)
                lc = len(c)
                if lc > ls:
                    continue
                count = 0
                while count < lc:
                    if c[count] == s[count]:
                        count += 1
                        continue
                    break
                if count == lc and lc < ls:
                    targetS.append(s[lc:])
                elif count == lc and lc == ls:
                    return
           
        return False
~~~

~~~
class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        # write your code here
        ls = len(s)
        targetS = [False for i in range(ls+1)]
        # targetS = [False] * (ls+1)
        
        targetS[0] = True
        for i in range(1, ls+1):
            for j in range(i):
                if targetS[j] and (s[j:i] in dict):
                    targetS[i] = True
                
        return targetS[ls]
~~~
## Test Cases
~~~
1. "a", ["a"] -> True
2. "aaba", ["a", "b"] -> True
3. "bcbcab", ["a","b"] -> False
4. "bcbcab", ["bcb","ca", "b"] -> True
~~~