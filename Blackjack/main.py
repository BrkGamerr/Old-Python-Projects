import random


def add_new_player(number):
    players[f"Player_{number}"] = {}
    players[f"Player_{number}"]["name"] = input("Enter your name: ").capitalize()
    players[f"Player_{number}"]["hand"] = random.sample(deck, 2)


def show_hands():
    # Shows the dealers cards to players - one card is hidden.
    print(f"\nDealers cards: * {dealer_cards[1]}")

    # Shows the players cards.
    for b in range(1, number_of_players + 1):
        hand = players[f"Player_{b}"]["hand"]
        name = players[f"Player_{b}"]["name"]
        print(f"{name}: {hand}")


def show_cards(player):
    # Shows players and dealers cards.
    print(f"\n{players[player]["name"]}: {players[player]["hand"]}")
    print(f"Dealer: {dealer_cards}")


def player_new_card(number):
    # Adds a card to players hand.
    hand = players[f"Player_{number}"]["hand"]
    hand.append(random.choice(deck))


def dealer_blackjack():
    # Checks if any player beside dealer got Blackjack
    print("\nDealer got Blackjack!")
    for c in players.keys():
        if sum(dealer_cards) and sum(players[f"{c}"]["hand"]) == 21:
            print(f"{players[f"{c}"]["name"]} - PUSH")
        else:
            pass
    exit()


def player_blackjack(number):
    # Checks if any players got Blackjack and adds them to blackjack_winners
    global blackjack_winners
    print(f"{players[f"Player_{number}"]["name"]} got Blackjack!")
    blackjack_winners.append(players[f"Player_{number}"]["name"])


def player_choice():
    # Shows players cards and lets him choose what to do next - hit or stand.
    for e in range(1, number_of_players + 1):
        player_name = players[f"Player_{e}"]["name"]
        while True:
            if sum(players[f"Player_{e}"]["hand"]) == 21:
                player_blackjack(number=e)
                break
            elif sum(players[f"Player_{e}"]["hand"]) < 21:
                user_choice = input(f"{player_name} what would like to do - Hit | Stand: ").lower()
                if user_choice == "hit":
                    player_new_card(e)
                    print(*players[f"Player_{e}"]["hand"])
                elif user_choice == "stand":
                    print(*players[f"Player_{e}"]["hand"])
                    break
            else:
                print(f"{players[f"Player_{e}"]["name"]} - Bust")
                del players[f"Player_{e}"]  # deletes the player if he bust
                break


# Variables
deck = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
players = {}
blackjack_winners = []

# Dealer gets two random cards from the deck.
dealer_cards = random.sample(deck, 2)

# Asks for the number of players and each of their names.
number_of_players = int(input("How many people are playing: "))
for a in range(1, number_of_players + 1):
    add_new_player(a)

# Shows cards at the beginning of the game.
show_hands()

# MAIN CODE
while True:

    if sum(dealer_cards) == 21:
        dealer_blackjack()

    player_choice()

    while sum(dealer_cards) < 17:
        dealer_cards.append(random.choice(deck))

    for g in players.keys():
        if sum(dealer_cards) > 21:
            print("\nDealer - Bust!")
            print(f"{players[g]["name"]} wins!")
            show_cards(player=g)
        elif sum(dealer_cards) == sum(players[f"{g}"]["hand"]):
            print("\nPush!")
            show_cards(player=g)
        elif sum(dealer_cards) > sum(players[f"{g}"]["hand"]):
            print("\nDealer wins!")
            show_cards(player=g)
        else:
            print(f"\n{players[g]["name"]} wins!")
            show_cards(player=g)

    print(f"\nPlayers who won with Blackjack: {blackjack_winners}")
    print("\nThank you for playing!")

    exit()
