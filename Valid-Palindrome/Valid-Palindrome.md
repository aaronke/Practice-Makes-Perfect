# [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

## Description
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,  
`"A man, a plan, a canal: Panama"` is a palindrome.  
`"race a car"` is not a palindrome.

**Note:** Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
## Analysis
### Clarifications
1. Do we only care about number and alphabet? Yes!
2. Do we consider about upper case? Only care about lower!

### Methods
**Method 1:** Use two pointers to compare in pair. Remeber to move forward when getting non-alphabet and non-number character.

* Time Complexity: `O(n)`
* Space Complexity: `O(1)`

Method 2: Firstly, create a list to store all the alphabet and number characters in sequence. And then join it together and use simpler two pointer method to judge whether it is palindrome.

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

**Note: ** why not just use string to get new string but use list? Because string is imutable in python, each time string is changed, it need to create complete new string. So it is very time-comsuming.

~~~
        # Good:) List to get new string
        newS = []
        for c in s:
            if c.isalpha() or c.isdigit():
                newS.append(c)
        newS = ''.join(newS)
~~~

~~~
        # Bad:( String to get new string --Exceed Time Limit
        newS = ""
        for c in s:
            if c.isalpha() or c.isdigit():
                newS += c
~~~

## Python Code
~~~
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # s = s.lower()
        # end = len(s)-1
        # start = 0
        
        # while start < end:
        #     while start+1 <= end and (not s[start].isalpha() and not s[start].isdigit()) :
        #         start += 1
        #     while start+1 <= end and (not s[end].isalpha() and not s[end].isdigit()):
        #         end -= 1 
        #     if s[start] == s[end]:
        #         start += 1
        #         end -= 1
        #     else:
        #         return False
        
        # return True
        
        # Naive -- Time Limite Exceed
        # newS = ""
        # for c in s:
        #     if c.isalpha() or c.isdigit():
        #         newS += c
        
        # end = len(newS) - 1
        # start = 0
        # while start < end:
        #     if newS[start] == newS[end]:
        #         start += 1
        #         end -= 1
        #     else:
        #         return False
        
        # return True
        
        # Refine method -- Because string is immutable, each time it will create a new. So instead of using string, apply list to store new string and then combine it.
        s = s.lower()
        newS = []
        for c in s:
            if c.isalpha() or c.isdigit():
                newS.append(c)
        newS = ''.join(newS)
        
        end = len(newS) - 1
        start = 0
        while start < end:
            if newS[start] == newS[end]:
                start += 1
                end -= 1
            else:
                return False
        
        return True
~~~
## Test Cases
~~~
1. [.a.] -> True
2. [..a.] -> True
3. [] -> True
4. [aba] -> True
5. [abba] -> True
6. [abc] -> False
7. [1b2] -> False
8. [11] -> True
9. [abcba] -> True
~~~