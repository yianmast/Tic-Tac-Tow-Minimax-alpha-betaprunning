# Tic Tac Toe – Human vs Human or AI (Minimax / Alpha-Beta Pruning)

This is a Python implementation of the classic **Tic Tac Toe** game. You can play against another human or challenge a simple AI that uses either the **Minimax algorithm** or **Alpha-Beta Pruning** to make strategic moves.

## 🧠 Features

- Play **human vs human**
- Play **human vs AI** (you choose who goes first)
- Watch **AI vs AI** battles
- AI strategies:
  - **Minimax**: Explores all possible outcomes
  - **Alpha-Beta Pruning**: Optimized version of minimax with pruning
- Simple CLI interface
- Modular code for easy extension or experimentation

## 📦 Requirements

Only standard Python libraries are used:

```bash
math
random
```
Tested with Python 3.6+

## 🕹️ How to Play
Clone the repo or download tictactoe.py

Run the script: ```python tictactoe.py```

Choose your desired mode by calling the corresponding function in the script:

- hvh() – Human vs Human
- hvai(minimax) – You vs AI (You play first, AI uses Minimax)
- hvai(alpha_beta) – You vs AI (You play first, AI uses Alpha-Beta)
- aivh(minimax) – AI vs You (AI plays first, uses Minimax)
- aivh(alpha_beta) – AI vs You (AI plays first, uses Alpha-Beta)
- aivai(minimax) – AI vs AI (Minimax)
- aivai(alpha_beta) – AI vs AI (Alpha-Beta)

## 🎮 Controls
Input a number from 0 to 8 when prompted.

Board index layout:  
 0 | 1 | 2  
 3 | 4 | 5  
 6 | 7 | 8  

## 📁 Code Structure
win(state): Checks if the game is won.

valid(state, ind): Validates a move.

move(state, ind, player): Executes a move.

evaluate(state, player): Scores board state for AI.

minimax(...): Basic AI decision-making.

alpha_beta(...): Optimized AI strategy.

ai1, ai2: AI move functions.

h1, h2: Human move input functions.

Game mode functions: hvh, hvai, aivh, aivai

## How the AI Works
The AI's goal is to choose the best possible move to maximize its chances of winning (or at least drawing) the game.

### 1. Minimax Algorithm:  
Minimax is a recursive algorithm used in decision-making and game theory to find the optimal move for a player assuming the opponent also plays optimally.

The AI considers all possible moves and simulates the game for each move to the end (or to a specified depth).

It assigns scores to final game states:

+1 if AI wins

-1 if AI loses

0 if it's a draw

The algorithm chooses moves that maximize the AI's score while minimizing the opponent's score.

It simulates two players alternating turns:

The maximizing player (the AI, playing as 'o') tries to maximize the score.

The minimizing player (the opponent, playing as 'x') tries to minimize the score.

The recursion explores the game tree fully, which can be computationally expensive.

### 2. Alpha-Beta Pruning:  
Alpha-Beta Pruning is an optimization of the Minimax algorithm that reduces the number of nodes the AI evaluates in the game tree:

It keeps track of two values:

Alpha: the best (highest) score that the maximizer currently can guarantee at that level or above.

Beta: the best (lowest) score that the minimizer currently can guarantee at that level or above.

While searching the tree, if it finds a move that proves to be worse than a previously examined move, it prunes (cuts off) that branch, because the opponent would avoid that move.

This pruning drastically reduces the search space, speeding up the AI's decision-making without changing the final decision.

### How Moves Are Chosen
The AI evaluates all possible moves by recursively simulating the game with Minimax or Alpha-Beta Pruning.

It picks the move with the best score from its perspective:

If it’s the AI's turn, it picks the move with the maximum score.

If it’s the human's turn, it assumes the human picks the move with the minimum score.

This approach ensures the AI always plays optimally, either winning or forcing a draw.


## 🧑‍💻 Author
Ioannis Mastoras
Created on 11 April 2020
