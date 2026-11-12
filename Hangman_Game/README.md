# Hangman Game

## Project Description

Hangman Game is a Python-based word guessing game where the player tries to guess a hidden word one letter at a time.

The program randomly selects a word from an external text file. The player must guess the correct letters before running out of attempts.

The game displays the hidden word using blanks and updates the word as the player guesses correctly. It also displays Hangman stages for incorrect guesses.

## Features

- Random word selection from a text file.
- Guess the hidden word one letter at a time.
- Displays correctly guessed letters.
- Tracks incorrect guesses.
- Allows a maximum of six wrong attempts.
- Prevents duplicate letter guesses.
- Validates user input.
- Displays Hangman ASCII art.
- Announces win or loss.
- Displays the correct word when the player loses.

## Technologies Used

- **Python 3** – Programming language.
- **random module** – Selects a random word.
- **File Handling** – Reads words from a text file.
- **set** – Stores already guessed letters.

## Project Structure

```text
Hangman_Game/
│
├── hangman.py
│
├── google-10000-english-no-swears.txt
│
└── README.md
```

## Requirements

- Python 3.x
- Visual Studio Code (recommended)
- Internet connection to download the word list initially.

No external Python packages are required.

## Word Dataset

The game uses a text file containing English words:

`google-10000-english-no-swears.txt`

Dataset source:

https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-no-swears.txt

## How to Run

**Step 1:** Download or clone the project.

**Step 2:** Open the project folder in Visual Studio Code.

**Step 3:** Make sure `hangman.py` and the word-list text file are in the same folder.

**Step 4:** Open the terminal.

**Step 5:** Run the program:

```bash
python hangman.py
```

**Step 6:** Start guessing letters to find the hidden word.

## Sample Output

```text
===== WELCOME TO HANGMAN GAME =====

Word: _ _ _ _ _

Guess a letter: a

Correct guess!

Word: _ a _ _ _

Guess a letter: e

Wrong guess!

Attempts remaining: 5

Guess a letter: p

Correct guess!

Word: p a _ _ _

...

Congratulations! You guessed the word!
```

*Actual output depends on the randomly selected word and the player's guesses.*

## Game Rules

1. The computer randomly selects a word.
2. The player guesses one letter at a time.
3. Correct guesses reveal the matching letters.
4. Incorrect guesses reduce the remaining attempts.
5. The player gets a maximum of six incorrect attempts.
6. The player wins by guessing all letters before running out of attempts.
7. The player loses if all six attempts are used.

## Learning Outcomes

Through this project, I learned:

- Python functions and loops.
- Conditional statements.
- Random word selection.
- Reading external text files.
- Working with strings and sets.
- User input validation.
- Tracking game attempts.
- Building a simple interactive console application.

## Author

Python Beginner Project

## License

This project is created for educational and learning purposes.