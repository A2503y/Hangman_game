# Hangman Game

This project is a classic implementation of the Hangman game, developed using Python. Players try to guess a secret word by suggesting letters within a limited number of attempts.

## Installation

1.  **Ensure Python is installed:**
    You need Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2.  **Install Pygame:**
    This game uses the Pygame library. You can install it using pip:
    ```bash
    pip install pygame
    ```

## How to Play

1.  **Run the game:**
    Open your terminal or command prompt, navigate to the directory where you saved `hangman.py`, and run the following command:
    ```bash
    python hangman.py
    ```

2.  **Choose difficulty:**
    The game will prompt you to choose a difficulty level: `easy`, `medium`, or `hard`. Type your choice and press Enter.

3.  **Guess letters:**
    The game will display a series of underscores representing the letters in the secret word.
    Guess letters one by one by typing them and pressing Enter.
    - If you guess a correct letter, it will be revealed in the word.
    - If you guess an incorrect letter, a part of the hangman will be drawn, and your remaining attempts will decrease.

4.  **Winning and Losing:**
    - You win if you guess all the letters in the word before running out of attempts.
    - You lose if the hangman is fully drawn before you guess the word. The game will then reveal the word.
    - There's also a time limit of 60 seconds to guess the word.

## Contributing

Contributions are welcome! If you have suggestions for improvements or find any bugs, please feel free to:

1.  Open an issue to discuss the change you would like to make.
2.  Fork the repository and create a pull request with your changes.

Please make sure to update tests as appropriate.

## License

This project is currently not licensed. Please add license information if you plan to distribute it.
