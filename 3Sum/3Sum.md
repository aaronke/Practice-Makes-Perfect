# [3Sum](https://leetcode.com/problems/3sum/)

## Description
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.

~~~
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
~~~
## Analysis
### Clarifications
1. If there is no result, should I return a empty list?
2. Is there any requirement for complexity?

### Methods
**Method 1 naive method:** I can think of three level of recursions. Once find three number's sum are 0 and then sort them. If the sorted list is not existing in result list, append it to result list. But this method gets time exceed limit error.

**Method 2 Two pointers method:** Basically, divide the issue as n twosum issues and then solve it by two pointers for each twosum.

* Time Complexity: `O(n^2)`
* Space Complexity: `O(n)`

## Python Code
~~~
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    # Naive method -- O(n^3) solutions
    #     rs = []
    #     self.searchRs(rs, 0, [], nums)
    #     return rs
    
    # def searchRs(self, rs, level, oneRs, nums):
    #     if level == 3:
    #         if sum(oneRs) == 0:
    #             oneRs.sort()
    #             if oneRs not in rs:
    #                 rs.append(oneRs)
    #         return

    #     for i in range(len(nums)):
    #         newOneRs = oneRs + [nums[i]]
    #         self.searchRs(rs, level+1, newOneRs, (nums[:i] + nums[i+1:]))
    
        nums.sort()
        target = 0
        rs = []
        newTargetList = []
        for i in range(len(nums)):
            newTarget = target - nums[i]
            if newTarget in newTargetList:
                continue
            else:
                newTargetList.append(newTarget)
            twoRs = self.twoSum(newTarget, nums[:i]+nums[i+1:])
            for row in twoRs:
                row = row + [nums[i]]
                row.sort()
                if row not in rs:
                    rs.append(row)
        return rs
    
    def twoSum(self, target, nums):
        l = len(nums)
        rs = []
        if l < 2:
            return []
        
        start = 0
        end = l-1
        while start < end:
            numsSum = nums[start] + nums[end]
            if numsSum == target:
                oneRs = [nums[start], nums[end]]
                if oneRs not in rs:
                    rs.append(oneRs)
                start += 1
                end -= 1
            elif numsSum > target:
                end -= 1
            else:
                start += 1
        
        return rs
~~~
## Test Cases
~~~
1. [1,-2,1] -> [[1,1,-2]]
2. [-1 0 1 2 -1 -4] -> [[-1, 0, 1],[-1, -1, 2]]
~~~