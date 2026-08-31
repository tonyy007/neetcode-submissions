class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = [set() for i in range(9)]
        rows = [set() for i in range(9)]
        columns =[set() for i in range(9)]
        # rows[0].add(3)
        # print(rows)

        for i in range(0, 9):
            for j in range(0,9):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j])
                if num in rows[i] or num in columns[j]:
                    return False

                rows[i].add(int(board[i][j]))
                columns[j].add(int(board[i][j]))
                if i < 3:
                    if j < 3:
                        if num in squares[0]:
                            return False
                        squares[0].add(int(board[i][j]))
                    elif j>=3 and j<6:
                        if num in squares[1]:
                            return False
                        squares[1].add(int(board[i][j]))
                    else:
                        if num in squares[2]:
                            return False
                        squares[2].add(int(board[i][j]))
                elif i >= 3 and i < 6:
                    if j < 3:
                        if num in squares[3]:
                            return False
                        squares[3].add(int(board[i][j]))
                    elif j>=3 and j<6:
                        if num in squares[4]:
                            return False
                        squares[4].add(int(board[i][j]))
                    else:
                        if num in squares[5]:
                            return False
                        squares[5].add(int(board[i][j]))
                else:
                    if j < 3:
                        if num in squares[6]:
                            return False
                        squares[6].add(int(board[i][j]))
                    elif j>=3 and j<6:
                        if num in squares[7]:
                            return False
                        squares[7].add(int(board[i][j]))
                    else:
                        if num in squares[8]:
                            return False
                        squares[8].add(int(board[i][j]))

        return True