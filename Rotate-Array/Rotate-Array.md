# [Rotate Array](https://leetcode.com/problems/rotate-array/)

## Description
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

## Analysis
### Clarifications
1. How do I deal with the k when it is larger than the length of array? Use Mode!

### Method
Firstly, we can use extra array to sway the content. ANd we can also move the array content to the right side one by one.But all those two methods is not the optimal -- O(n) time, O(1) space.

Therefore, there is easy trick to do it. So first reverse the whole array and then reverse two partial array. The final result is what we want. Since the reverse is kind of the same, so we can define it as function and use three times.

* Time Complexity: `O(n)`
* Space Complexity: `O(1)`

## Python Code
~~~
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        self.reverseSub(nums, 0, l-1)
        self.reverseSub(nums, 0, k-1)
        self.reverseSub(nums, k, l-1)
        
        
    def reverseSub(self,nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
~~~

## Test Cases
~~~
[1,2,3,4,5,6,7], 12  = [1,2,3,4,5,6,7], 5 
						 => return [3,4,5,6,7,1,2]
[1,2,3,4,5,6,7], 3   => return [5, 6, 7, 1, 2, 3, 4]
~~~