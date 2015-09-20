# [Move Zeroes](https://leetcode.com/problems/move-zeroes/)

## Description
Given an array `nums`, write a function to move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

For example, given `nums = [0, 1, 0, 3, 12]`, after calling your function, `nums` should be `[1, 3, 12, 0, 0]`.

Note:
You must do this **in-place** without making a copy of the array.
Minimize the total number of operations.
## Analysis
### Clarifications
Just be clear about the requirements!! Since I worked on a similar question([Sort Color](https://github.com/haoyuchen1992/Practice-Makes-Perfect/blob/master/Sort-Colors/Sort-Colors.md)), actually, at the beginning, I made a complete wrong direction. It needs to be kept the same relative order for non-zero value.

### Solution
Therefore, I choose to keep the order of non-value firstly. For the other spots, I can just fill with Zero. Simple and Elegant!!

* Time Complexity: `O(n)`
* Space Complexity: `O(1)`

## Python Code
~~~
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        l = len(nums)
        nonZero = 0
        for i in range(l):
            if nums[i] != 0:
                nums[nonZero] = nums[i]
                nonZero += 1
        for i in range(nonZero,l):
            nums[i] = 0
~~~
## Test Cases
~~~
1. [1,2,0,0] -> [1,2]
2. [0,1,0,2,0] -> [1,2]
3. [] -> []
4. [1] -> [1]
~~~