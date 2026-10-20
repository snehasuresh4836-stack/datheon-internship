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


## Task 2: Stock Portfolio Performance Tracker

### Project Overview

The Stock Portfolio Performance Tracker is a Python-based program that calculates the performance of a stock investment.

The program allows the user to enter an S&P 500 stock symbol, buy price, and number of shares. It retrieves the latest available stock price using the `yfinance` library and calculates the total investment, current portfolio value, gain or loss, and gain or loss percentage.

The portfolio results are also saved to a CSV file for future reference.

### Features

- Validates the stock symbol using an S&P 500 ticker dataset.
- Accepts the user's buy price and number of shares.
- Retrieves the latest available stock price using `yfinance`.
- Calculates total invested amount.
- Calculates current portfolio value.
- Calculates gain or loss.
- Calculates gain or loss percentage.
- Saves portfolio results to `portfolio_summary.csv`.
- Handles invalid stock symbols and invalid numerical inputs.

### Technologies Used

- Python
- CSV
- yfinance
- S&P 500 ticker dataset

### Project Files

```text
portfolio.py
sp500_tickers.csv
portfolio_summary.csv

How to Run
Install the required library:
pip install yfinance

Run the program:
python portfolio.py

The program requires an internet connection to retrieve the latest available stock price.

Example:
Enter S&P 500 stock symbol: AAPL
Enter your buy price: 200
Enter number of shares: 2

Fetching current stock price...

----------- PORTFOLIO SUMMARY -----------
Stock Symbol       : AAPL
Buy Price          : $200.00
Number of Shares   : 2
Current Price      : $...
Total Invested     : $400.00
Current Value      : $...
Gain/Loss          : $...
Gain/Loss %        : ...%
-----------------------------------------

Portfolio summary saved to portfolio_summary.csv
Learning Outcome
Through this task, I practiced:
- Reading data from CSV files
- Working with external Python libraries
- Retrieving stock market data
- Performing financial calculations
- Handling user input and errors
- Writing results to CSV files
- Building a practical Python application