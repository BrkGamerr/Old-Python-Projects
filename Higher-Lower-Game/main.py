import random
from os import system
from data import *


def clear():
    # Clears out the terminal
    system("cls")


def game_play():


    def compare_followers(a, b):
        # Compares the number of followers both accounts have.
        a_followers = a["follower_count"]
        b_followers = b["follower_count"]
        if a_followers > b_followers:
            return a_followers
        elif a_followers < b_followers:
            return b_followers
        else:
            return a_followers


    def versus():
        print(f"Compare A: {first_account["name"]}, {first_account["description"]}, from {first_account["country"]}.")
        print("VS")
        print(f"Compare B: {second_account["name"]}, {second_account["description"]}, from {second_account["country"]}.")


    first_account = random.choice(data)
    score = 0

    while True:

        second_account = random.choice(data)

        versus()

        higher_follower = compare_followers(a=first_account, b=second_account)

        guess = input("\nWho has more followers. Type 'A' or 'B': ").lower()

        if guess == "a":
            guess = first_account
        elif guess == "b":
            guess = second_account

        if guess["follower_count"] == higher_follower:
            score += 1
            first_account = guess
            print(f"\nYou're right! Score: {score}")
        else:
            print(f"Sorry, that's wrong! Final score: {score}")
            break


game_play()
