# [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

## Description
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

## Analysis
Method 1 -- Check all the possible pairs
* Time complexity: `O(n^2)`
* Space complexity: `O(1)`

Method 2 -- Hashtable
* Time complexity: `O(n)`
* Space complexity: `O(n)`

Method 1 -- Sorting
* Time complexity: `O(nlogn)`
* Space complexity: `O(n)`

## Python Code
~~~
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Naive -- O(n^2) -- Time Limit Exceed
        # hashNum = []
        # for i in nums:
        #     if i not in hashNum:
        #         hashNum.append(i)
        #     else:
        #         return True
        # return False
        
        # Naive -- Apply hashtable O(n) -- 56ms
        # hashNum = {}
        # for i in nums:
        #     if i not in hashNum:
        #         hashNum[i] = 1
        #     else:
        #         return True
        # return False
        
        # Naive -- Sorting 52 ms
        # l =  len(nums)
        # if l < 2:
        #     return False
        # nums.sort()
        # for i in range(l-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False
        
        # Set solution for python
        numsSet =  set(nums)
        if len(nums) == len(numsSet):
            return False
        return True
~~~

## Notes
1. Remember the usage case of set in python(Offical [docs](https://docs.python.org/2/tutorial/datastructures.html)).
