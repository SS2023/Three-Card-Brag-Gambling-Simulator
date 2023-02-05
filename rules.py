def color(num_card, type_card):

    if(len(list(set(type_card))) == 1):
        return True

    else:
        return False

def sequence(num_card, type_card):

    num_card.sort()

    if(num_card[1] == (num_card[2] + num_card[0])/2):
        return True

    else:
        return False

def color_sequence(num_card, type_card):

    return [color(num_card, type_card), sequence(num_card, type_card)]

def double(num_card, type_card):

    if(len(list(set(num_card))) == 2):
        return True

    else:
        return False

def triple(num_card, type_card):

    if(len(list(set(num_card))) == 1):
        return True

    else:
        return False

def card_pattern_checker(user_cards):

    res = 0
    num_card = [i[0] for i in user_cards]
    type_card = [i[1] for i in user_cards]

    if(double(num_card, type_card)):

        res = res + 1

        if(num_card.count(num_card[0]) == 2):

            twice_num_card = num_card[0]

            if (num_card.count(num_card[1]) == 1):

                single_num_card = num_card[1]

            else:
                single_num_card = num_card[2]

        else:

            twice_num_card = num_card[1]
            single_num_card = num_card[0]

        res = res + twice_num_card/100 + single_num_card/10000

        return res

    elif(color_sequence(num_card, type_card) == [True, False]):

        res = res + 2
        num_card.sort(reverse=True)
        biggest_card = num_card[0]
        second_card = num_card[1]
        smallest_card = num_card[2]

        if(biggest_card == 13 and second_card == 2 and smallest_card == 1):

            res = 4.129

        else:

            res = res + biggest_card/100 + second_card/10000 + smallest_card/1000000

        return res

    elif(color_sequence(num_card, type_card) == [False, True]):

        num_card.sort()
        res = res + 3
        biggest_card = num_card[-1]
        res = res + biggest_card/100
        return res

    elif(color_sequence(num_card, type_card) == [True, True]):

        num_card.sort()
        res = res + 4
        biggest_card = num_card[-1]
        res = res + biggest_card/100
        return res

    elif(triple(num_card, type_card)):

        res = res + 5
        only_card_num = list(set(num_card))[0]
        res = res + only_card_num/100
        return res

    else:

        num_card.sort()

        if(num_card[-1] == 13 and num_card[0] == 1 and num_card[1] == 2):

            res = 3.129

        else:

            biggest_card = num_card[-1]
            second_card = num_card[1]
            smallest_card = num_card[0]
            res = res + biggest_card/100 + second_card/10000 + smallest_card/1000000

    return res