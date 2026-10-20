import random


# Load words from the provided word list
def load_words():
    with open("google-10000-english-no-swears.txt", "r") as file:
        words = file.read().splitlines()

    # Keep only words with 4 or more alphabetic characters
    words = [
        word.lower()
        for word in words
        if word.isalpha() and len(word) >= 4
    ]

    return words


# Display the Hangman figure
def display_hangman(wrong_guesses):
    stages = [
        """
           +---+
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]

    print(stages[wrong_guesses])


# Play one round of Hangman
def play_game(words):
    secret_word = random.choice(words)

    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("\n================================")
    print("     HANGMAN WORD GUESSING GAME")
    print("================================")

    while wrong_guesses < max_wrong_guesses:

        # Display the current word
        display_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)
        print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

        # Check whether the player has guessed the complete word
        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word!")
            print("The word was:", secret_word)
            return

        guess = input("Enter a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabetic letter.")
            continue

        # Check duplicate guesses
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.add(guess)

        # Check the guess
        if guess in secret_word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

        display_hangman(wrong_guesses)

    print("\nGAME OVER!")
    print("The correct word was:", secret_word)


# Main program
def main():
    words = load_words()

    if not words:
        print("No suitable words found in the word list.")
        return

    while True:
        play_game(words)

        again = input("\nDo you want to play again? (yes/no): ").lower().strip()

        if again != "yes":
            print("\nThank you for playing Hangman!")
            break


if __name__ == "__main__":
    main()