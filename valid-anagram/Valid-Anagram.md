# [Valid Anagram](https://leetcode.com/problems/valid-anagram/)

## Analysis
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,  
s = "anagram", t = "nagaram", return true.  
s = "rat", t = "car", return false.  

**The fist step** is to understand what anagram is. Anagram is to rerange the word into a new word by using all the original characters. Each character is only allowed to used exactly once. 

So we should clariy whether two empty string  are valid anagram, the answer from Leetcode test is YES. And then obviously, with different length of strings, it will definietly not be valid. If they are with same lengths and equal with each other after sorting, they are valid anagram.
                  
1. Sorting  
    * Time Complexity:  O(nlogn) 
    * Space Complexity: O(n) or O(1) (Depend on sorting algorithm in python)
2. hashtable
    * Time Complexity:  O(n) 
    * Space Complexity: O(n)
3. Array -- Use array to replace hashtable **(Best)**. Since all the input are lower-case letters, we could choose to use a lenghth-26 array. And therefore, index would be similar as the key in hashtablek. 
    * Time Complexity:  O(n) 
    * Space Complexity: O(1)  

    
####tags: *Easy, Sort, Anagram*

## Python Code
~~~python
import string # For method 3

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
        # Method 1 -- Sorting       
        # if sorted(s) != sorted(t):
        #     return False
        # return True    
        
        # Method 2 -- Hashtable 
        # sdic = {}
        # for i in s:
        #     if i not in sdic:
        #         sdic[i] = 1
        #     else:
        #         sdic[i] = sdic[i] + 1
        
        # tdic = {}        
        # for i in t:
        #     if i not in tdic:
        #         tdic[i] = 1
        #     else:
        #         tdic[i] = tdic[i] + 1   
        
        # for key, value in sdic.iteritems():
        #     if key not in tdic:
        #         return False
        #     if tdic[key] != value:
        #         return False
        # return True
        
        # Method 3 -- Array
        numberAlpha = [0]*26 #26 character
        for i in s:
            numberAlpha[string.lowercase.index(i)] += 1
        for i in t:
            numberAlpha[string.lowercase.index(i)] -= 1
        for i in numberAlpha:
            if i != 0:
                return False
        return True
~~~        
## Notes
1. What is the difference between `sort` and `sorted` in Python?  
	In python, `sort` is build-in function for list object and it will modifiy list in place. However, `sorted` is a build-in function for iterable object. And it will return a new sorted list.

2. How to sort an object based on one attribute  
   `key` attribut and lambda method will play a role here. Here is the example below. you can name as whatever you like, in example below, it is named as `student`.
	`sorted(student_objects, key=lambda student: student.age)  # sort by age`
   [More details in offical docs](https://wiki.python.org/moin/HowTo/Sorting)
3. How to iterate dictionary in python  
Stackoverflow [link](http://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops-in-python) and code example:  
**Need both key and value:**  
`for key, value in d.iteritems():`  
*Note:* in python3, `d.items()` will replace `d.iteritems()`  
**Only need key:**  
`for key in d:`  
4. This problem has been seen in Epic interview. It is required to use hashtable method. See more details on [一亩三分地](http://www.1point3acres.com/bbs/thread-140532-1-1.html).  
5. How to init an array with specific length
StackOverflow [Link](http://stackoverflow.com/questions/521674/initializing-a-list-to-a-known-number-of-elements-in-python)  
For one D:`newArray = [0]*length`  
For two D: `newArray = [[0]\*length1, [0]*length2]
6. how to get the off-set index of character in python  
We need introduce string module in python. It will get the index for each letters. (Applied in Method 3)

~~~python
>>> import string
In [63]: string.lowercase.index('c')
Out[63]: 2

In [64]: string.lowercase
Out[64]: 'abcdefghijklmnopqrstuvwxyz'

In [65]: string.uppercase
Out[65]: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
~~~	

7. All the operator with eaqua sign, the non-equal sign should be left.
Examples, `<=`, `!=`, `>=` and so on.



