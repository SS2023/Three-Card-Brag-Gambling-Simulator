import random

cards = [i + 1 for i in range(13)]
suits = ['Spade', 'Club', 'Diamond', 'Heart']
deck = [[i, j] for i in cards for j in suits]

def shuffle_deck():

    random.shuffle(deck)
    return None

def card_suit(no_of_players):

    table = [[] for i in range(no_of_players)]
    shuffle_deck()

    for i in range(no_of_players):

        tempList = [no_of_players * j + i for j in range(3)]

        for j in tempList:

            table[i].append(deck[j])

    return table