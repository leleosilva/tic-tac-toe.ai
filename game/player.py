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

    def move(self):
        pass


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

    def move(self):
        pass