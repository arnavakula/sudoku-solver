example_board = [[0, 0, 0, 0, 0, 1, 0, 9, 0], [0, 2, 4, 3, 6, 0, 0, 0, 0], [6, 1, 0, 0, 0, 0, 4, 0, 0], [8, 6, 0, 5, 9, 3, 7, 0, 4], [2, 7, 9, 6, 0, 4, 5, 0, 1], [0, 0, 3, 0, 0, 0, 9, 0, 8], [7, 0, 0, 9, 1, 0, 0, 4, 0], [0, 0, 2, 0, 0, 0, 6, 0, 0], [0, 0, 0, 8, 0, 6, 3, 7, 0]]

def solve(board):
    #try to find empty slot
    try:
        i, j = find_empty_slot(board)
    #if no empty slots, comp has found a solution
    except:
        return board
    
    #find valid value for selected slot
    for num in range(1, 10):
        if is_valid_move(board, i, j, num) == True:
            board[i][j] = num

            #if we can find a solution for the next square, continue
            if solve(board):
                return True
            #if there is no solution, change solution for previous slot
            else:
                board[i][j] = 0
        
    return False

def find_empty_slot(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    
    return False

def is_valid_move(board, i, j, num):
    #check col
    for row in board:
        if num == row[j]:
            return False
    
    #check row
    if num in board[i]:
        return False

    #check box
    for row in range(3 * int(i/3), 3 * int(i/3) + 3):
        for col in range(3 * int(j/3), 3 * int(j/3) + 3):
            if board[row][col] == num:
                return False

    return True

def main(board):
    solve(board)

    for row in board:
        print(row)
        
main(example_board)


#PSUEDOCODE
#recursion until there are no empty slots
    #find open space
    #put in number
    #test if next square can have a solution
        #if not, put new number for previous spot

