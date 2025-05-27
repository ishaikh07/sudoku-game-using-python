sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def print_board(b):
    for i in range(9):
        if i % 3 == 0:
            print("-" * 25)
        for j in range(9):
            if j % 3 == 0:
                print("|", end=" ")
            if (b[i][j]) > 0:
                print(b[i][j], end=" ")
            else:
                print(".", end=" ")
        print("|")
    print("-" * 25)

# print_board(sudoku_board) 

def check_validation(board):
    copy_board=board
    # row validation
    for row in board:
        for item in row:
            if item < 1 or item > 9:
                return "Invalid Board"
            elif row.count(item) > 1:
                return "Invalid Board"

    # # col validation i=1 [3, 0]
    for i in range(9):
        col = []
        for item in board:
            col.append(item[i])
        for val in col:
            if val < 1 or val > 9:
                return "Invalid Board"
            elif col.count(val) > 1:
                return "Invalid Board"

    # grid validation
    counter = 3
    initital=0
    for i in range(3):
        grid=[]
        for j in range(9):
            if j == 3 or j == 6:
                for item in grid:
                    if item < 1 or item > 9:
                        return "Invalid Board"
                    elif grid.count(item) > 1:
                        return "Invalid Board"
                grid=[]
            grid.extend(copy_board[j][initital:counter])
        
        for item in grid:
            if item < 1 or item > 9:
                return "Invalid Board"
            elif grid.count(item) > 1:
                return "Invalid Board"

        grid=[]
        counter+=3
        initital+=3
    
    return "Check Pass"

def play_game():
    print_board(sudoku_board)

    # check if user wants to play or validate
    to_do = int(input("Press 1 to check your sudoku or press 0 to enter new values: "))
    if to_do == 1:
        print(check_validation(sudoku_board))
    else:
        row  = int(input("enter your row=> ")) -1
        col = int(input("enter your col=> ")) -1
        v = int(input("Enter your value=> "))

        sudoku_board[row][col]=v
        print("Value Updated!!")

while True:
    play_game()
