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


s = Solution()
input = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
print s.isValidSudoku(input)
        
        
                    
            
        
        
        