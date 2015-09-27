# [Next Permutation](https://leetcode.com/problems/next-permutation/)

## Description
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.  
`1,2,3` → `1,3,2`  
`3,2,1` → `1,2,3`  
`1,1,5` → `1,5,1`  
## Analysis
### Clarifications
1. Is the input array sorted? No!

### Methods
**Method 1 Naive DFS:** 
So basically, use DFS and recursion to get the result. If one is not in result list, then added it.

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

Code Practice Notes:

~~~
## Good
if oneRs not in rs:
	rs.append(oneRs)
	self.sub(rs, oneRs, 
~~~
Why the below is bad? Because we don't want to calculated same sing multiple times!!

~~~
## Bad
if oneRs not in rs:
	rs.append(oneRs)
self.sub(rs, oneRs, 
~~~
**Method 2 Bit Manipulation:** So basically, think about use binary bit to know if the subset contains one index or not. Because if there are 3 elements in input list, there are 8 subsets (`2^3`). So it converts the issue into bint manipulation issue.  

* Time Complexity: `O(n)`
* Space Complexity: `O(1)`

So remeber to sort at the beginning and then you can return the sorted subset by adding them sequenctly.


## Python Code
~~~
import operator
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    #     rs = [[]]
    #     if len(nums) == 0:
    #         return rs
    #     self.sub(rs, [], nums)
    #     return rs
        
    # def sub(self, rs, curSub, curNums):
    #     l = len(curNums)
    #     if l == 0:
    #         return
    #     for i in range(l):
    #         oneRs = curSub + [curNums[i]]
    #         oneRs.sort()
    #         if oneRs not in rs:
    #             rs.append(oneRs)
    #             # Position Matters!!
    #             self.sub(rs, oneRs, (curNums[:i]+curNums[i+1:]))
        l = len(nums)
        nums.sort()
        numSets = 1 << l
        rs = []
        for i in range(numSets):
            oneRs = []
            v = 1<<(l-1) 
            for j in range(l):
                if  i & v:
                    oneRs.append(nums[j])
                v = v>>1
            rs.append(oneRs)
        
        return rs
~~~
## Test Cases
1. [] -> [[]]
2. [1] ->[[], [1]]
3. [1,2] -> [[], [1], [2], [1,2]]
4. [1,3,2] ->[[3], [1], [2], [1,2,3], [1,3],[2,3], [1,2],[]]