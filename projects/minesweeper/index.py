import random
import re

class Board:
    def __init__(self, size, bombs_num):
        # sizexsize board 
        self.size = size
        # default bombs in board
        self.bombs_num = bombs_num

        self.board = self.create_board() # with bombs planted
        self.assign_values()

        self.dug = set() # track of bombs location

    def create_board(self):
        board = [[None for _ in range(self.size)] for _ in range(self.size)]
        planted_bombs = 0

        while planted_bombs < self.bombs_num:
            bomb_location = random.randint(0, self.size**2 - 1)
            row = bomb_location // self.size # bomb in row
            col = bomb_location % self.size # bomb in column

            if board[row][col] == '*': # do not add other bomb where is one already
                continue
            board[row][col] = '*' # bomb added
            planted_bombs += 1 # track of planted bombs updated

        return board
        
    def assign_values(self):
        # scan through board
        for r in range(self.size):
            for c in range(self.size):
                # if there is already a bomb
                if self.board[r][c] == '*':
                    continue
                # define count of bombs around 
                self.board[r][c] = self.get_num_near_bombs(r, c)

    def get_num_near_bombs(self, row, col):
        count = 0 # trank of bombs

        # scan around bomb location
        for r in range(max(0, row-1), min(self.size-1, (row+1) + 1)):
            for c in range(max(0,col-1), min(self.size-1, (col+1) + 1)):
                # when location found
                if row == r and c == col:
                    continue
                # when bomb found 
                if self.board[r][c] == '*':
                    count += 1 # update track

        return count

    def dig(self, row, col):
        self.dug.add((row, col)) # update last dug

        # if bomb found
        if self.board[row][col] == '*':
            return False
        # when return num higher than 0
        elif self.board[row][col] > 0:
            return True

        # scan board
        for r in range(max(0, row-1), min(self.size-1, (row+1) + 1)):
            for c in range(max(0,col-1), min(self.size-1, (col+1) + 1)):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c) # responsive
            
        return True

    def __str__(self):
        vision_board = [[None for _ in range(self.size)] for _ in range(self.size)]

        for row in range(self.size):
            for col in range(self.size):
                if (row, col) in self.dug:
                    vision_board[row][col] = str(self.board[row][col])
                else:
                    vision_board[row][col] = ' '

        # visio board format
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.size):
            columns = map(lambda x: x[idx], vision_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(vision_board)):
            row = vision_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep
        


def play(size=10, bombs_num=10):
    board = Board(size, bombs_num)
    safe = True 

    while len(board.dug) < board.size ** 2 - bombs_num:
        print(board)
        user_input = re.split(',(\\s)*', input("Write row, col: "))
        row, col = int(user_input[0]), int(user_input[-1])

        if row < 0 or row >= board.size or col < 0 or col >= size:
            print("Invalid location, try again!")
            continue

        safe = board.dig(row, col)
        if not safe:
            break

    if safe:
        print("You won!")
    else:
        print("You lost!")
        board.dug = [(r, c) for r in range(board.size) for c in range(board.size)]
        print(board)

if __name__ == '__main__':
    play()

