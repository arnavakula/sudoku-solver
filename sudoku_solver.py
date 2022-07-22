import time
from bs4 import BeautifulSoup
import requests
import json
import re

example_board = [[0, 6, 4, 8, 7, 0, 0, 0, 9], [0, 0, 3, 9, 0, 0, 2, 5, 0], [0, 0, 7, 3, 0, 2, 0, 0, 4], [0, 0, 2, 0, 5, 4, 0, 9, 0], [9, 0, 0, 0, 0, 0, 0, 0, 6], [0, 3, 0, 6, 9, 0, 1, 0, 0], [3, 0, 0, 4, 0, 8, 9, 0, 0], [0, 2, 9, 0, 0, 1, 4, 0, 0], [8, 0, 0, 0, 3, 9, 5, 6, 0]]
def enter_nums(board):
    for i in range(0, 9):
        for j in range(0, 9):
            board[i][j] = int(input("enter:"))
    
    print(board)

def scrape_puzzle(mode):
    url = 'https://www.nytimes.com/puzzles/sudoku/{}'.format(mode)
    soup = BeautifulSoup(requests.get(url).content,"html.parser")

    data = json.loads(re.sub('window.gameData = ', '', soup.find('script').contents[0]))

    puzzle = data[mode]['puzzle_data']['puzzle']

    board = []
    for i in range(9):
        board.append(puzzle[9 * i:9 * i + 9])

    return board


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

def main():
    t1 = time.time()

    board = scrape_puzzle('hard')

    solve(board)

    for row in board:
        print(row)
    
    t2 = time.time()
    print("Time to solve: %rs" % (round(t2 - t1, 5)))
        
# main(example_board)
if __name__ == '__main__':
    main()



#PSUEDOCODE
#recursion until there are no empty slots
    #find open space
    #put in number
    #test if next square can have a solution
        #if not, put new number for previous spot

