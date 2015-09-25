
# [First Missing Positive](https://leetcode.com/problems/first-missing-positive/)

## Description
Given an unsorted integer array, find the first missing positive integer.

For example,
Given `[1,2,0]` return `3`,
and `[3,4,-1,1]` return `2`.

Your algorithm should run in O(n) time and uses constant space.
## Analysis
### Clarifications
1. When you say first missing number, does it mean there are multiple missing numbers, but only the first one need to be returned?

### Methods
Firstly, don't try to meet all the requirements(`O(n)` time and constant space). I tested serveral bruteforce methods. It does work on leetcode. 

So the first bruteforce method is to do sorting first and then find the first missing positive number. 

* Time Complexity: `O(nlogn)`
* Space Complexity: `O(1)`

Another bruteforce is to create an array with length of the maximum number. And then each time finding the number, use the number as index and set the status vaiable as `True`. The advantage is to obtained `O(n)` time, however, it has to use a lot of space on the array.

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

The best way to do will meet the requirements (`O(n)` time and `O(1)` space). The basic idea is to use the value of elment as index and switch the postion, in order to get the appointment similar as `nums[n] = n`. More practice should be done for this one!!

* Time Complexity: `O(n)`
* Space Complexity: `O(1)`


## Python Code
~~~
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Naive Sorting
        # nums.sort()
        # pre = 0
        # for i in nums:
        #     # This is the trick!! if i is not larger than pre, don't need to be checked.
        #     if i <= pre:
        #         continue
        #     else:
        #         if i != (pre + 1):
        #             return (pre+1)
        #         else:
        #             pre = pre+1
        # retur2n pre+1
        
        # Method 2 -- O(n), but not constant variable
        # if len(nums) == 0:
        #     return 1
        # maxNum = max(max(nums), 1)
        # status = [False] * maxNum
        
        # for i in nums:
        #     if i > 0 and not status[i-1]:
        #         status[i-1] = True
        
        # for j in range(len(status)):
        #     if not status[j]:
        #         return j+1
        # return len(status)+1
        
        # O(n) method -- based on the index's limitation!!
        lenNum = len(nums)
        for i in range(lenNum):
            target = nums[i]
            # Magic happens here (while loop)
            while target > 0 and target <= lenNum and nums[target-1] != target:
                newTarget = nums[target-1]
                nums[target-1] = target 
                target = newTarget
                
        for i in range(lenNum):
            if nums[i] != i+1:
                return i+1
        
        return lenNum+1
~~~

## Test Cases
~~~
1. [0,2,2,1,1] -> 3
2. [1,2] -> 3
3. [-1,-2,1,3] -> 2
4. [0] -> 1
~~~