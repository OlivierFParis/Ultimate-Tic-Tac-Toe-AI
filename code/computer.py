import heapq
import random

import pandas as pd

from player import Player


class Computer(Player):
    def __init__(self, playerToken, difficulty):
        super().__init__(playerToken)
        self.difficulty = difficulty
        self.model = None
        self.setDifficulty(difficulty)

    def get_difficulty(self):
        return self.difficulty

    def setDifficulty(self, difficulty):
        """
        Sets the difficulty of the AI by calling for the matching algorithmic model.
        :param difficulty: A string value representing the difficulty of the computer.
        :return: Nothing
        """
        if difficulty == "random":
            pass
        if difficulty == "easy":
            import joblib
            self.model = joblib.load("models/uttt_random_vs_random_model_X.pkl") if self.playerToken == 1 else joblib.load("models/uttt_random_vs_random_model_O.pkl")
        if difficulty == "medium":
            import joblib
            self.model = joblib.load("models/uttt_easy_vs_random_model_X.pkl") if self.playerToken == 1 else joblib.load("models/uttt_easy_vs_random_model_O.pkl")
        if difficulty == "hard_rf_model":
            import joblib
            self.model = joblib.load("models/hard_model_X.pkl") if self.playerToken == 1 else joblib.load("models/hard_model_O.pkl")
        if difficulty == "hard_gb_model":
            import joblib
            self.model = joblib.load("models/hard_gb_model_X.pkl") if self.playerToken == 1 else joblib.load("models/hard_gb_model_O.pkl")


    def setToken(self, token):
        self.playerToken = token
        self.setDifficulty(self.difficulty)

    def take_turn(self,boardState, boardIndex, valid_bin):
        """
        Master function to call for either a random movement or a movement predicted by an algorithmic model.
        :param boardState: A list of 81 integers representing the current board state (1 if occupied by X, 0 if empty, -1 if occupied by O).
        :param boardIndex: The index of the current board state from 0 to 8.
        :param valid_bin: A binary list of valid moves (1 is valid, 0 if invalid).
        :return: The location of the move to be done by the AI, as an integer from 0 to 80.
        """
        if self.difficulty == "random":
            return self.random_move(boardState, valid_bin)
        else:
            return self.ML_move(boardState, valid_bin)





    def random_move(self, boardState, valid_bin):
        """
        Selects a random move from the available moves.
        :param boardState: A list of 81 integers representing the current board state (1 if occupied by X, 0 if empty, -1 if occupied by O).
        :param valid_bin: A binary list of valid moves (1 is valid, 0 if invalid).
        :return: The location of the move to be done by the AI, as an integer from 0 to 80.
        """
        available_moves = get_available_moves(boardState, valid_bin)
        placement = int(random.choice(available_moves))
        return placement



    def ML_move(self, boardState, valid_bin):
        """
        Predicts the best available move from those available and valid.
        Computes the top-5 best moves and cycles through if invalid.
        If all 5 are invalid, calls for a random move.
        :param boardState: A list of 81 integers representing the current board state (1 if occupied by X, 0 if empty, -1 if occupied by O).
        :param valid_bin: A binary list of valid moves (1 is valid, 0 if invalid).
        :return: The location of the move to be done by the AI, as an integer from 0 to 80.
        """
        if boardState.count(0) >= 70:
            return self.random_move(boardState, valid_bin)
        # if boardState.count(0) >= 6:
        #     if random.random() < 0.55:
        #         return self.random_move(boardState)

        if not self.model:
            raise RuntimeError("Model not loaded for ML-based computer")

        df_input = pd.DataFrame([boardState], columns=[f"cell{i}" for i in range(81)])
        probs = self.model.predict_proba(df_input)[0]

        # Mask invalid moves
        masked_probs = [p if m == 1 else -1 for p, m in zip(probs, valid_bin)]

        # Try top-5 moves
        top_moves = heapq.nlargest(5, range(len(masked_probs)), key = lambda i: masked_probs[i])
        for move in top_moves:
            if boardState[move] == 0 and valid_bin[move] == 1:
                return move

        # Fallback
        print("No legal top-5 move - falling back to random.")
        return self.random_move(boardState, valid_bin)




def get_available_moves(boardState, valid_bin):
    """
    Function to return a list of the available position as integers from 0 to 80.
    :param boardState: A list of 81 integers representing the current board state (1 if occupied by X, 0 if empty, -1 if occupied by O).
    :param valid_bin: A binary list of valid moves (1 is valid, 0 if invalid).
    :return: A list of integers from 0 to 80 representing the available moves.
    """
    newlist = []
    for x in range(len(boardState)):
        if boardState[x] == 0 and valid_bin[x] == 1:
            newlist.append(x)
    return newlist

