# [Valid Anagram](https://leetcode.com/problems/valid-anagram/)

## Analysis
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,  
s = "anagram", t = "nagaram", return true.  
s = "rat", t = "car", return false.  

**The fist step** is to understand what anagram is. Anagram is to rerange the word into a new word by using all the original characters. Each character is only allowed to used exactly once. 

So we should clariy whether two empty string  are valid anagram, the answer from Leetcode test is YES. And then obviously, with different length of strings, it will definietly not be valid. If they are with same lengths and equal with each other after sorting, they are valid anagram.

1. Sorting (See code below)
2. hashtable 

####tags: *Easy, Sort, Anagram*

## Python Code

	class Solution(object):
	    def isAnagram(self, s, t):
	        """
	        :type s: str
	        :type t: str
	        :rtype: bool
	        """
	        lens = len(s)
	        lent = len(t)
	        
	        if (lens != lent):
	            return False
	        
	        if sorted(s) != sorted(t):
	            return False
	        return True
        
## Notes
1. What is the difference between `sort` and `sorted` in Python?

	In python, `sort` is build-in function for list object and it will modifiy list in place. However, `sorted` is a build-in function for iterable object. And it will return a new sorted list.	

2. How to sort an object based on one attribute

   `key` attribut and lambda method will play a role here. Here is the example below. you can name as whatever you like, in example below, it is named as `student`.
   
	`sorted(student_objects, key=lambda student: student.age)  # sort by age`
   
   [More details in offical docs](https://wiki.python.org/moin/HowTo/Sorting)


