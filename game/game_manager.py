from time import sleep
from tictactoe import TicTacToe

class GameManager():

    # Main loop that runs the manager and creates a tic-tac-toe instance
    def run(self) -> None:
        print("\nWelcome to tic-tac-toe!")
        sleep(1)
        
        while True:
            
            # Ask the user for information 
            player_type_1 = self.ask_player_type(is_first_player=True)
            sleep(0.25)
            player_type_2 = self.ask_player_type(is_first_player=False)
            sleep(0.25)
            dim_choice = self.ask_board_dim()
            sleep(0.25)
            
            game = TicTacToe(player_choices=[player_type_1, player_type_2], board_dim=dim_choice)
            outcome = game.play()

            # Show message based on the game outcome
            if outcome.value == 1:
                print(f"X wins the game!")
            elif outcome.value == -1:
                print(f"O wins the game!")
            else:
                print("It's a tie!")

            sleep(0.5)
            if self.ask_to_play_again() == False:
                break

    # Asks the user for the desired type of player (human, random or computer)
    def ask_player_type(self, is_first_player) -> int:
        player = (1, 'X') if is_first_player else (2, 'O')
        
        while True:
            print()
            print("1 - Human player")
            print("2 - Random player (chooses random positions)")
            print("3 - Computer player (based on Minimax algorithm)")
            choice = input(f"Choose the type for player {player[0]} ('{player[1]}'): ")

            try:
                choice = int(choice)
            except ValueError:
                print("\nInvalid choice. Try again.")
                continue
            if choice not in [1, 2, 3]:
                print("\nInvalid choice. Try again.")
            else:
                return choice

    # Asks the user for the desired board dimension     
    def ask_board_dim(self) -> int:

        while True:
            print()
            choice = input("Choose the dimension N for a NxN board (default = 3): ")

            # If the user presses Enter, chooses the default dimension
            if choice == "":
                return 3

            try:
                choice = int(choice)
            except ValueError:
                print("Invalid choice. Try again.")
                continue
            if choice <= 0:
                print("\nInvalid choice. Try again.")
            
            # The implementation might be slow for big dimensions,
            # including the Minimax algorithm
            elif choice > 20:
                print("Warning: the game might not be optimized for this dimension.")
                return choice
            else:
                return choice

    # Asks if the user wants to play again
    def ask_to_play_again(self) -> bool:
        
        while True:
            print()
            choice = input("Do you want to play again? (y/n): ")
            choice = choice.lower()

            if choice in ["y", "yes"]:
                return True
            elif choice in ["n", "no"]:
                return False
            else:
                print("Invalid choice. Try again.")

game_manager = GameManager()
game_manager.run()