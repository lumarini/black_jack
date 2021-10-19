import random
import os
clear = lambda: os.system('cls')
clear()

ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
cards = []


def deck_of_cards():
    for rank in ranks:
        for suit in suits:
            a = rank
            b = suit
            if ranks.index(a) == 0:
                c = 11
            elif ranks.index(a) > 9:
                c = 10
            else:
                c = ranks.index(a) + 1
            new_card = (a, b, c)
            cards.append(new_card)


deck_of_cards()

play = str.lower(input("Do you want to play a game of Black Jack?\nType 'Y' for Yes, or 'N' for No.  "))

player_cards = []
dealer_cards = []

player_points = []
dealer_points = []


def play_again():
    player_cards.clear()
    dealer_cards.clear()
    player_points.clear()
    dealer_points.clear()
    play_again = str.lower(input("Play again? Type 'Y' for Yes, or 'N' for No."))

    if play_again == "y":
        clear()
        deal_cards()
    elif play_again == "n":
        clear()
        print("You have ended the program. Goodbye!")


def calculate_player_score():
    player_points.clear()
    for player_card in player_cards:
        player_points.append(player_card[2])
        player_score = sum(player_points)
        if player_card[0] == "A" and player_score > 21:
            player_points.append(-10)
    player_score = sum(player_points)
    print(f"Your current score is {player_score}")
    get_result(player_score)


def calculate_dealer_score():
    player_points.clear()
    dealer_points.clear()

    for player_card in player_cards:
        player_points.append(player_card[2])
        player_score = sum(player_points)
        if player_card[0] == "A" and player_score > 21:
            player_points.append(-10)
    for dealer_card in dealer_cards:
        dealer_points.append(dealer_card[2])
        dealer_score = sum(dealer_points)
        if dealer_card[0] == "A" and dealer_score > 21:
            dealer_points.append(-10)
    player_score = sum(player_points)
    dealer_score = sum(dealer_points)
    print(f"Your current score is {player_score}")
    print(f"Dealer's score is {dealer_score}")
    next_card_dealer(player_score, dealer_score)


def next_card_dealer(player_score, dealer_score):
    if dealer_score < 17:
        print("Dealer has to get another card.")
        input("Press Enter to continue.")
        new_card_dealer = random.choice(cards)
        dealer_cards.append(new_card_dealer)
        cards.remove(new_card_dealer)
        print(f"Dealer's cards are: ")
        for card in dealer_cards:
            print(f"{card[0]} of {card[1]}")
        calculate_dealer_score()

    elif dealer_score == 21:
            print(f"Dealer wins with 21 points, you lose.")
            play_again()
    elif dealer_score > 21:
            print("Dealer's busted. You won!")
            play_again()
    elif dealer_score > 16:
        if dealer_score == player_score:
            print("It's a draw. Dealer wins.")
            play_again()
        elif dealer_score > player_score:
            print(f"Dealer wins with {dealer_score} points, you lose.")
            play_again()
        elif dealer_score < player_score:
            print(f"Dealer loses with {dealer_score} points. You win!")
            play_again()


def get_result(player_score):
    if player_score > 21:
        print("Busted. You lose.")
        print("...")
        play_again()

    elif player_score == 21:
        print("***Your score is 21. You win!***")
        play_again()

    elif player_score < 21:
        next_card_player = str.lower(input("Do you want another card?\nType 'Y' for Yes, or 'N' for No.  "))
        if next_card_player == "y":
            new_card = random.choice(cards)
            player_cards.append(new_card)
            cards.remove(new_card)
            print(f"Your cards are: ")
            for card in player_cards:
                print(f"{card[0]} of {card[1]}")
            calculate_player_score()
        elif next_card_player == "n":
            calculate_dealer_score()


def deal_cards():
    player_card_1 = random.choice(cards)
    player_cards.append(player_card_1)
    cards.remove(player_card_1)
    player_card_2 = random.choice(cards)
    player_cards.append(player_card_2)
    cards.remove(player_card_2)
    dealer_card_1 = random.choice(cards)
    dealer_cards.append(dealer_card_1)
    cards.remove(dealer_card_1)

    print(f"Your cards are {player_cards[0][0]} of {player_cards[0][1]} and {player_cards[1][0]} of {player_cards[1][1]}."
          f"\nYour score is {player_cards[0][2]+player_cards[1][2]}.\nDealer's card is {dealer_cards[0][0]} of {dealer_cards[0][1]}.")
    print("...")

    calculate_player_score()


if play == "y":
    deal_cards()
elif play == "n":
    print("You have ended the program. Goodbye!")
else:
    print("Error. Please select one of the options below.")
    str.lower(input("Do you want to play a game of Black Jack?\nType 'Y' for Yes, or 'N' for No.  "))


