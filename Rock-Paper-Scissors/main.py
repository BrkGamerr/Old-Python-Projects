import random

game_choices = {
    "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """,
    "paper": """
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """,
    "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """
}

computer_score = 0
user_score = 0


def play_the_game():

    global computer_score, user_score

    if user_choice == computer_choice:
        print("It's a draw!")
        return  # use return to cause StopIteration and skip rest of the if-else statements

    if user_choice == game_choices["rock"]:
        if computer_choice == game_choices["paper"]:
            print("Computer wins!")
            computer_score += 1
        else:
            print("You win!")
            user_score += 1

    if user_choice == game_choices["paper"]:
        if computer_choice == game_choices["rock"]:
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

    if user_choice == game_choices["scissors"]:
        if computer_choice == game_choices["rock"]:
            print("Computer wins!")
            computer_score += 1
        else:
            print("You win!")
            user_score += 1


def who_wins():

    global computer_score, user_score

    if user_score == computer_score:
        print(f"The Final Score - User: {user_score} Computer: {computer_score}")
        print("It's a draw.")
        print("Thank you for playing!")
        exit()
    elif user_score > computer_score:
        print(f"The Final Score - User: {user_score} Computer: {computer_score}")
        print("You win!")
        print("Thank you for playing!")
        exit()
    else:
        print(f"The Final Score - User: {user_score} Computer: {computer_score}")
        print("You lose!")
        print("Thank you for playing!")
        exit()


# MAIN CODE
while True:

    # random value choice from game_choices dictionary
    computer_choice = random.choice(list(game_choices.values()))

    # getting a value from key in dictionary based on what the user input is
    user_choice = game_choices[input("Choose 'rock', 'paper' or 'scissors': ").lower()]

    play_the_game()

    print(user_score)
    print(computer_score)

    # gives the user choice to stop the game
    want_to_continue = input("Want to continue playing? 'yes' or 'no': ").lower()

    if want_to_continue == "yes":
        continue
    else:
        who_wins()
