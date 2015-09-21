# [Combination Sum](https://leetcode.com/problems/combination-sum/)

## Description
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

**Note:** All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).

The solution set must not contain duplicate combinations.  
For example, given candidate set `2,3,6,7` and target `7`,   
A solution set is:   
`[7]`   
`[2, 2, 3]` 
## Analysis
### Clarifications
1. if T = 5, [2,3] and [3,2] would be the same result. Because [3,2] will be converted tinto [2,3] finally, correct?

### Method - Dynamic Programming
So basically, Basically, the idea is `T(n) = T(n-1) + 1`. We assume that a number is on the list and then convert the issue into a new target number with the same condidate numbers. But still, there are a lot of traps!!

1. It requires each solution should show it as non-decending order. Therefore, once one solution is found, please sorting. You can also sort and get rid of duplicates after we get all the possible solutions. However, it would be saving a lot of time if sorting and deleting duplicates at the first. 

2. Deep copy on array. In the solution code below, `oneRs` should be copy deeply. Otherwise, multiple solutions will be mixed!! Remeber the value of `oneRs` is the reference of that array.

3. Another lesson I learn is that when using for loop, please never use a name for multiple times. For example, `i`, if in anther loop, please use `j`. Or just replace with a more meaningful name!! In this solution, at the beginning, I used `i` for two times and got a weird bug. Because two `i`s are influenced each other.

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

Is the complexity analysis above correct? Recursion makes it take deeper and each time it will create a result array.If we think that array is constant, then the space complexity is `O(n)`, otherwise, it will be `O(n^2)`.

## Python Code
~~~
class Solution(object):
    # rs = []
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        rs = []
        oneRs = []
        self.getCombination(rs, candidates, target, oneRs)
        return rs
    def getCombination(self, rs, candidates, target, oneRs):
        if target == 0 and oneRs:
            oneRs.sort()
            if oneRs not in rs:
                rs.append(oneRs)
        for i in range(len(candidates)):
            newOneRs = []
            for j in oneRs:
                newOneRs.append(j)
            if target >= candidates[i]:
                newOneRs.append(candidates[i])
                self.getCombination(rs, candidates[i:], target-candidates[i], newOneRs)
~~~
## Test cases
~~~
1. [2],4 -> [[2,2]]
2. [2],2 -> [[2]]
3. [2,3], 5 -> [[2,3]]
4. [2,3,7], 7 -> [[2,2,3],[7]]
~~~
