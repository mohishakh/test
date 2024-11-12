board=[["x","o","x"],['x','o','o'],['o','o','x']]
def check_winer(board):
    for x in board:
        if x[0]==x[1]==x[2] and x!="":
            return (x[0],"winner")
    for y in range(3):
        if board[0][y]==board[1][y]==board[2][y] and board[0][y]!="":
            return(board[0][y],"winner")
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]!="":
        return(board[0][0],"winner")
    if board[0][2]==board[1][1]==board[2][0] and board[0][0]!="":
        return(board[0][2],"winner")
print(check_winer(board))