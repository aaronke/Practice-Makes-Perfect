# [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

## Description
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., `0 1 2 4 5 6 7` might become `4 5 6 7 0 1 2`).

Find the minimum element.

You may assume no duplicate exists in the array.
## Analysis
### Clarifications
1. What is the requirement for the complexity?
2. How many rotation will be done for the list? Only once?

### Methods
**Naive Four Cases:**
Assume that rotation is only applied once. And then there are four cases to get the minimum number in this list. Therefore, we implemented in that way!  

* Time Complexity: `O(n)`
* Space Complexity: `O(1)`

**Binary Search:**
Original Notes from [Link](http://bangbingsyb.blogspot.com/2014/11/leecode-find-minimum-in-rotated-sorted.html)
Original List: `[0,1,2,3,4,5,6]`
Case One: `2,3,4,5,6,0,1`
Case Two: `5,6,0,1,2,3,4`

For case one, `nums[mid] > nums[end]`, then the minimum must be on the range of `[mid, end]`.

For case two, `nums[mid] < nums[end]`, then the minum must be on the range of `[start, mid]`

It takes time to understand it! It's still hard to think it instantly.

Base cases: 
1. When start = end, then A[start] is min.
2. start+1 = end, then if A[mid] = A[start], min is the min between A[mid] and A[end].

* Time Complexity: `O(logn)`
* Space Complexity: `O(1)`

## Python Code
~~~
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # lenNums = len(nums)
        # if lenNums == 0:
        #     return None
        # if lenNums == 1:
        #     return nums[0]
        
        # leftUp = False
        # rightUp = False
        # leftVal = nums[0]
        # rightVal = nums[lenNums-1]
        
        # if leftVal < nums[1]:
        #     leftUp = True
        # if rightVal < nums[lenNums-2]:
        #     rightUp = True
        
        # if leftUp and rightUp:
        #     return min(leftVal, rightVal)
        
        # if leftUp and not rightUp:
        #     compareVal = leftVal
        #     for i in range(lenNums-1):
        #         if nums[i] > nums[i+1]:
        #             compareVal = nums[i+1]
        #     return min(leftVal, compareVal)
        # if not leftUp and rightUp:
        #     compareVal = leftVal
        #     for i in range(lenNums-1):
        #         if nums[i] < nums[i+1]:
        #             compareVal = nums[i]
        #     return min(rightVal, compareVal)
        # if not leftUp and not rightUp:
        #     for i in range(lenNums-1):
        #         if nums[i] < nums[i+1]:
        #             return nums[i]
        
        # Binary Search
        end = len(nums) -1
        start = 0
        
        while end > start:
            mid = (end+start)/2
            if nums[mid] < nums[end]:
                end =  mid
            else:
                start = mid + 1
        return nums[start]
~~~
## Test Cases
~~~
1. [1,2] -> 1
2. [7,6,5,11,8] -> 5
3. [4,5,6,7,0,1,2] -> 0
~~~