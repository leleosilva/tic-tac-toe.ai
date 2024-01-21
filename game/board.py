import numpy as np

class Board():
    
    # Constructor method
    def __init__(self, dim: int=3) -> None:
        self.dim = dim

        # Each board position is a dictionary that holds the
        # information of occupation and which player occupies it
        position = {'occupied': False, 'player': None}
        self.positions = np.array(
            [[position.copy() for _ in range(self.dim)] for _ in range(self.dim)],
            dtype=object
        )

    # String representation of Board
    def __str__(self) -> str:
        board_repr = "\n"
        positions_repr = [] # Stores the representation of each position
        
        # Iterate through positions, checking if they are occupied
        for row in range(self.dim):
            for col in range(self.dim):

                # Get the player string representation ('X' or 'O')
                if self.positions[row, col]['occupied'] == True:
                    positions_repr.append(self.positions[row, col]['player'])
                else: # Get the index of a unoccupied position
                    positions_repr.append(str(row * self.dim + col))
                    
        # Board with positions represented by 'X', 'O' or its index  
        for i in range(self.dim):
            
            # Alignment based on board dimension
            if self.dim ** 2 < 10: # Up to 9 positions
                alignment = ''
            elif self.dim ** 2 <= 100: # Up to 99 positions
                alignment = '^2'
            else:
                alignment = '^3' # 100 or more positions

            # Get representation per each row
            row_repr = positions_repr[(i * self.dim):((i+1) * self.dim)]

            board_repr += ('| ' + f' | '.join([format(repr, alignment) for repr in row_repr]) + ' |\n')
        return board_repr
    
    # Sets position as occupied by a player represented by 'X' or 'O'
    def occupy_position(self, position_idx: int, player_repr: str):
        
        # Converts 1-D array index to 2-D index (row and col)
        row_idx = position_idx // self.dim
        col_idx = position_idx % self.dim

        self.positions[row_idx, col_idx]['occupied'] = True
        self.positions[row_idx, col_idx]['player'] = player_repr

    # Sets position as not occupied
    def undo_move(self, position_idx: int):

        # Converts 1-D array index to 2-D index (row and col)
        row_idx = position_idx // self.dim
        col_idx = position_idx % self.dim

        self.positions[row_idx, col_idx]['occupied'] = False
        self.positions[row_idx, col_idx]['player'] = None
    
    # Checks if the board is totally empty.
    # np.ravel() is used to flatten the board to a 1-D array.
    def is_empty(self) -> bool:
        return all(position.get('occupied') == False for position in self.positions.ravel())
    
    # Checks if the board is fully occupied.
    # np.ravel() is used to flatten the board to a 1-D array.
    def is_fully_occupied(self) -> bool:
        return all(position.get('occupied') == True for position in self.positions.ravel())
    
    # Return the index of positions which are not occupied.
    # np.ravel() is used to flatten the board to a 1-D array.
    def get_available_positions(self) -> list:
        return [idx for idx, position in enumerate(self.positions.ravel()) if position.get('occupied') == False]

    # Check on each row whether a winner exists, based on two conditions:
    # 1. If a row is fully occupied;
    # 2. If the same player occupies the entire row.
    def check_winner_rows(self, player_repr: str):
        for row_idx in range(self.dim):
            row = self.positions[row_idx, :]
            
            row_fully_occupied = all(position.get('occupied') == True for position in row)
            player_fully_occupies = all(position.get('player') == player_repr for position in row)

            if row_fully_occupied and player_fully_occupies:
                return True
        return False

    # Check on each column whether a winner exists, based on two conditions:
    # 1. If a column is fully occupied;
    # 2. If the same player occupies the entire column.
    def check_winner_cols(self, player_repr: str):
        for col_idx in range(self.dim):
            col = self.positions[:, col_idx]
            
            col_fully_occupied = all(position.get('occupied') == True for position in col)
            player_fully_occupies = all(position.get('player') == player_repr for position in col)

            if col_fully_occupied and player_fully_occupies:
                return True
        return False

    # Check on each diagonal whether a winner exists, based on two conditions:
    # 1. If a diagonal is fully occupied;
    # 2. If the same player occupies the entire diagonal.
    def check_winner_diagonals(self, player_repr: str):
        
        # First diagonal
        diag1 = self.positions.diagonal()

        # The anti-diagonal is obtained by flipping the board
        # vertically with np.flipud()
        diag2 = np.flipud(self.positions).diagonal()

        diagonals = [diag1, diag2]
        for diag in diagonals:
            
            diag_fully_occupied = all(position.get('occupied') == True for position in diag)
            player_fully_occupies = all(position.get('player') == player_repr for position in diag)

            if diag_fully_occupied and player_fully_occupies:
                return True
        return False