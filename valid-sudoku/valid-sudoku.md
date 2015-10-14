# [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

## Description
Determine if a Sudoku is valid, according to: Sudoku Puzzles - [The Rules](http://sudoku.com.au/TheRules.aspx).

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
A partially filled sudoku which is valid.

Note: A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

## Analysis
Method 1 -- Navie: The naive method is to check three types (columns, cells, rows) repectively. 

Method 2 -- Check once: Go through the sudoku array once and check three types at the same time. But it needs to add variable to store the status of checking.

Method 1 and 2 are a very common trade-off between space and time.

## Python Code
~~~python
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Method 1 -- Check three modal
        # if len(board) != 9:
        #     return False
        # numbers = '123456789.'
        
        # # Check row
        # for row in board:
        #     arrayHash = [False] * 9
        #     if len(row) != 9:
        #         return False
        #     for l in row:
        #         indexL = numbers.index(l)
        #         if indexL == 9:
        #             continue
        #         if  (not arrayHash[indexL]):
        #             arrayHash[indexL] =  True
        #         else:
        #             return False
        # # Check column             
        # for column in range(0, 9):
        #     arrayHash = [False] * 9
        #     for row in board:
        #         indexL = numbers.index(row[column])
        #         if indexL == 9:
        #             continue
        #         if (not arrayHash[indexL]):
        #             arrayHash[indexL] =  True
        #         else:
        #             return False
        # # Check box
        # boxID = [[0, 0], [0, 3], [3, 0], [3, 3], [0, 6], [6, 0], [3, 6], [6, 3], [6, 6]]
        # for box in boxID:
        #     arrayHash = [False] * 9
        #     for row in range(0,3):
        #         for column in range(0,3):
        #             indexL = numbers.index(board[row + box[0]][column + box[1]])
        #             if indexL == 9:
        #                 continue
                    
        #             if (not arrayHash[indexL]):
        #               arrayHash[indexL] =  True
        #             else:
        #                 return False
        # return True
        
        # Method 2 -- Check once for all
        cells =[]
        rows = []
        columns = []
        for i in range(0,9):
            cells.append([False]*9)
            rows.append([False]*9)
            columns.append([False]*9)
        
        if len(board) != 9:
            return False
        numbers = '123456789.'
        for row in range(0,9):
            if len(board[row]) != 9:
                return False
            for column in range(0, 9):
                indexL = numbers.index(board[row][column])
                if indexL != 9:
                    if (cells[(row/3) + (column/3)*3][indexL]) or rows[row][indexL] or columns[column][indexL]:
                        return False
                    if not (cells[(row/3) + (column/3)*3][indexL]):
                        cells[(row/3) + (column/3)*3][indexL] = True
                    if not rows[row][indexL]:
                        rows[row][indexL] = True
                    if not columns[column][indexL]:
                        columns[column][indexL] = True
        
        return True
~~~

## Notes
1. Mistake about initialize 2-D array in Python  
`cells = [[False]*9]*9` 9 sub-arrays share the same reference, in another words, they are the same. See example below.

~~~python
# Wrong practice!! --  a = [[False]*1]*2  => [[False], [False]] =>
#                      a[1] = True
#                      Result: a => [[True], [True]] , NOT : [[False], [True]]
#                      Result-- The second * gives your same reference!!
# cells = [[False]*9]*9
# rows = [[False]*9]*9
# columns = [[False]*9]*9

# Correct practice!!
cells =[]
rows = []
columns = []
for i in range(0,9):
    cells.append([False]*9)
    rows.append([False]*9)
    columns.append([False]*9)
~~~        

# another way to initialize 2D array
cells = [[False]*9 for i in range(9)]
rows = [[False]*9 for i in range(9)]
columns = [[False]*9 for i in range(9)]

The place that I debugged my code and found the cause is called [Python Tutor](http://www.pythontutor.com/visualize.html#mode=edit). It can visualize the execution of python program and see the allocation of memory. It's powerful! Not only good for small program debugging, but also great for learning purpose.
