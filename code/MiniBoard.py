
class MiniBoard:
    def __init__(self):
        self.tiles = [0] * 9
        self.winner = None
        self.full = False
        self.visual_win_state = []

    def make_move(self, pos, token):
        """
        Converts the specific position in the list into the player's token
        :param pos: A position from 0 to 8 representing the index of the cell in the tiles list
        :param token: An integer value for the player's token (1 if X, -1 if O)
        :return: A boolean value True if someone won, False otherwise
        """
        self.tiles[pos] = token
        return self.check_winner(token)

    def is_full(self):
        return self.full

    def is_won(self):
        return self.winner is not None


    def check_winner(self, token):
        """
        Checks whether someone won the small tic-tac-toe board
        :param token: An integer value for the player's token (1 if X, -1 if O)
        :return: True if someone won the small tic-tac-toe board, False otherwise
        """
        try:
            count = 0
            tiles = self.tiles.copy()
            win_states = [[0,1,2],[3,4,5],[6,7,8], #Horizontal
                          [0,3,6],[1,4,7],[2,5,8], #Vertical
                          [0, 4, 8], [2, 4, 6]]    #Diagonal

            for x in win_states:
                for y in x:
                    if tiles[y] != token:
                        count = 0
                        break
                    else:
                        count += 1
                if count == 3:
                    self.winner = token
                    self.full = True
                    self.set_visual_win_state()
                    return True
            if 0 not in tiles: self.full = True
            return False
        except IndexError:
            print("Something went wrong")
            exit()


    def get_tiles(self):
        return self.tiles

    def set_visual_win_state(self):
        """
        Sets the visual state of the board with a large symbolic representation of the player's token X or O.
        :return: Nothing
        """
        if self.winner == 1:
            self.visual_win_state = ["\u2572"," ","\u2571"," ","\u2573"," ","\u2571"," ","\u2572"]
        else:
            self.visual_win_state = ["\u256d","\u2501","\u256E","\u2503"," ","\u2503","\u2570","\u2501","\u256f"]

    def get_visual_win_state(self):
        return self.visual_win_state