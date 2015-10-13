# [Nim Game](https://leetcode.com/problems/nim-game/)

## Description
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.

## Analysis
### Clarifications
1. What do you mean by optimal strategies? Know the result for every interger!
2. What should I return when n is 0? 0

### Method
At the beginning, I don't realize the issue can be just solved by mode. Firstly, I would use some cases, for example when n is 4,5,6,7. And gradually, I realized that every result is determined by the previous 3 values. And only when all 3 status are true, the current postion should be false.

At the beginning, I would think about recursion, but obviously, it costs too much. Instead, I apply array to store the status. However, when n is 200000, the array still costs too much. Therefore, mode comes in!! By using mode, all the complexity would be constant!

* Time Complexity: `O(1)`
* Space Complexity: `O(1)`

## Python Code
~~~
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        rs = n%4
        if rs == 0:
            return False
        return True
        
        # Method 1
        # if n <= 3:
        #     return True
            
        # rs = [False] * n
        # rs[0] = True
        # rs[1] = True
        # rs[2] = True
        
        # cur = 3
        # while cur < n:
        #     if  rs[cur-3] and  rs[cur-2] and  rs[cur-1]:
        #         rs[cur] = False
        #     else:
        #         rs[cur] = True
        #     cur += 1
                
        # return rs[-1]
~~~
