# [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)

## Description
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given `"egg"`, `"add"`, return true.

Given `"foo"`, `"bar"`, return false.

Given `"paper"`, `"title"`, return true.

Note: You may assume both s and t have the same length.
## Analysis
### Clarifications
1. Is it case sensative? Yes!
2. Do the input contains specical charactoers or numbers? Yes!

### Method
With the help of hashtable, yse number to lable each new characters. And then create a new list with the new labels. If s and t create the same list, then it showns that they are isomorphic (return `True`). Otherwise, return `False`.

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

## Python Code
~~~
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # s = s.lower()
        # t = t.lower()
        l = len(s)
        hashS = {}
        hashT = {}
        cS = 0
        cT = 0
        for i in range(l):
            if s[i] not in hashS:
                hashS[s[i]] = str(cS)
                cS += 1
            if t[i] not in hashT:
                hashT[t[i]] = str(cT)
                cT += 1
        strS = []
        strT = []
        
        for i in range(l):
            strS.append(hashS[s[i]])
            strT.append(hashT[t[i]])
        
        # strS = "".join(strS)
        # strT = "".join(strT)
        if strS == strT:
            return True
        return False
        
~~~
## Test Cases
~~~
1. "abba","abab" -> False
2. "paper","title" -> True
3. "a..", "egg" -> True
4. "Kv>>i", "happy" -> True
~~~