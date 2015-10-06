# [Game of Life](https://leetcode.com/problems/game-of-life/)

## Description
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population..
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state.

**Follow up:**   

1. Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.

2. In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
## Analysis

**Method 1**-- Use new array to get result and then assign new array to old board. There are two ways to count the live cells. One way is to count 8 manully and other way is to use two simple for loops to do that.

* Time Complexity: `O(mn)`
* Space Complexity: `O(mn)`

**Method 2**-- Since the data type of element is int, so it can be used more than 2 status. Especially, the bit manipulation could allow us to think the second digit is the next status and the first one is current status. So it allows us to use constant space.

* Time Complexity: `O(mn)`
* Space Complexity: `O(1)`

## Notes
If you have a line of code -- `board[i][j] = board[i][j]<< 1 + 1`. When `board[i][j] = 1`, what's the result? It's not 3, but 4. Because the priority of plus(`+`) is larger than `<<`. Be really careful in the future!

## Python Code

~~~
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # Method 3 -- Use bit manipulation
        h = len(board)
        w = len(board[0])
        
        for i in range(h):
            for j in range(w):
                count = self.getCount(board, i, j)
                if count == 3 and not board[i][j] & 1:
                    board[i][j] = 2
                elif (count < 2 or count > 3) and board[i][j] & 1:
                    board[i][j] = 1
                elif (count == 2 or count == 3) and board[i][j] & 1:
                    board[i][j] = 3

        for i in range(h):
            for j in range(w):
                 board[i][j] = board[i][j] >> 1
                
    def getCount(self, board, h, w):
        count = 0
        for i in range(max(h-1,0), min(h+2,len(board))):
            for j in range(max(w-1, 0), min(w+2, len(board[0]))):
                if (i != h or j != w) and (board[i][j] & 1):
                    count += 1
                    
        return count        
        
        # Method 3 -- Use another new board to get new status
        # newBoard = []
        # for row in board:
        #     newRow = []
        #     for j in row:
        #         newRow.append(j)
        #     newBoard.append(newRow)
        
    #     for h in range(len(board)):
    #         for w in range(len(board[0])):
    #             count = self.countLive(board, h, w)
    #             if count < 2 or count > 3:
    #                 if board[h][w] == 1:
    #                     board[h][w] = 4
    #                 else:
    #                     board[h][w] == 0
    #             elif count == 3 :
    #                 if board[h][w] == 0:
    #                     board[h][w] = 3
    #                 else:
    #                     board[h][w] = 1
    #     for h in range(len(board)):
    #         for w in range(len(board[0])):
    #             if board[h][w] == 4:
    #                 board[h][w] = 0
    #             elif board[h][w] == 3:
    #                 board[h][w] = 1

    
    # def countLive(self, board, x,y):
    
    # Method 1 -- use for loop to search 8 cases
    #     count = 0
    #     w = len(board[0])
    #     h = len(board)
    #     var = [0, 1, -1]
    #     for i in var:
    #         for j in var:
    #             if x+i >= 0 and y+j >= 0  and x+i<h and y+j<w and (board[x+i][y+j] == 1 or board[x+i][y+j] == 4):
    #                 count += 1
    #     if board[x][y] == 1:
    #         count -= 1
    #     return count
        
        # Method 2 -- manully search 8 cases
        # if x+1<h and y+1<w and (board[x+1][y+1] == 1 or board[x+1][y+1] == 4):
        #     count += 1
        # if x+1<h and (board[x+1][y] == 1 or board[x+1][y] == 4):
        #     count += 1
        # if y+1<w  and (board[x][y+1] == 1 or board[x][y+1] == 4):
        #     count += 1
        # if x-1>=0 and y-1>=0 and (board[x-1][y-1] == 1 or board[x-1][y-1] == 4):
        #     count += 1
        # if y-1>=0 and (board[x][y-1] == 1 or board[x][y-1] == 4):
        #     count += 1
        # if x-1>=0 and (board[x-1][y] == 1 or board[x-1][y] == 4):
        #     count += 1
        # if x-1>=0 and y+1<w and  (board[x-1][y+1] == 1 or board[x-1][y+1] == 4):
        #     count += 1
        # if x+1<h and y-1>=0 and (board[x+1][y-1] == 1 or board[x+1][y-1] == 4):
        #     count += 1
        
        # return count
~~~
## Test Cases
~~~
1. [[1,0], [1,1]] -> [[1,1],[1,1]]
2. [[1]] -> [[1]]
~~~
