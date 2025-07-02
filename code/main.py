import random

from computer import Computer
from game import TicTacToe
from player import Player
from training_data import DataLogger


def start_screen():
    """
    Start screen with the different option the user can select.
    :return: Nothing
    """
    keep_playing = True
    while keep_playing:
        print("Welcome to Ultimate Tic Tac Toe!")
        choice_1 = input("1. Player vs Player" + "\n" + "2. Player vs AI" + "\n" + "3. AI vs AI" + "\n" + "4. Training Sets" + "\n" + "5. Exit" + "\n")
        match choice_1: # Player vs Player
            case "1":
                playerList = make_player(2, None)
                run_game(playerList[0], playerList[1], None)

            case "2": # Player vs AI
                difficulty = ["","hard_gb_model"]
                playerList = make_player(1, difficulty)
                run_game(playerList[0], playerList[1], None)

            case "3": # AI vs AI

                difficulty = ["random","random"]
                playerList = make_player(0, difficulty)
                for i in range(0, 100):
                    run_game(playerList[0], playerList[1], None)
                    temp_token = playerList[0].getToken()
                    playerList[0].setToken(playerList[1].getToken())
                    playerList[1].setToken(temp_token)

            case "4": # Creating of Training sets by putting two AI against one another

                # Map each token to its logger
                x_logger = DataLogger("training_X.csv")
                o_logger = DataLogger("training_O.csv")

                # Create a dictionary to access by token
                loggers = {1: x_logger, -1: o_logger}

                difficulty = ["medium","random"]
                playerList = make_player(0, difficulty)
                for i in range(0, 600):
                    run_game(playerList[0], playerList[1], loggers)
                    x_logger.loggers_clear()
                    o_logger.loggers_clear()
                    temp_token = playerList[0].getToken()
                    playerList[0].setToken(playerList[1].getToken())
                    playerList[1].setToken(temp_token)

            case "5": # Exit
                keep_playing = False
            case _:
                print("Invalid choice!")


# Creates the player objects
def make_player(amount, difficulty):
    """
    Creates a player object by randomizing the tokens 1 for X and -1 for O.
    :param amount: The amount of players to make.
    :param difficulty: The difficulty of the AI to make in the return call function.
    :return: A list of player objects.
    """
    token_list = [1, -1]
    random.shuffle(token_list)
    playerList = []
    for i in range(0, amount):
        playerList.append(Player(token_list[i]))
    return chooseAI(amount, playerList,token_list, difficulty)


def chooseAI(amount, playerList, token_list, difficulty):
    """
    Creates the AI player object.
    The amount of AI players to make is determined by the amount argument passed to the makePlayer function, and will start from there until it reaches 2 players.
    :param amount: Amount of AI players to make (2-amount)
    :param playerList: A list of player objects.
    :param token_list: A list of shuffled tokens representing X for 1 and O for -1.
    :param difficulty: A list of string arguments indicating the difficulty of the AI to make.
    :return: A list of player objects.
    """
    if difficulty is None: # If there is no AI to be made
        return playerList
    else:
        for i in range(amount, 2):
            playerList.append(Computer(token_list[i], difficulty[i]))
        return playerList


# Function to begin the game
def run_game(player1,player2, loggers):
    """
    Function to begin the game
    :param player1: The first player object
    :param player2: The second player object
    :param loggers: The logger objects that will serve to create the training set for any AI opponent. None if not training.
    :return: Nothing
    """
    game = TicTacToe(player1, player2, loggers)
    game.play_game()


# Main function to start program
if __name__ == '__main__':
    start_screen()
    exit()






