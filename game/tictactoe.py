from enum import Enum
from board import Board
from player import *

# Enum defining possible game outcomes
class Outcome(Enum):
    X_WINS = 1
    O_WINS = -1
    TIE = 0


class TicTacToe:

    # Constructor method
    def __init__(self, player_choices: list[PlayerType], board_dim: int=3) -> None:
        self.board = Board(board_dim)

        self.players = []
        for p_number, p_type in enumerate(player_choices):
            player = self.define_player(p_number, p_type)
            self.players.append(player)

    # Creates and returns a player based on PlayerType enum value
    def define_player(self, player_number: int, player_type: int) -> Player:
        
        # By convention, the first player is always X (player_number == 0)
        repr = PlayerRepr.X if player_number == 0 else PlayerRepr.O

        if PlayerType.HUMAN.value == player_type:
            return HumanPlayer(repr)
        elif PlayerType.RANDOM.value == player_type:
            return RandomPlayer(repr)
        else:
            return ComputerPlayer(repr)

    def play(self):

        curr_player = self.players[0]
        while self.board.is_fully_occupied() == False:
            curr_player.move()
            
            if self.check_winner(curr_player):
                return f"{curr_player.repr} wins the game!"
            
            curr_player = self.change_turn(curr_player)
        
        return "It's a tie!"
    
    # Checks if the current player wins the game after playing their turn
    def check_winner(self, curr_player: Player):
        pass

    # Changes turn based on the current player
    def change_turn(self, curr_player: Player) -> Player:
        return self.players[0] if curr_player is self.players[1] else self.players[1]
    

game = TicTacToe([1, 2])
game.play()