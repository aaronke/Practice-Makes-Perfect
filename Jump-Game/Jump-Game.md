# [Jump Game](https://leetcode.com/problems/jump-game/)

## Description
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = `[2,3,1,1,4]`, return `true`.

A = `[3,2,1,0,4]`, return `false`.
## Analysis
### Clarifications
1. Is the list sorted? NO
2. For non-negative number, so there is 0, correct? So once dropping on zero and the index is not the last one, it will return false, correct?
3. Your maximum jump length at that position means the number of jump could below one number.

### Methods
It is really easy to misunderstand the issue!! When nums[i] is 2, it means that when jumping to index i, you can jump `0,1,2` distances, not just `2`.

After knowing the issues, the first naive way is to based on the concept and find all the possible path, see whether the last index is reachable. It can be implementd as recursion or DFS. However, both of them are too much! I got either `Time Exceed Limit`, `Memory Exceed Limit`, or `Too Deep Recursion`.

Therefore, consider the dicussion on [LeetCode](https://leetcode.com/discuss/41420/1-6-lines-o-n-time-o-1-space), it has two simple methods!!

**Method 1:** First one is forward checking. When it is reachable one index, it will update the remotest index that can be reached at that point. If the remostest index is alwasy ahead of current index, it will return `True`.

**Method 2:** Another way is to backward checking. With similar data structure, starting from the end of list (set it as current index at the begnning), and then check if the adjacent left index can be lead to the current index. If yes, update current index.  If not, check lefter one.  In then end, if the current index is the first index and its value is not `0`, then return True. However, remember there is a special case -- `[0]`, then the value is `0`, but based on the length, still return `True`.

Both back and forward checking cost linear time and space is constant.

* Time Complexity: `O(n)`
* Space Complexity: `O(1)`

## Notes
1. when use `while` loop, really think about the edge cases and check if it is what you want. For example, in backward checking method, Original I had code below:

~~~
        while 0 <= count:
            count -= 1
~~~

But I made mistake here, because at last, count = -1. However it should be 1.The correct one should delete equal sign.

~~~
        while 0 < count:
            count -= 1
~~~


2. The reason why naive method can't pass the test and get errors about memory and storage limit is because I used range and recursion. When I can only deal with one element at a time in one level of recursion, never do it!! Another thing is that when your input could be `900000`, never use `range(900000)`. It should not be used in that way! There must be other way to avoid using it.

## Test Cases
~~~
1. [0,1] -> False
2. [0] -> True
3. [2,1,0,0] -> False
4. [2,5,0,0] -> True 
~~~

## Python Code
~~~
class Solution(object):
    
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # Feasible method 1 -- Forward Version
        # m = 0
        # for i, n in enumerate(nums):
        #     if i > m:
        #         return False
        #     m = max(m, i+n)
        # return True
        
        # Feasible method 2 -- Backward Version
        m = len(nums)
        cur = m - 1
        count = m - 1
        # Make a mistake here -- add 0 <= count, but count can never be -1! so think about the last momment!!
        while 0 < count:
            count -= 1
            if nums[count] >= (cur-count):
                cur = count
        if nums[0]>0 and cur <= 0:
            return True
        elif nums[0] == 0 and m == 1:
            return True
        return False        
        
        
        
        
        # Stupid idea with too many recursions!!
        # lenNums = len(nums)
        # if lenNums == 0:
        #     return False
        # if lenNums == 1:
        #     return True
        # if nums[0] >= lenNums-1:
        #     return True
        
        # for i in range(nums[0]):
        #     if self.canJump(nums[i:]):
        #         return True
                
        # return False
        
        
        # Memoery Exceed Example!!! -- Be carefull to use range for the input variable. Since input could be very big, it costs too much storage
    #     if len(nums) <= 0:
    #         return False
    #     if (len(nums)-1) == 1:
    #         return True
    #     return self.getLevel(0, nums, len(nums)-1)
        
    # def getLevel(self,level, nums, target):
    #     if nums[level] + level >= target and target >= level:
    #         return True
    #     testRange = min(nums[level],target-level)
    #     rs = [False]*testRange
    #     for i in range(1, testRange):
    #         if not rs[i] and self.getLevel(level+i, nums, target):
    #             return True
    #         rs[i] = True
                
    #     return False
    
        # lenNums = len(nums)
        # cur = 0
        # most = 1
        # while most < lenNums:
        #     if cur < most:
        #         temp = most + nums[cur]
        #         if most < temp:
        #             most = temp
        #             cur = cur + 1
        #         else:
        #             return False
        #     else:
        #         return False
        # return True
        
        # Time Limit Exceeded !!!
        # rs = [0]
        # level = 0 
        # target = len(nums) - 1
        # status = [False]*(target+1)
        # while rs:
        #     newRs = []
        #     for oneRs in rs:
        #         for i in range(1, nums[oneRs]+1):
        #             if i+level >= target:
        #                 return True
        #             elif (i+level) not in newRs and not status[i+level]:
        #                 newRs.append(i+level)
        #                 status[i+level] = True
        #     rs = newRs
        #     level += 1
        # return False
~~~