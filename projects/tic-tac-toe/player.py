import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self, game):
        pass


class RandomAIPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.free_moves())
        return square

class RandomDefaultPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_move = False
        val = None
        
        while not valid_move:
            square = input(self.letter + '\'s turn. Write move (0-8): ')
            try:
                val = int(square)
                if val not in game.free_moves():
                    raise ValueError
                valid_move = True
            except ValueError:
                print('Invalid square, try again!')

        return val

class AIPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.free_moves()) == 9:
            square = random.choice(game.free_moves())
        else:
            square = self.minmax(game, self.letter)['position']
        return square

    def minmax(self, state, player):
        p_max = self.letter
        p_random = 'O' if player == 'X' else 'X'

        if state.curr_winner == p_random:
            return {
                'position': None,
                'score': 1 * (state.num_empty_squares() + 1)  if p_random == p_max  else -1 * (state.num_empty_squares() + 1)
            }

        elif not state.empty_squares():
            return {
                'position': None,
                'score': 0
            }
        
        if player == p_max:
            best = {
                'position': None,
                'score': -math.inf
            }
        else:
             best = {
                'position': None,
                'score': math.inf
            }

        for possible_move in state.free_moves():
            state.make_move(possible_move, player)

            simulation = self.minmax(state, p_random)

            state.board[possible_move] = ' '
            state.curr_winner = None
            simulation['position'] = possible_move

            if player == p_max:
                if simulation['score'] > best['score']:
                    best = simulation
            else:
                if simulation['score'] < best['score']:
                    best = simulation

        return best