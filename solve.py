board = [
    [0, 0, 1, 9, 4, 0, 8, 3, 0],
    [6, 0, 4, 0, 8, 7, 1, 0, 0],
    [0, 9, 0, 0, 1, 0, 0, 0, 7],
    [2, 0, 7, 1, 0, 0, 0, 8, 9],
    [0, 1, 8, 0, 6, 0, 7, 5, 0],
    [3, 4, 0, 0, 9, 0, 2, 1, 6],
    [7, 3, 0, 8, 2, 1, 5, 0, 4],
    [1, 5, 0, 4, 0, 0, 0, 2, 8],
    [0, 8, 2, 0, 5, 0, 3, 7, 0]
]

def display(board):
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - -")

        for column in range(len(board[row])):
            if column % 3 == 0 and column != 0:
                print(' | ', end="")

            if column == 8:
                print(board[row][column])
            else:
                print(str(board[row][column]) + " ", end="")

def find_slot(board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == 0:
                return (row, column)

    return False

def check(board, number, position):
    for column in range(len(board[position[0]])):
        if board[position[0]][column] == number and board[position[0]][column] != position[1]:
            return False

    for row in range(len(board)):
        if board[row][position[1]] == number and position[0] != row:
            return False

    box_x = position[1] // 3
    box_y = position[0] // 3

    for row in range(box_y * 3, box_y * 3 + 3):
        for column in range(box_x * 3, box_x * 3 + 3):
            if board[row][column] == number and position != (row, column):
                return False

    return True

def solve(board):
    slot = find_slot(board)

    if slot:
        row, column = slot

        for number in range(1, 10):
            if check(board, number, slot):
                board[row][column] = number

                if solve(board):
                    return True

                board[row][column] = 0

        return False
    else:
        return True

solve(board)
display(board)