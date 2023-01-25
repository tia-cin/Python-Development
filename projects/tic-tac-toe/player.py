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
        return random.choice(game.free_moves())

class RandomDefaultPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_move = False
        val = None
        
        while not valid_move:
            square = input(self.letter + '\'s turn. Write move (0-9): ')
            try:
                val = int(square)
                if val not in game.free_moves():
                    raise ValueError
                valid_move = True
            except ValueError:
                print('Invalid square, try again!')

        return val