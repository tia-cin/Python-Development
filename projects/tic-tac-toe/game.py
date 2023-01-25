from player import RandomAIPlayer, RandomDefaultPlayer

def play(game, px, po, print_game=True):
    letter = 'X'
    
    if print_game:
        game.print_board_nums()

    while game.empty_squares():
        if letter == 'O':
            square = po.get_move(game)
        else:
            square = px.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.print_board()
                print('')
            
            if game.curr_winner:
                if print_game:
                    print(f"{letter} wins!")

            letter = 'O' if letter == 'X' else 'X'

        if print_game:
            print("Tie!")


class TicTacToe:
    def __init__(self):
        # 3x3 board (9 blank spaces)
        self.board = [' ' for _ in range(9)]
        self.curr_winner = None
    
    def print_board(self):
        # draw vertical lines & board structure
        for row in [self.board[i * 3 : (i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # number location in board as strings
        num_board = [ [ str(i) for i in range(j * 3, (j + 1) * 3) ] for j in range(3)]

        for row in num_board:
            print('| ' + ' | '.join(row) + ' |')

    def free_moves(self):
        return [ i for i, spot in enumerate(self.board) if spot == ' ' ]

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return len(self.free_moves())

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter

            if self.is_winner(square, letter):
                self.curr_winner = letter
            return True
        return False

    def is_winner(self, square, letter):
        # check if 3 in rows
        row_index = square // 3
        row = self.board[row_index * 3 : (row_index + 1) * 3]

        if all([spot == letter for spot in row]):
            return True

        # check if 3 in columms
        col_index = square % 3
        col = [self.board[col_index * 3  + i * 3] for i in range(3)]

        if all([spot == letter for spot in col]):
            return True

        # check if 3 in diagonals
        if square % 2 == 0:
            d1 = [self.board[i] for i in [0, 4, 8]]
            d2 = [self.board[i] for i in [2, 4, 6]]

            if all([spot == letter for spot in d1]):
                return True
            if all([spot == letter for spot in d2]):
                return True
            
        return False
        
if __name__ == '__main__':
    px = RandomDefaultPlayer('X')
    po = RandomAIPlayer('O')
    t = TicTacToe()
    play(t, px, po, print_game=True)