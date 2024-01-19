import random
from enum import Enum
from board import Board

# Enum defining possible representations for each player
class PlayerRepr(Enum):
    X = 0
    O = 1

# Enum defining different types of players
class PlayerType(Enum):
    HUMAN = 1
    RANDOM = 2
    COMPUTER = 3


# Parent class for all types of players
class Player():

    def __init__(self, repr: PlayerRepr) -> None:
        self.repr = repr

    def move(self):
        pass


# Defines a player controlled by a human
class HumanPlayer(Player):
    
    def __init__(self, repr: PlayerRepr) -> None:
        super().__init__(repr)

    def move(self, board: Board):
        available_positions = board.get_available_positions()

        while True:
            choice = input(f"\n{self.repr}'s turn. Input move (0-{board.dim ** 2 - 1}): ")

            try:
                choice = int(choice)
            except ValueError:
                print("Invalid position. Try again.")
                continue

            if 0 > choice or choice > board.dim ** 2 - 1:
                print("Invalid position. Try again.")
            elif choice not in available_positions:
                print("The chosen position is occupied. Try again.")
            else:
                break
        board.occupy_position(choice, self.repr)
            


# Defines a player that randomly chooses a position to play
class RandomPlayer(Player):

    def __init__(self, repr: PlayerRepr) -> None:
        super().__init__(repr)

    def move(self, board: Board):
        choice = random.choice(board.get_available_positions())
        board.occupy_position(choice, self.repr)



# Defines a player controlled by AI based on the Minimax algorithm
class ComputerPlayer(Player):

    def __init__(self, repr: PlayerRepr) -> None:
        super().__init__(repr)

    def move(self, board: Board):
        pass