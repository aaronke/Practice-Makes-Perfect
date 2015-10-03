# [Word Search](https://leetcode.com/problems/word-search/)

## Description
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

~~~
[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
~~~
word = `"ABCCED"`, -> returns `true`,  
word = `"SEE"`, -> returns `true`,   
word = `"ABCB"`, -> returns `false`.  
## Analysis
### Clarifications
1. what if the input are a empty list and emtpy string, should I return `True`?

### Method
Use Recursion to solve the issue. The key part is understand how to find the correct recursion, when we return false and when we return ture. Really be careful!! Especailly, when you need to input a reference(2D array). Change the value first and revert it back when do another same level recursion.

* Time Complexity: `O(K*n)` -- `K` is the length of word
* Space Complexity: `O(n)`-- If considering about recursion storage comsumption

## Python Code

~~~
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        h = len(board)
        w = len(board[0])
        for i in range(h):
            for j in range(w):
                if self.existValue(i, j, word, board, 0):
                    return True
        return False
                    
    def existValue(self,h, w, word, board, level):
        lh = len(board)
        lw = len(board[0])
        if level == len(word):
            return True
        if(h >lh-1 or h <0 or w<0 or w >lw-1 or board[h][w]!=word[level]):
            return False
        
        newStr = []
        for i in range(lw):
            if i != w:
                newStr.append(board[h][i])
            else:
                newStr.append('*')
        newStr = "".join(newStr)
        tempStr = board[h]
        board[h] = newStr

        result = self.existValue(h-1, w, word, board, level+1) or self.existValue(h, w-1, word, board, level+1) or self.existValue(h+1, w, word, board, level+1) or self.existValue(h, w+1, word, board, level+1)
        
        board[h] = tempStr
        return result
~~~

## Test Cases
~~~
1. ["aa"], "aaa" -> False
2. ["aa"]. "a" -> True
3. ["ABCE", "SFCS", "ADEE"], "SEE" -> True
~~~