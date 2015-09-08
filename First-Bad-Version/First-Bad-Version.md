# [First Bad Version](https://leetcode.com/problems/first-bad-version/)

## Description
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which will return whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

## Analysis
Method 1 -- Naive(Failed in test) -- We could checking the bad verson starting from `1` until we find the first bad one. But the problem is that it will cost too many cicles to reach there. 

* Time Complexity -- `O(n)`
* Space Complexity -- `O(1)` (originall I am thinking about using array to list the version number and it turns out to be an unnecessary and bad idea!)

Method 2 -- Binary Search --  Just remember the start and ending number and take advantage of binary search. When checking the version number is bad, update ending number with checking number. If not, update start number with checking number plusing one.

* Time Complexity -- `O(logn)`
* Space Complexity -- `O(1)`

## Python Code
~~~python
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Naive Method 1 -- Too much space for arraylist 
        # for i in range(1, n+1):
        #     if isBadVersion(i):
        #         return i
        # s = 1
        
        # Naive Method 2 -- No way and it will get 'Time Limit Exceed'
        # while s <= n:
        #     if isBadVersion(s):
        #         return s
        #     s += 1
        
        # Failed Binary search implementation --Too much memory comsumption 
        # if n == 1:
        # 	 return 1 
        # l = n
        # versions = range(1, n+1) 
        # checking = l/2
        # while l > 1:
        #     if self.isBadVersion(checking):
        #         versions = versions[:checking+1]
        #     else:
        #         versions = versions[checking+1:]
        #     l =  len(versions)
        #     checking = l/2
        # return versions[0]
        
        start = 1
        end = n
        checking = (end + start)/2
        while (end != start):
            if isBadVersion(checking):
                end = checking
            else:
                start =  checking + 1
            checking = (end+start)/2
        return start
~~~
## Notes
1. Thinking about test cases before and while implementation algorithm. For example, for this issue, there are serveral cases we can test by ourself, such as `n = 1, 2, 3 or 123445434`.

2. Be careful about array list usage (`range(n)`). `n` could be very large number in test case. So it will cost way much space.  
