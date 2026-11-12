
import random

HANGMAN_ART = [
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


def load_words():

    with open("google-10000-english-no-swears.txt", "r") as file:

        words = [
            line.strip().lower()
            for line in file
            if line.strip().isalpha()
        ]

    return words


words = load_words()

secret_word = random.choice(words)

print("\n===== HANGMAN WORD GUESSING GAME =====")
print("Guess the hidden English word!")
print("You have 6 incorrect attempts.\n")


guessed_letters = set()
won = False

wrong_guesses = 0
max_attempts = 6


while wrong_guesses < max_attempts:

    print(HANGMAN_ART[wrong_guesses])

    display_word = ""

    for letter in secret_word:

        if letter in guessed_letters:
            display_word += letter.upper() + " "
        else:
            display_word += "_ "

    print("\nGuess the word:")
    print(display_word)

    print("Guessed letters:", sorted(guessed_letters))
    print("Attempts left:", max_attempts - wrong_guesses)

    guess = input("\nEnter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter!")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.add(guess)

    if guess in secret_word:

        print("Correct guess!")

        if all(letter in guessed_letters for letter in secret_word):

            won = True
            print("\n==============================")
            print("     CONGRATULATIONS! YOU WON!")
            print("==============================")
            print("The word was:", secret_word.upper())
            break

    else:

        wrong_guesses += 1
        print("Wrong guess!")

    print("Attempts left:", max_attempts - wrong_guesses)


if not won:

    print(HANGMAN_ART[wrong_guesses])
    print("\n==============================")
    print("          GAME OVER!")
    print("==============================")
    print("The correct word was:", secret_word.upper())
