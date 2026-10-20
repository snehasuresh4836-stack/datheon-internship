# Hangman Word Guessing Game

## About the Project

This project is a console-based Hangman Word Guessing Game developed using Python as part of the Datheon Python Internship.

The game randomly selects an English word from the provided word list. The player has to guess the hidden word one letter at a time. The player is allowed a maximum of six incorrect guesses before the game ends.

## Features

- Random selection of words from the provided word list
- Hidden word display using underscores
- Letter-by-letter guessing
- Maximum of 6 incorrect guesses
- ASCII Hangman display
- Tracks previously guessed letters
- Prevents duplicate guesses
- Validates user input
- Displays the correct word when the player loses
- Displays a congratulatory message when the player wins
- Option to play multiple rounds

## Technologies Used

- Python 3
- Python Standard Library
- Random module
- File Handling

## Project Files

datheon-internship/
|
| `hangman.py` | Main Python program for the Hangman game |
| `google-10000-english-no-swears.txt` | English word list used by the game |
| `README.md` | Project documentation |

## How the Game Works

1. The program loads words from the provided text file.
2. Suitable English words are selected from the list.
3. The program randomly selects one word.
4. The selected word is hidden from the player.
5. The player enters one letter at a time.
6. If the letter is present in the word, it is revealed.
7. If the letter is incorrect, the number of wrong guesses increases.
8. The Hangman figure is updated after an incorrect guess.
9. The player wins when all letters of the word are correctly guessed.
10. The player loses after six incorrect guesses.

## Input Validation

The program checks the player's input and:

- Accepts only one alphabetic character at a time.
- Rejects numbers and special characters.
- Rejects multiple letters entered together.
- Prevents the same letter from being guessed repeatedly.

## How to Run

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

### Step 2: Open the Project

Open the project folder in VS Code.

### Step 3: Run the Program

Open the VS Code terminal and run:

```bash
python hangman.py

Example

================================
     HANGMAN WORD GUESSING GAME
================================

Word: _ _ _ _ _ _

Wrong guesses: 0 / 6

Enter a letter:

The player continues guessing letters until the word is completely revealed or six incorrect guesses are made.

Internship
This project was developed as part of the Python Internship at Datheon.
Author
Sneha Suresh

BCA (Honours) Student
