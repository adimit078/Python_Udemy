import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

if (play == "y"):
    print(art.logo)

while play != "n":
    playerCards = []
    compCards = []
    playerTotal = 0
    compTotal = 0

    card1 = cards[random.randint(0,len(cards) - 1)]
    playerCards.append(card1)
    card2 = cards[random.randint(0,len(cards) - 1)]
    playerCards.append(card2)

    print(f"Your cards: {playerCards}, current score: {sum(playerCards)}")
    playerTotal = sum(playerCards)

    compCard1 = cards[random.randint(0, len(cards) - 1)]
    compCards.append(compCard1)
    print(f"Computer's first card: {compCard1}")

    compCard2 = cards[random.randint(0, len(cards) - 1)]
    compCards.append(compCard2)
    compTotal = sum(compCards)

    addCard = input("Type 'y' to get another card, type 'n' to pass: ")
    while (addCard != 'n'):
        if (playerTotal