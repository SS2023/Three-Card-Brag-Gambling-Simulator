from matplotlib import pyplot as plt

from cards import *
from rules import *

shuffle_deck()

if __name__ == '__main__':

    print('Setting up the table')

    print('Enter the betting amount:')
    value = int(input())
    fee = value

    print('Enter the number of players:')
    players = int(input())
    num = players

    for j in range(num):
        print('Enter the wallet size of Player {}:'.format(j))
        balance = int(input())

    print('Enter the number of rounds:')
    rounds = int(input())

    players_info = []
    lost_players = []

    for i in range(num):
        players_info.append([i, balance])

    player_names = [i[0] for i in players_info]

    original_two = balance
    original = fee
    sim = 10
    counter = 0
    winnings = 0
    X = []
    Y = []

    for z in range(sim):

        if z == sim - 1:

            plt.title("Simple Mean Simulator Ran {} times".format(sim))
            plt.xlabel("Simulations")
            plt.ylabel("Winnings")

            plt.plot(X, Y)
            plt.savefig("martingale.png")
            plt.clf()

        X.append(z)

        num = players

        for i in range(num):
            players_info.clear()
            lost_players.clear()
        for i in range(num):
            players_info.append([i, balance])

        fee = original
        balance = original_two

        for i in range(rounds):

            if (num > 1):

                print('Round {}'.format(i + 1))

                for j in range(num):
                    players_info[j][1] -= fee  # fee received

                players_cards = card_suit(num)

                for j in range(num):
                    print('Player {}\'s cards: {}'.format(players_info[j][0], players_cards[j]))

                players_scores = [card_pattern_checker(k) for k in players_cards]
                winner_index = players_scores.index(max(players_scores))
                players_info[winner_index][1] += num * fee

                print('Player {} Won!'.format(players_info[winner_index][0]))

                for j in players_info:
                    print("Player {} has {} dollars".format(j[0], j[1]))

                if winner_index != 0:
                    fee = fee * 2
                    print("Player 0 lost so betting double next round! The betting amount is {} dollars".format(fee))

                for j in players_info:
                    if (j[1] < fee):
                        lost_players.append(j)
                        players_info.remove(j)
                        num = num - 1
            else:

                print('\nOther players ran out of money.\nPlayer {} has won before reaching {} rounds.'.format(players_info[0][0], rounds))
                print('Final Results:')
                print('Player {} ended with {} dollars'.format(players_info[0][0], players_info[0][1]))

                for j in lost_players:
                    print('Player {} ended with {} dollars'.format(j[0], j[1]))

                print('###############################################################################################')

                if winner_index == 0:
                    Y.append(players_info[0][1])
                    counter = counter + 1
                    winnings = winnings + players_info[0][1]

                else:
                    Y.append(lost_players[0][1])
                    winnings = winnings + lost_players[0][1]

                if z == sim - 1:
                    print('Player 0 won {} games out of the {} !'.format(counter, sim))
                    probability = counter/sim * 100
                    print('The probability of winning with the martingale strategy is {}% !'.format(probability))
                    average_winnings = winnings/sim
                    print('On average, Player 0 ended up with {} dollars after each game !'. format(average_winnings))

                break