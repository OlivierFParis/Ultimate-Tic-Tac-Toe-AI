import random

import computer
from UltimateBoard import UltimateBoard


# Tic Tac Toe Class used to call functions to run the game
class TicTacToe:
    def __init__(self, player_1, player_2, loggers):
        self.board = UltimateBoard()
        self.winner = False
        self.player_1 = player_1
        self.player_2 = player_2
        self.loggers = loggers # Dict mapping token -> logger
        self.starting_Player = None
        self.turn = 0


    # Function for Game Loop
    def play_game(self):
        if self.starting_Player is None: # Randomize starting player
            self.starting_Player = random.choice([self.player_1, self.player_2])
            self.turn = self.starting_Player

        # Main Game Loop
        while not self.winner:
            print("\n"+"Player {}'s turn".format(symbol(self.turn.getToken())))

            self.board.print_board()
            self.turn_move()

            # Switches whose turn it is
            if self.turn == self.player_1:
                self.turn = self.player_2
            else: self.turn = self.player_1



    def turn_move(self):
        """
        Function that calls for the Player/AI's move, record the present board state and mo
        :return: Nothing
        """
        placement = self.turn.take_turn(self.board.get_flattened_state(),self.board.get_current_board_index(), self.board.get_valid_bin())
        if isinstance(self.turn, computer.Computer) and self.loggers is not None:
            self.loggers[self.turn.getToken()].record(self.board.get_flattened_state(), placement)
        self.game_Outcome(self.board.make_move(placement, self.turn.getToken()))



    def game_Outcome(self, code):
        """
        Receives a code from the board class telling it whether someone won or if it's a tie.
        :param code: integer value 1 for someone won, 0 for tie.
        :return: prints the winner and terminates the main game loop by setting self.winner to True.
        """
        if code == 1:
            self.winner = True
            print()
            self.board.print_board()
            print("Player {} wins!".format(symbol(self.turn.getToken())))
            if isinstance(self.turn, computer.Computer) and self.loggers is not None:
                self.loggers[self.turn.getToken()].save()

        elif code == 0:
            self.winner = True
            print()
            self.board.print_board()
            print("We have a tie!")



def symbol(value):
    """
    Converts an integer to a token symbol.
    :param value: Either 1, 0, or 01
    :return: "X" if value is 1, "O" if value is -1, and a space " " for anything else.
    """
    return "X" if value == 1 else "O" if value == -1 else " "




