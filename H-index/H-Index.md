# [H-Index](https://leetcode.com/problems/h-index/)

## Description
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.  

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

## Analysis
**Method 1 --** Firstly sorting, and then starting from tail, until finding the maximum value.

**Method 2 --** Remember the h index will never larger than the length of citation list. So all the papers whose citation is larger than length will be contribure to index which is nor larger than length. There are a lot of traps! Please program it multiple times! Ideas from [LeetCode Discussion](https://leetcode.com/discuss/55952/my-o-n-time-solution-use-java).

## Python Code
~~~python
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        ## Method 1 -- Sorting
        # l = len(citations)
        # if l == 0:
        #     return 0
        # citations.sort()
        # hIndex = 0
        # for i in range(l):
        #     if (l-i) <= citations[i] and (l-i) > hIndex:
        #         hIndex = (l-i)
        
        # return hIndex
        
        ## Method 2 -- HIndex can only be range from 0 ~ lenght
        l =  len(citations)
        if l == 0:
            return 0
        nums = []
        for i in range(l+1):
            nums.append(0) 
        for j in range(l):
            if citations[j] > l:
                nums[l] += 1
            else:
                nums[citations[j]] += 1
        t = 0
        for i in list(reversed(range(l+1))):
            t = t + nums[i]
            if t >= i:
                return i
        return 0
~~~


## H-Index II -- Update
**Follow up for H-Index:** What if the citations array is sorted in ascending order? Could you optimize your algorithm?

~~~
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l =  len(citations)
        
        rs = 0
        # nums = [0] * (l+1)
        while citations:
            a =  citations.pop()
            if rs < a:
                rs = rs + 1
        return rs
~~~

This is simple but is also easy to make mistake!! Review it often.



        