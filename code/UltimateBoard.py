from MiniBoard import MiniBoard
RED = "\033[31m"
RESET = "\033[0m" # Resets all formatting

class UltimateBoard:
    def __init__(self):
        self.boards = [MiniBoard() for _ in range(9)]
        self.global_winner = None
        self.global_tie = False
        self.current_board_index = None  # Where the next move must go


    def make_move(self, pos, token):
        """
        Control function to add the token to specific smaller boards.
        Also calls functions to check if someone won, there's a tie, or the game can continue.
        :param pos: An integer from 0 to 80 indicating the position the player/AI will be making their move at
        :param token: The player's token (1 for X, -1 for O)
        :return: 1 if the game is won, 0 if tied, -1 otherwise
        """
        board_index = pos // 9
        local_index = pos % 9
        if self.boards[board_index].make_move(local_index,token):
            if self.check_winner(token):
                return 1
        if self.check_tie():
            return 0
        self.set_current_board_index(pos-board_index*9)
        return -1


    def set_current_board_index(self, new_board_index):
        """
        Sets the current board index to the board the next player must play in
        :param new_board_index: integer from 0 to 8 representing a small board in the larger one
        :return: Nothing
        """
        if self.boards[new_board_index].is_won(): # Can combine in one
            self.current_board_index = None
        elif self.boards[new_board_index].is_full():
            self.current_board_index = None
        else:
            self.current_board_index = new_board_index


    def check_winner(self, token):
        """
        Checks whether the game is won or not
        :param token: An integer value 1 or -1 representing the token of the player that just played
        :return: True if someone won, False otherwise
        """
        count = 0
        win_states = [[0,1,2],[3,4,5],[6,7,8], #Horizontal
                      [0,3,6],[1,4,7],[2,5,8], #Vertical
                      [0, 4, 8], [2, 4, 6]]    #Diagonal
        for x in win_states:
            for y in x:
                if self.boards[y].winner != token:
                    count = 0
                    break
                else:
                    count += 1
            if count == 3:
                self.global_winner = token
                return True
        return False


    def check_tie(self):
        """
        Checks whether the game is tied or not by checking if any small board is not full or won
        :return: False if there is no tie, True otherwise
        """
        for x in self.boards:
            if not x.is_full():
                return False
        else:
            return True


    def get_flattened_state(self):
        """
        Combine all 9 miniboard tiles into one list of 81
        :return: A list of 81 integers (1 for X, -1 for O, and 0 for empty)
        """
        return [tile for board in self.boards for tile in board.tiles]


    def get_visualized_state(self):
        """
        Returns a list containing X, O, " ", or a special symbol depending on the game state, instead of a list of (1, 0, -1)
        :return: Returns a list containing a visualized state of the board.
        """
        display = []
        for board in self.boards:
            if board.is_won():
                display.extend(board.get_visual_win_state())
            else:
                for cell in board.get_tiles():
                    display.append(symbol(cell))
        return display



    def get_valid_bin(self):
        """
        Creates a binary list for available positions across the whole board. 1 being a valid move, while 0 is for invalid moves.
        :return: The binary list of valid and invalid positions.
        """
        valid_bin = []
        if self.current_board_index is None:
            for i in range(9):
                if self.boards[i].is_won() or self.boards[i].is_full():
                    for j in range(9):
                        valid_bin.append(0)
                else:
                    for tile in self.boards[i].tiles:
                        valid_bin.append(1) if tile == 0 else valid_bin.append(0)
        else:
            for i in range(9):
                if i != self.current_board_index:
                    for j in range(9):
                        valid_bin.append(0)
                else:
                    for tile in self.boards[self.current_board_index].tiles:
                        valid_bin.append(1) if tile == 0 else valid_bin.append(0)

        return valid_bin


    def print_board(self):
        """
        Displays the full board
        :return: Nothing
        """
        full_state = self.get_visualized_state()
        if self.current_board_index is not None:
            color = RED
        else: color = None
        for large_row in range(3):
            for small_row in range(3):
                for large_col in range(3):
                    for small_col in range(3):
                        print(" " + f"{full_state[large_row*27 + large_col*9 + small_row*3 + small_col]}", end="")
                        if small_col < 2 and color is not None and (large_col+large_row*3)==self.current_board_index: print(f"{color} |{RESET}", end="")
                        elif small_col < 2: print(" |", end="")
                        if small_col == 2 and not large_col == 2:
                            print(" \u2503", end="")
                print()
                if small_row < 2:
                    for i in range(3):
                        if color is not None and (i+large_row*3)==self.current_board_index: print(f"{color}-----------{RESET}", end="")
                        else: print("-----------", end="")
                        if i < 2: print("\u2503", end="")
                    print()
                if small_row == 2 and not large_row == 2:
                    for i in range(35):
                        if i == 11 or i == 23:
                            print("\u254b", end="")
                        else:
                            print("\u2501", end="")
                    print()


    def get_current_board_index(self):
        return self.current_board_index


# 1 = "X", 0 = empty, -1 = "O"
def symbol(value):
    """
    Converts an integer to a token symbol.
    :param value: Either 1, 0, or 01
    :return: "X" if value is 1, "O" if value is -1, and a space " " for anything else.
    """
    return "X" if value == 1 else "O" if value == -1 else " "


'''
0  1  2  | 9  10 11 | 18 19 20
3  4  5  | 12 13 14 | 21 22 23
6  7  8  | 15 16 17 | 24 25 26
------------------------------
27 28 29 | 36 37 38 | 45 46 47
30 31 32 | 39 40 41 | 48 49 50
33 34 35 | 42 43 44 | 51 52 53
------------------------------
54 55 56 | 63 64 65 | 72 73 74
57 58 59 | 66 67 68 | 75 76 77
60 61 62 | 69 70 71 | 78 79 80
'''




