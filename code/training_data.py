
import csv
import os


class DataLogger:
    def __init__(self, filename):
        self.filename = filename
        self.rows = []

    def record(self, board, move):
        # board: list of 9 ints
        # move: int 0–8
        self.rows.append(board + [move])

    def save(self):
        header = [f"cell{i}" for i in range(81)] + ["label"]
        file_exists = os.path.exists(self.filename)
        with open(self.filename, "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(header)
            writer.writerows(self.rows)
        self.rows.clear()

    def correct_move(self, move):
        last_state = self.rows.pop()
        last_state[-1] = move
        self.rows.clear()
        self.rows.append(last_state)

    def loggers_clear(self):
        self.rows.clear()



