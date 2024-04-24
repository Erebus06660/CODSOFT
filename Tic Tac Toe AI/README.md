# Tic Tac Toe Game with AI (Python)

This Python script implements a Tic Tac Toe game using the Pygame library, with an AI opponent that makes moves based on the Minimax algorithm.

## Libraries Used

The following Python libraries are used in this project:

- **Pygame**: Pygame is a cross-platform set of Python modules designed for writing video games.
- **NumPy**: NumPy is a fundamental package for scientific computing with Python, providing support for arrays, matrices, and mathematical functions.
- **Sys**: The sys module provides access to some variables used or maintained by the Python interpreter and to functions that interact with the interpreter.
- **Copy**: The copy module provides functions for creating copies of objects.
- **Random**: The random module provides functions for generating random numbers.


## Controls: 
- Click on an empty square to place your move.
- Press 'g' to switch between AI mode and player vs. player mode.
- Press '0' to set AI level to random moves.
- Press '1' to set AI level to unbeatable.

## Code Structure

- `tic_tac_toe.py`: Contains the main game logic.
- `AI.py`: Defines the AI class with methods for evaluating moves using the Minimax algorithm.
- `Console.py`: Defines the Console class for managing the game board.

## Example

```python
# Import necessary modules
import pygame
import sys
from tic_tac_toe import Game, main

# Create a game instance
game = Game()

# Start the game loop
main()
```
## Acknowledgments

We would like to express our gratitude to CODSOFT for providing us with the opportunity to work on this project.
