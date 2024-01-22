import math
import random
from time import sleep
from enum import Enum
from board import Board

# Enum defining possible representations for each player
class PlayerRepr(Enum):
    X = 1
    O = -1

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
            choice = input(f"It's {self.repr.name}'s turn. Input move (0-{board.dim ** 2 - 1}): ")

            try:
                choice = int(choice)
            except ValueError:
                print("Invalid position. Try again.")
                continue

            if choice < 0 or choice > (board.dim ** 2 - 1):
                print("Invalid position. Try again.")
            elif choice not in available_positions:
                print("The chosen position is occupied. Try again.")
            else:
                break
        board.move(choice, self.repr.name)
            

# Defines a player that randomly chooses a position to play
class RandomPlayer(Player):

    def __init__(self, repr: PlayerRepr) -> None:
        super().__init__(repr)

    def move(self, board: Board):
        choice = random.choice(board.get_available_positions())
        
        print(f"It's {self.repr.name}'s turn. {self.repr.name} chooses position {choice}.")
        sleep(0.5) # Adds a small delay of 0.5 second to make the UI clearer; optional

        board.move(choice, self.repr.name)


# Defines a player controlled by AI based on the Minimax algorithm
class ComputerPlayer(Player):

    def __init__(self, repr: PlayerRepr) -> None:
        super().__init__(repr)
        self.is_max_player = True if self.repr == PlayerRepr.X else False

    def move(self, board: Board):
        
        if board.is_empty(): # Chooses random position if the board is empty
            choice = random.choice(board.get_available_positions())
        else: # Executes the Minimax algorithm
            choice = self.minimax(
                board, self.is_max_player, depth=0,
                alpha=float('-inf'), beta=float('inf'),
            ).get('position')

        print(f"It's {self.repr.name}'s turn. {self.repr.name} chooses position {choice}.")
        sleep(0.5) # Adds a small delay of 0.5 second to make the UI clearer; optional

        board.move(choice, self.repr.name)

    # Minimax algorithm with alpha-beta pruning, which runs recursively up to 'depth'
    def minimax(self, board: Board, is_maximizing: bool, depth: int, alpha: float, beta: float) -> dict:
        from tictactoe import GameState

        # Check if the game is over or maximum depth has been reached
        if board.check_winner(PlayerRepr.X.name):
            return {'position': None, 'score': GameState.X_WINS.value}
        elif board.check_winner(PlayerRepr.O.name):
            return {'position': None, 'score': GameState.O_WINS.value}
        elif board.is_fully_occupied() or depth > 5:
            return {'position': None, 'score': GameState.TIE.value}
        
        # Initial score for min/max player
        if is_maximizing:
            best_metrics = {'position': None, 'score': -math.inf}
        else:
            best_metrics = {'position': None, 'score': math.inf}

        # Simulate move on all available positions (game state tree):
        # 1. Execute move on board;
        # 2. Call minimax() recursively;
        # 3. Undo move;
        # 4. Update best metrics;
        # 5. Do the alpha-beta pruning step.
        for position in board.get_available_positions():

            board.move(position, PlayerRepr.X.name if is_maximizing else PlayerRepr.O.name)

            metrics = self.minimax(board, not is_maximizing, depth + 1, alpha, beta)
            metrics['position'] = position

            board.undo_move(position)

            # Update best metrics according to min/max player
            if is_maximizing:
                if metrics['score'] > best_metrics['score']:
                    best_metrics = metrics
            else:
                if metrics['score'] < best_metrics['score']:
                    best_metrics = metrics

            # Alpha-beta pruning
            if is_maximizing:
                alpha = max(alpha, best_metrics['score'])
            else:
                beta = min(beta, best_metrics['score'])

            if beta <= alpha:
                break

        return best_metrics