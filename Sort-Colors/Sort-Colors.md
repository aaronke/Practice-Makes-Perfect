# [Sort Colors](https://leetcode.com/problems/sort-colors/)

## Description
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.
## Analysis
Be careful to understand the question. We can only change the number list in place.

**Method 1** Two Passes -- bucket sorting. As for the first pass, we create 3 variables to store the numbers of values for 1, 2, 3. Then assign it by another pass. Therefore, if we come across 0 or 2, we just put the value under the index and update the index. But still remeber to move the original value to safe place.

`[A] + [B] + [C]`

`A` is place to store `0`, `C` is the place to store `2`. So the while loop can only check the B part(unclear part that can be `0,1,2`.

Another thing is that when updating part `C`, we don't need to update `start`(`A`'s ending index). Because the value under that index will be changed and need to be checked again!! Very easy to make mistake! Be careful! 

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

**Method 2** One pass -- Tricks -- Imagin there are two indexes(one is ending index for 0, anther one is the starting index for 2). Therefore, 


## Test Cases
 Test Input -> Expected Output

1. [1] -> [1]
2. [2,0] -> [0,2]
2. [0,1,2] -> [0,1,2]
3. [] -> []
4. [2,1,2,1,0] -> [0,1,1,2,2]

## Python Code
~~~
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # red, white, blue = 0, 0, 0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         red += 1 
        #     elif nums[i] == 1:
        #         white += 1
        #     elif nums[i] == 2:
        #         blue += 1
        # for h in range(red):
        #     nums[h] = 0
        # for j in range(red, red + white):
        #     nums[j] = 1
        # for k in range(red + white, red + white + blue):
        #     nums[k] = 2
        
        zero = 0
        two = len(nums) - 1
        start = 0
        while start <= two:
            if nums[start] == 0:
                nums[start] = nums[zero]
                nums[zero] = 0
                zero += 1
            if nums[start] == 2:
                nums[start] = nums[two]
                nums[two] = 2
                two -= 1
                start -= 1 
            start += 1      
~~~