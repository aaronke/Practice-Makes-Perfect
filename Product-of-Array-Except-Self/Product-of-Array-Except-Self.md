# [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

## Description
Given an array of n integers where n > 1, `nums`, return an array output such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

Solve it **without division** and in O(n).

For example, given `[1,2,3,4]`, return `[24,12,8,6]`.

**Follow up:** Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
## Analysis
### Clarifications
1. What do you mean by "without division"?
2. What happen if there is zero in the array List? All the rest will be zero?
3. What's the return value when input is `[1]`?

### Method
Consider about the issue, it only depends on the rest of elements. So when it comes to product, there are situations.

1. No zero, apply normal method, get overall product and divide with element A when it comes to its new value.
2. One Zero, only the one with zero has non-zero value.
3.  Two or more zeros, all the elements will be zero.  

* Time Complexity: `O(n)`
* Space Complexity: `O(1)`

##Note
1. Please never make mistake like use `==` to assign value!! It will has no effects!!

## Python Code
~~~
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numZeros = 0
        numProducts = 0
        for i in nums:
            if i == 0:
                numZeros += 1
            else:
                if numProducts == 0:
                    numProducts = i
                else:
                    numProducts *= i
        # three Cases
        if numZeros > 1:
            for i in range(len(nums)):
                nums[i] = 0
                
        if numZeros == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = numProducts
                else:
                    nums[i] = 0
        if numZeros == 0:
            for i in range(len(nums)):
                nums[i] = numProducts/nums[i]
        
        return nums
~~~

## Test Cases
~~~
1. [1,2] -> [2,1]
2. [2,3,4,5] -> [60, 40, 30, 24]
3. [0, 1,2,3] -> [6, 0, 0, 0]
4. [0,1,0,2,3] -> [0, 0, 0, 0]
~~~
