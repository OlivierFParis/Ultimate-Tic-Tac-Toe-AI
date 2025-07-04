# Ultimate-Tic-Tac-Toe-AI

A fully functional, console-based Ultimate Tic Tac Toe game featuring both human and AI opponents, including a machine learning-powered bot trained using real gameplay data.

## Features

- Playable Ultimate Tic Tac Toe game in the console
- AI opponents:
  - Random AI: selects legal moves at random
  - Machine Learning AI: trained using `GradientBoostingClassifier` on over 12,000 moves from bot-vs-bot matches
- Move validation, enforced rules, and automatic game state printing
- Color-coded console display for enhanced readability
- Declares win, tie, or ongoing game automatically

## AI Training Approach

- Game data was collected by saving moves made by AI bots during hundreds of games
- Models trained using `scikit-learn`'s `GradientBoostingClassifier` on board states (81 features) and corresponding legal move (1 label)
- The best-performing model (trained on mixed difficulty bot matches) is included as `hard_gb_model_X.pkl` and `hard_gb_model_O.pkl`

## Project Structure

```
.
├── code/
│   ├── main.py                # Launches the game
│   ├── game.py                # Manages turn flow and overall game logic
│   ├── MiniBoard.py           # Represents a 3x3 local board
│   ├── UltimateBoard.py       # Combines 9 MiniBoards
│   ├── player.py              # Human player input handler
│   ├── computer.py            # AI player logic
│   ├── training_data.py       # Logs AI matches game data
│   ├── train_model.py         # Trains models from collected data
├── requirements.txt           # Python dependencies
├── README.md                  # Project description and usage
├── Mediumtraining_X.csv       # Sample training data
├── models/
│   ├── hard_gb_model_X.pkl        # Trained ML model for player X
│   ├── hard_gb_model_O.pkl        # Trained ML model for player O
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/OlivierFParis/Ultimate-Tic-Tac-Toe-AI.git
cd Ultimate-Tic-Tac-Toe-AI
```

2. (Optional) Create a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To start the game:

```bash
cd code
python main.py
```

The player symbol (X or O) is randomly assigned at the start of the game. Currently, the ML difficulty level is fixed, but functionality to select AI difficulty is planned for future updates.

## Training Your Own Model

- Use `training_data.py` to simulate games between bots and generate `.csv` datasets
- Run `train_model.py` to train your own model using the collected data
- You can customize the model type (e.g., `RandomForestClassifier`, `GradientBoostingClassifier`) and training parameters

## Notes

- This project does not include a GUI
- Only essential `.pkl` and `.csv` files are included due to GitHub's file size restrictions
- Game logic ensures all moves are legal and adheres strictly to Ultimate Tic Tac Toe rules

## License

This project is shared for educational and demonstration purposes.
