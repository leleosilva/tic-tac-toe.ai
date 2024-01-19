import numpy as np

class Board():
    
    # Constructor method
    def __init__(self, dim=3):
        self.board_dim = dim

        # Each board position is a dictionary that holds the
        # information of ocupation and which player occupies it
        position = {'occupied': False, 'player': None}
        self.positions = np.array(
            [[position.copy() for _ in range(self.board_dim)] for _ in range(self.board_dim)],
            dtype=object
        )

    # String representation of Board
    def __str__(self):
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
            board_repr += ('| ' + ' | '.join(positions_repr[(i * self.board_dim):((i+1) * self.board_dim)]) + ' |\n')

        return board_repr