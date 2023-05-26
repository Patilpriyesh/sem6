global N
N = 4


def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end= " ")
        print()


def isSafe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
        
    # check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
        
    # check for lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
        
    return True


def solveNQUntil(board, col):
    if col >= N:
        return True
    
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQUntil(board, col + 1) == True:
                return True
            board[i][col] = 0
    return False



def solveNQ():
    board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

    if solveNQUntil(board, 0) == False:
        print("Print Solution does not Exists")
        return False
    
    printSolution(board)
    return True

solveNQ()