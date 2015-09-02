# [Single Number II](https://leetcode.com/problems/single-number-ii/)

## Description
Given an array of integers, every element appears three times except for one. Find that single one.

**Note:** Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
## Analysis
Method 1 is using hashtable. The time complexity is `O(n)`, but the space comlexity is `O(n)` too. It is not the perfect answer for is issue. It also happens to method 2. But the reason I put the code here is that from the simplity of code and readablility, Both them are better and easier to understand. Simple and 'stupid' methods are not alwasy bad.

As for method 3 (Use bit manipulation), there is a good explanation in this Chinese [blog](http://www.cnblogs.com/zuoyuan/p/3719753.html). Basically, thinking about each bit will have three `1` and if not, it means that it is a effective bit for the number we need to find.

One misunderstanding point I have here is that I think the special number will have one or two. But the fact is that we only considers about the case with one specail number.

## Python Code
~~~python
### Method 1 -- hashtable
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        for i in nums:
            if i not in h:
                h[i] = 1
            elif h[i] != 3:
                h[i] += 1
            if  h[i] == 3: # This has to be check after each loop, so no "else"!!
                h.pop(i)
        return h.items()[0][0]
~~~

~~~
### Method 2 -- set
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a= set(nums)
        a = sum(a)*3 -sum(nums)
        a = a/2
        return a
~~~

~~~
### Method 3 -- bit manipulation

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        one = 0; two = 0; three = 0
        for i in range(len(A)):
            two |= A[i] & one             
            one = A[i] ^ one              
            three = ~(one & two)　　　　  
        	  one &= three
            two &= three
        return one
~~~

## Notes
1. when we want to get the key of dictionary, we can transfer dictionary into iterable items firstly and then get the key by index(Applied in method 1). `h.items()[0][0]` is to get the first(only) key in dictionary `h`.


