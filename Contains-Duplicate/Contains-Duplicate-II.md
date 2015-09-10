# [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)

## Description
Given an array of integers and an integer `k`, find out whether there are two distinct indices `i` and `j` in the array such that `nums[i] = nums[j]` and the difference between `i` and `j` is at most `k`.

## Analysis
**Method 1 **-- Naive -- Just check it from the starting point. Search and compare all the possible range.
* Time Complexity -- `O(n^2)`
* Space Complexity -- `O(1)`

**Method 2**-- Two pointers. Based on k, checking k*n times. It will be very efficient when k is small.
* Time Complexity -- `O(n)`
* Space Complexity -- `O(1)`

**Method 3 and 4**-- Take advantage of hashtable and record the minimum gap for the pair with the same numbers.

* Time Complexity -- `O(k*n)`
* Space Complexity -- `O(n)` --  hashtable size

**Method 5**-- Think about sliding window. The window size is `k`. If there is duplicate within `k` elements, then it returns `True`. Remeber to use set data structure in python and record end and start index. 

* Time Complexity -- `O(k*n)`
* Space Complexity -- `O(k)` -- window size

## Python Code
~~~Python
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        # Method 1 Naive -- O(n^2) -- Time Limited Exceed
        # l =  len(nums)
        # for i in range(l-1):
        #     for j in range(i+1,l):
        #         if (nums[i] == nums[j]) and ((j-i) <= k):
        #             return True
        # return False
        
        # Method 2 Two pointers -- Time Limited Exceed
        # l =  len(nums)
        # for i in range(1, k+1):
        #     for j in range(l-i):
        #         if nums[j] == nums[i+j]:
        #             return True
        # return False
        
        
    #     Method 3 Hashtable 
    #     l = len(nums)
    #     hashNums = {}
    #     for i in range(l):
    #         if nums[i] not in hashNums:
    #             hashNums[nums[i]] = [i]
    #         else:
    #             hashNums[nums[i]].append(i)
    #     for hashNumVal in hashNums.itervalues():
    #         # If I move the length checking into checkGap, the time cost will jump from 64ms to 136ms
    #         if (len(hashNumVal) >= 2) and self.checkGap(hashNumVal,k):
    #             return True
    #     return False
    
    # def checkGap(self, nums, k):
    #     l =  len(nums)
    #     small = nums[1] - nums[0]
    #     for i in range(l-1):
    #         if nums[i+1] - nums[i] < small:
    #             small = nums[i+1] - nums[i]
    #     if small <= k:
    #         return True

        # Method 4  Refined hashTable
        # l = len(nums)
        # hashNums = {}
        # minGap = k+1
        # for i in range(l):
        #     if nums[i] not in hashNums:
        #         hashNums[nums[i]] = [i]
        #     else:
        #         if len(hashNums[nums[i]]) != 1:
        #             hashNums[nums[i]].pop(0)
        #         hashNums[nums[i]].append(i)
        #         if (hashNums[nums[i]][1] - hashNums[nums[i]][0]) < minGap:
        #             minGap = hashNums[nums[i]][1] - hashNums[nums[i]][0]
                    
        # if minGap <= k:
        #     return True
        # return False
        
        # Method 5 Slide Window
        setNum = set()
        start = 0
        end = 0
        for i in range(len(nums)):
            if  (nums[i] not in setNum):
                end += 1
                setNum.add(nums[i])
            else:    
                return True
            if (end-start > k):
                setNum.remove(nums[start])
                start += 1 
        return False
    
~~~
## Notes
1. Remember to try to reduce the times of invoking embedded funtions. So for method 3, the refinement that moving the length checking outside of embedded function, will dramatically decrease the numbers of using checkGap method.

2. The refinement from method 3 to method 4 is just because the only thing determin the return value is the minimum index gap between the same values in the number list.

3.  How to init an empty set. StackoverFlow [Link](http://stackoverflow.com/questions/6130374/empty-set-literal-in-python)
 `variableName = set()`



        
    
            
        
                    
            
            
        
        
        