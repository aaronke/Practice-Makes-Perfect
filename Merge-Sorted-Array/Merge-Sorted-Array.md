# [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

## Description
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

**Note:** You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
## Analysis
### Clarifications
1. The length of nums1 is larger or equal to (m+n), correct?
2. Can I use extra space (O(n))?
3. Both of the lists are non-descending order, correct?

### Method
**Naive Method**
Basically, the solution below is to store the merged list into a new array. And when the merging finishes, then assign the array to `nums1` respectively.

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

**Method with constant space**
Basically, it takes advantage of the storage of longer storage. And put the higher value to the last n elements!!Deserve to make antoher try!!

* Time Complexity: `O(n)`
* Space Complexity: `O(1)`

## Python Code
~~~
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # Naive Way to do it!!
        # tempNum = []
        
        # update1 = True
        # update2 = True
        # count1 = 0
        # count2 = 0
        # while (count1 < m) and (count2 < n):
        #     if (count1 < m) and update1: 
        #         num1 = nums1[count1]
        #     if (count2 < n) and update2: 
        #         num2 = nums2[count2]
        #     if num1 < num2:
        #         tempNum.append(num1)
        #         update1 = True
        #         update2 = False 
        #         count1 += 1
        #     else:
        #         tempNum.append(num2)
        #         update1 = False
        #         update2 = True
        #         count2 += 1
        # while (count1 < m):
        #     tempNum.append(nums1[count1])
        #     count1 += 1
        # while (count2 < n):
        #     tempNum.append(nums2[count2])
        #     count2 += 1
        
        # for i in range(len(tempNum)):
        #     nums1[i] = tempNum[i]
        
        # Smarter Way to do it!!
        end = m+n-1
        num1Index = m-1
        num2Index = n-1
        
        while (num2Index >= 0) :
            if num1Index < 0 or nums1[num1Index] < nums2[num2Index]:
                nums1[end] = nums2[num2Index]
                num2Index -= 1 
                end -= 1
            else:
                nums1[end] = nums1[num1Index]
                num1Index -= 1
                end -= 1
~~~

## Test Cases
~~~
1. [1,2,3], 1
   [4, 5],1
              -> [1,4,3]
2. [1,10,11], 2 
   [0,2], 2
              -> [0,1,2,10]
3. [1,3,5],2
   [0]
   				 -> [0,1,3]
4. [0], 0
   [1], [1]  
              -> [1] 
~~~