class Player:
    def __init__(self, playerToken):
        self.playerToken = playerToken

    def getToken(self):
        return self.playerToken

    def setToken(self, token):
        self.playerToken = token


    def take_turn(self,boardState, boardIndex, valid_bin):
        """
        Asks for the player's move, checks whether the move is valid or not.
        :param boardState: A list of 81 integers representing the current board state (1 if occupied by X, 0 if empty, -1 if occupied by O).
        :param boardIndex: The index of the current board state from 0 to 8.
        :param valid_bin: A binary list of valid moves (1 is valid, 0 if invalid).
        :return: The location of the move to be done by the player, as an integer from 0 to 80.
        """
        try:
            if boardIndex is None:
                boardIndex, placement = map(int, input("Choose your board and then your move, from 1 to 9, separated by a space.\nExample 1 1 is board 1 square 1\n").strip().split())
                boardIndex -= 1
                placement -= 1
            else:
                print("Choose your move, from 1 to 9")
                placement = int(input()) - 1
            try:
                location = boardIndex * 9 + placement
                if boardState[location] == 0 and valid_bin[location] == 1:
                    return location
                else:
                    print("You cannot play in an occupied space!")
                    return self.take_turn(boardState, boardIndex, valid_bin)
            except IndexError or ValueError:
                print("Choose a valid number from 1 to 9")
                return self.take_turn(boardState, boardIndex, valid_bin)
        except ValueError:
            print("Only numbers are allowed!")
            return self.take_turn(boardState, boardIndex, valid_bin)