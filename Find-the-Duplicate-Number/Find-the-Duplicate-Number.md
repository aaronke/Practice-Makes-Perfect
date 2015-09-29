# [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

## Description
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

**Note:**  
1.You must not modify the array (assume the array is read only).  
2.You must use only constant, `O(1)` extra space.  
3. Your runtime complexity should be less than `O(n2)`.  
4. There is only one duplicate number in the array, but it could be repeated more than once.

## Analysis
### Clarifications
1. Only constant space is used
2. Can't change value inplace (Read Only)
3. complexity should be less than `O(n^2)`
4. One duplicate number could be shown multiple times.  

The constriains should be really understood!
### Methods
Before thinking about the valid methods, we could think about various methods if there are no constrains noted above.

**Method 1:** Use hashtable to store the value and put value into hashtable.If one valueis already in hashtable, return it.

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`
* In-place change: `False`

**Method 2:** Sort the number list and then check one by one. Once finding same value, return it. --But it changes the array in place

* Time Complexity: `O(nlogn)`
* Space Complexity: `O(1)`
* In-place change: `True`

**Method 3:** Since the number value is `1 ~ n` and the length of array is `n+1`. So it is natrual to think about using index to exchange the value until finding the exchanged value is existing in other position.

* Time Complexity: `O(n)`
* Space Complexity: `O(1)`
* In-place change: `True`

**Method 4:** Naive method and check the same value. But the expected result is `Time exceed limit` and also not meet the requirement of time complexity

* Time Complexity: `O(n^2)`
* Space Complexity: `O(1)`
* In-place change: `False`

**Method 5:** Use refined binary search to find the number between `1 ~ n`. The challenage is about how to update the start and end. So for each iteration, we will check the number of value that larger than `middle` (`(end+start)/2`). If it is large than `middle -1`, then new `start` is `middle`, otherwise new `end` is `middle`.

Another key point is that this method can't reach to the result direction. Then end and start could only be two adjacent numbers. In order to check which one of them are the duplicates. And we need check the number list one more time. Finally, get the result! Idea is simple, but easy to make mistake in implementation!! **Only this method does meet all the requirements!**

* Time Complexity: `O(nlogn)`
* Space Complexity: `O(1)`
* In-place change: `False`

Remember to practice a lot on this one in future!






## Python Code
~~~
# import operator
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Method 1 : hashtable not acceptable, because O(1) space
        # hashTable = {}
        
        # for i in nums:
        #     if i not in hashTable:
        #         hashTable[i] = 1
        #     else:
        #         return i
        
        
        # Method 2: sorting O(nlogn) time with O(1) space -- No! it manipulate inplace
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return nums[i]
        
        # Method3 : But modified the code!! sorting O(n) time with O(1) space
        # count = 0
        # l = len(nums)
        # while count < l:
        #     while nums[count] != count:
        #         temp =  nums[count]
        #         if temp == nums[temp]:
        #             return temp
        #         else:
        #             nums[count] = nums[temp]
        #             nums[temp] = temp
        #     count += 1
        
        # O(n^2) -- Time exceed Limit
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         xorRs = operator.xor(nums[j], nums[i])
        #         if xorRs == 0:
        #             return nums[i]
        
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[j] - nums[i]) == 0:
        #             return nums[i]
        
        
        # It's hard one, because there are a lot edage cases!!
        l = len(nums)
        end = l-1
        start = 1
        constant = end/2
        
        while start < end-1:
            middle = (end + start)/2
            count = 0
            for i in range(l):
                if nums[i] < middle:
                    count += 1
            if count > middle - 1:
                end = middle
            else:
                start = middle
        count = 0
        for i in range(l):
            if nums[i] == start:
                count += 1
        if count > 1:
            return start
        return end
~~~

## Test Cases
~~~
1. [1,2,1] -> 1
2. [7,9,7,4,2,8,7,7,1,5] -> [7]
3. [1,1] -> 1
4. [2,1,3,4,2] -> 2
~~~
