
# [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

## Description
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array `[2,3,1,2,4,3]` and `s = 7`,the subarray `[4,3]` has the minimal length under the problem constraint.
## Analysis
### Clarifications
1. In order to get the sum, can we use one number for multiple times? NO.
2. Is this input array sorted? NO
3. When there are multiple results, like if the input number is 7, and I have [8], and [9], Can I return either of them?
4. What do you mean by subarray? It should be part of array with the adjcent index. Otherwise, it is not subarray!!(`I misunderstood this one!`)

### Method
**Brute force:** All these three implementations are either exceeding the time limit or run out of storage limit. 

First idea is using dynamic programming(recursion) -- `T(n) = T(n-1) + O(n)`. However, since each element need a level of function callback. It would cost too much resource. Therefore its implementation gets `Memory Limit Exceed`.

Another idea is to start from 1 and enumerate all the sublists level by level, until finding the one with smallest length whose sum is larger or equal to `s`. But `O(n^2)` lets it exceed time limit.


* Time Complexity: `O(n^2)`
* Space Complexity: `O(n)`

**Linear Solution:** Consider the solution in the leetcode discussion - [link](https://leetcode.com/discuss/36384/python-o-n-and-o-n-log-n-solution). It showns both `O(n)` and `O(nlogn)` solutions.

To be updated more!!

## Python Code
~~~
class Solution(object):
    #     """
    #     :type s: int
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    
    # Time Exceed Limit
    # rs = 0
    # def minSubArrayLen(self, s, nums):
    #     l = len(nums)
    #     for size in range(1,l+1):
    #         rs = self.minSubArray(size, nums, s)
    #         if rs:
    #             return len(rs)
    #     return 0

    # def minSubArray(self, size, nums, s):
    #     l = len(nums)
    #     for i in range(size, l):
    #         if sum(nums[(i-size):i]) >= s:
    #             return nums[(i-size):i]
    #     return None

    # Memory Limit Exceed    
    # def minSubArrayLen(self, s, nums):
    #     if not nums:
    #         return 0
    #     lastRs = self.minSubArrayLen( s, nums[1:])
    #     rs = lastRs
    #     end = lastRs + 1
    #     if lastRs == 0:
    #         end = len(nums)+1
    #     for i in range(1, end):
    #         if sum(nums[:i]) >= s:
    #             rs = i
    #     return rs
    
    # def minSubArrayLen(self, s, nums):
    #     if not nums:
    #         return 0
    #     count = 0
    #     lenNums = len(nums)
    #     rs = lenNums + 1
    #     while count < lenNums:
    #         count += 1
    #         for i in list(reversed(range(count))):
    #             if sum(nums[i:count]) >= s and rs > (count-i):
    #                 rs = count - i
    #                 break
    #     return rs
    
    # O(n) smart solution
    def minSubArrayLen(self, s, nums):
        total = left = 0
        result = len(nums) + 1
        for right, n in enumerate(nums):
            total += n
            while total >= s:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        return result if result <= len(nums) else 0
~~~
## Test Cases
~~~
1. [1,2,3,4,5], 5 -> 1
2. [1,2,3,4], 5 -> 2
3. [50,50,3,1,1,1,100], 103 -> 3
4. [1],1 ->1 
~~~
