
# [Ugly Number](https://leetcode.com/problems/ugly-number-ii/)

## Description
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include `2, 3, 5`. For example, `1, 2, 3, 4, 5, 6, 8, 9, 10, 12` is the sequence of the first `10` ugly numbers.

Note that `1` is typically treated as an ugly number.

## Analysis

**Method 1 -- Navie :** The naive method is to check whether the number is ugly one by one. But since the gap between ugly numbers will increase along with the number, the computation complexity for this method is huge (Almost exponential).

* Time complexity: `O(k)` (`k` is the `n-th` ugly number)
* Space complexity: `O(1)` 

**Method 2 -- Dynamic Programming**: Considering about the hint that focusing on how to generate ugly number, induction in math could be applied. Assume we know the list of ugly numbers, We can find that every subsequence is the ugly-sequence itself (1, 2, 3, 4, 5, …) multiply 2, 3, 5.

	(1) 1×2, 2×2, 3×2, 4×2, 5×2, …
	(2) 1×3, 2×3, 3×3, 4×3, 5×3, …
	(3) 1×5, 2×5, 3×5, 4×5, 5×5, …

Then similar as merge sorting, we combine those three lists and the result is the ugly number list.  
(Idea: http://www.geeksforgeeks.org/ugly-numbers/)

* Time complexity: `O(n)` 
* Space complexity: `O(n)` 

##  Python Code
~~~python
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Method 1 -- Naive (brute force counting)
        # count = 1
        # start = 1
        # temp = 0
        # if n == 1:
        #     return start
        # while (count < n):
        #     start += 1
        #     # if self.checkUgly(start):
        #     temp = start
        #     while temp%2 == 0:
        #         temp =  temp/2
        #     while temp%3 == 0:
        #         temp =  temp/3
        #     while temp%5 == 0:
        #         temp =  temp/5
        #     if temp == 1:
        #         count += 1
        # return start
        
        # Method 2 -- Dynamic Programming       
        uglyList = [1]
        index2, index3, index5 = 0, 0, 0
        
        while( len(uglyList) < n):
            v2, v3, v5 = uglyList[index2]*2, uglyList[index3]*3, uglyList[index5]*5 
            minNum = min(v2, v3, v5)
            if minNum == v2:
                index2 += 1
            if minNum == v3:
                index3 += 1
            if minNum == v5:
                index5 += 1
            uglyList.append(minNum)
            
        return uglyList[n-1]
~~~

## Notes
Dynamic programing is the idea that asumme an existing `n-th` result is already known, feature out a way to get `(n+1)-th` result. In this question, the way is to mutiple `2, 3, 5` to the existing ugly number list. Great idea!
