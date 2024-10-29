'''
As a user (AAU), I want to see a welcome message at the start of a game.
AAU, before being prompted for a move, I want to see the board printed in the console to know what moves have been made.
AAU, at the beginning of each turn, told whose turn it is: It’s player X’s turn!
AAU, I should be prompted to enter a move and be provided an example of valid input ('Enter a valid move (example: A1)').
AAU, I want to be able to enter my move’s column letter in upper or lower case (a/A, b/B, or c/C) to make it easier to enter my move.
AAU, if I enter a move in an invalid format or try to occupy a cell already taken, I want to see a message chastising me and be re-prompted.
AAU, after entering a move, I should once again be presented with the updated game board, notified of the current turn, and asked to enter a move for the other player. This process should continue until there is a winner or a tie
AAU, I should see a message at the end of the game indicating the winner or stating that the game ended in a tie.
'''

class Game():
    def __init__(self): 
        # When the game starts all inside Init are set as starting values
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
        self.turn = "X"
        self.tie = False
        self.winner = None

    # defining playgame
    def play_game(self):
        print('START')
    # render the game so it can be seen
    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
    """)
    # render and track current game state
    def print_message(self):
        if game_instance.tie == True:
            print("Tie Game!")
        elif game_instance.winner != None:
            print(f"{self.winner} wins the game!")
        else: print(f"It's player {self.turn}'s turn!")

game_instance = Game()
game_instance.play_game()
game_instance.print_board()