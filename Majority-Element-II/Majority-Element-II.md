# [Majority Element II](https://leetcode.com/problems/majority-element-ii/)

## Description
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

## Analysis
**Method 1 -- HashTable**  
Firstly, get the hashtable represenation of the array. And then if the key's value(frequencey) is larger than the limit and not shown in existing results.Then add it into result list.

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

**Method 2 -- Sorting**
Sort the number list firstly, and then if there is a interval that contains the same value but whose length is larger than the limit, then add it into results. 

* Time Complexity: `O(nlogn)`
* Space Complexity: `O(1)`

**Method 3 -- To be updated -- Boyer-Moore Majority Vote algorithm**   

https://leetcode.com/discuss/43248/boyer-moore-majority-vote-algorithm-and-my-elaboration

* Time Complexity: `O(n)`
* Space Complexity: `O(1)`
## Python Code
~~~
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # O(n) time and space -- remember to check if one result exists or not
        # hashMap = {}
        
        # for i in nums:
        #     if i not in hashMap:
        #         hashMap[i] = 1
        #     else:
        #         hashMap[i] += 1
        
        # limit = len(nums)/3
        # rs = []
        # for key, val in hashMap.iteritems():
        #     if val > limit and (key not in rs):
        #         rs.append(key)
        
        # return rs
        
        # O(nlogn)time  O(1) space
        nums.sort()
        l = len(nums)
        if l == 0:
            return []
        cur = 0
        start = 0
        end = 0
        preVal = nums[0]
        limit = l/3
        rs = []
        while cur < l:
            if nums[cur] == preVal:
                end = cur
            else:
                start = cur
                end = cur
            if (end - start + 1) > limit and (nums[cur] not in rs):
                rs.append(nums[cur])
            preVal = nums[cur]
            cur += 1
        
        return rs
~~~
## Test Cases
~~~
1. [1] -> [1]
2. [] -> []
3. [1, 2] -> [1,2]
4. [1,1,2] -> [1]
5. [1,1,2,2,3] -> [1,2]
6. [1,2,3,4,5] -> []
7. [1,2,3,4,4] -> [4]
~~~
