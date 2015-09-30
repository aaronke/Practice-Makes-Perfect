# [Subsets II](https://leetcode.com/problems/subsets-ii/)

## Description
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,2], a solution is:
## Analysis
The only difference between another issue -- [Next Permutation](https://github.com/haoyuchen1992/Practice-Makes-Perfect/blob/master/Next-Permutation/Next-Permutation.md) is that for this one, it allows duplicated numbers. This different will add duplicate checking when adding results. But beside that, all the things are the same. I implemented exist two methods with the same idea from Next Permutation.

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

## Python Code
~~~
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    # Search in Deepth
    #     rs = [[]]
    #     oneRs = []
    #     self.subSets(oneRs, rs, nums)
    #     return rs
        
    # def subSets(self,oneRs, rs, nums):
    #     l = len(nums)
    #     if l == 0:
    #         return
        
    #     for i in range(l):
    #         newRs = oneRs + [nums[i]]
    #         newRs.sort()
    #         if newRs not in rs:
    #             rs.append(newRs)
    #             self.subSets(newRs, rs, (nums[:i] + nums[i+1:]))
    
        l = len(nums)
        numsRs = 1 << l
        rs = []
        stepMove = range(l)
    
        for i in range(numsRs):
            oneRs = []
            for j in stepMove:
                if (1 << j) & i:
                    oneRs.append(nums[j])
            oneRs.sort()
            if oneRs not in rs:
                rs.append(oneRs)
    
        return rs
~~~
## Test Cases
~~~
1. [1] -> [[], [1]]
2. [] -> [[]]
3. [1,2,3] -> [[3], [1], [2], [1,2,3], [1,3],[2,3], [1,2],[]]
4. [1,2,2] -> [[1], [2], [1,2,2], [1,2],[2,2], []]
~~~