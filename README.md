# Rock-Paper-Scissors Game Readme

## Overview
This repository contains a simple Rock-Paper-Scissors game implemented in Python using the PyQt5 library for the graphical user interface. The game features a welcome screen, a home screen where the user can make selections, and a results screen displaying the outcome of each round.

## Features
- **Welcome Screen**: The initial screen that greets the user and prompts them to start the game.
- **Home Screen**: The main gameplay screen where the user can make selections (Rock, Paper, or Scissors) and play against the computer.
- **Result Screen**: The screen that shows the final results and provides an option to play again.

## Dependencies
- **PyQt5**: The main library for creating the graphical user interface.
- **sys**: Used for system-specific parameters and functions.
- **random**: Provides functions for generating pseudo-random numbers.
- **QTimer**: Part of PyQt5, used for executing functions with a delay.
- **QPixmap**: Part of PyQt5, used for handling images.

## How to Play
1. **Welcome Screen**: Run the program, and the welcome screen will appear. Click the "Start" button to proceed to the home screen.
2. **Home Screen**: Make your selection by clicking the corresponding button for Rock, Paper, or Scissors. The computer will randomly make its choice.
3. **Results**: After three rounds, the results screen will appear, showing the overall outcome. Click the "Play Again" button to return to the home screen.

## File Structure
- **Start-game.ui**: UI file for the welcome screen.
- **game.ui**: UI file for the home screen.
- **Stop-game.ui**: UI file for the results screen.
- **images/**: Folder containing images used in the game.

## How to Run
1. Make sure you have Python installed on your machine.
2. Install the required dependencies using the following command:
   pip install PyQt5
3. Run the game by executing the following command in the terminal:
   python <main.py>
   
## Credits
- This game was created by me.
