import random
from data import alphabet, words_list, hangman_art

LIVES = 6
GUESSED_LETTERS = []
TRIED_LETTERS = []
CHOSEN_WORD = random.choice(words_list)
DISPLAY = ["_" for letter in CHOSEN_WORD]


def correct_guess(guess):
    for letter in range(len(CHOSEN_WORD)):
        if CHOSEN_WORD[letter] == guess:
            DISPLAY[letter] = guess


def check_if_won():
    if LIVES == 0:
        print("\nYou lose!")
        print(f"\nThe word is: {CHOSEN_WORD}")
        exit()

    if "_" not in DISPLAY:
        print("\nYou win!")
        exit()


# MAIN CODE
while True:

    user_guess = input("\nEnter a letter you'd like to guess: ").lower()

    if user_guess not in alphabet:
        print("\nPlease enter letters only!")
        continue

    if user_guess in GUESSED_LETTERS:
        print(f"\nYou've already guessed: {user_guess.capitalize()}")
        print(*DISPLAY)
        continue
    elif user_guess in TRIED_LETTERS:
        print(f"\nYou've already tried: {user_guess.capitalize()}")
        print(*DISPLAY)
        continue

    if user_guess in CHOSEN_WORD:
        GUESSED_LETTERS.append(user_guess)
        print(hangman_art[f"{LIVES}"])
        correct_guess(user_guess)
    else:
        TRIED_LETTERS.append(user_guess)
        LIVES -= 1
        print(f"\nLives left: {LIVES}")
        print(hangman_art[f"{LIVES}"])

    print(*DISPLAY)

    check_if_won()
