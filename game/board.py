import numpy as np

class Board():
    
    # Constructor method
    def __init__(self, dim: int=3) -> None:
        self.board_dim = dim

        # Each board position is a dictionary that holds the
        # information of ocupation and which player occupies it
        position = {'occupied': False, 'player': None}
        self.positions = np.array(
            [[position.copy() for _ in range(self.board_dim)] for _ in range(self.board_dim)],
            dtype=object
        )

    # String representation of Board
    def __str__(self) -> str:
        board_repr = ""
        positions_repr = [] # Stores the representation of each position
        
        # Iterate through positions, checking if they are occupied
        for row in range(self.board_dim):
            for col in range(self.board_dim):

                # Get the player string representation ('X' or 'O')
                if self.positions[row, col]['occupied'] == True:
                    positions_repr.append(self.positions[row, col]['player'])
                else: # Get the index of a unoccupied position
                    positions_repr.append(str(row * self.board_dim + col))
                    
        # Board with positions represented by 'X', 'O' or its index  
        for i in range(self.board_dim):
            
            # Alignment based on board dimension
            if self.board_dim ** 2 < 10: # Up to 9 positions
                alignment = ''
            elif self.board_dim ** 2 <= 100: # Up to 99 positions
                alignment = '^2'
            else:
                alignment = '^3' # 100 or more positions

            # Get representation per each row
            row_repr = positions_repr[(i * self.board_dim):((i+1) * self.board_dim)]

            board_repr += ('| ' + f' | '.join([format(repr, alignment) for repr in row_repr]) + ' |\n')
        return board_repr
    
    # Checks if the board is fully occupied.
    # np.ravel() is used to flatten the board to a 1-D array.
    def is_fully_occupied(self) -> bool:
        return all(position.get('occupied') == True for position in self.positions.ravel())
    
    # Return the index of positions which are not occupied.
    # np.ravel() is used to flatten the board to a 1-D array.
    def get_available_positions(self) -> list:
        return [idx for idx, position in enumerate(self.positions.ravel()) if position.get('occupied') == False]
        
    def check_winner_rows(self):
        pass

    def check_winner_cols(self):
        pass

    def check_winner_diagonals(self):
        pass