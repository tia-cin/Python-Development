import random

def is_win(p1, p2):
    if (p1 == 'r' and p2 == 's'):
        return True
    
    elif (p1 =='s' and p2 == 'p') :
        return True
    
    elif (p1 == 'p' and p2 == 'r'):
        return True

    return False


def play():
    user_move = input("(R) for Rock, (P) for paper, (S) for scissors: ")
    computer_move = random.choice(['r', 'p', 's'])

    if user_move == computer_move:
        print("Tie!")

    elif is_win(user_move, computer_move):
        print("You won!")

    else: print("You lost!")

play()