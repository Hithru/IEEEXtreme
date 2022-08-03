# Challenge Name: Poker hands
# Difficulty: 10%

from typing import List


def hand_type(hand: List):
    hand_values = {}
    hand_suites = {}
    for card in hand:
        card_value = card[0]
        card_suite = card[1]
        if card_value == 'T':
            card_value = 10
        elif card_value == 'J':
            card_value = 11
        elif card_value == 'Q':
            card_value = 12
        elif card_value == 'K':
            card_value = 13
        elif card_value == 'A':
            card_value = 14
        else:
            card_value = int(card_value)

        hand_values.setdefault(card_value, 0)
        hand_values[card_value] += 1
        hand_suites.setdefault(card_suite, 0)
        hand_suites[card_suite] += 1
    tiebreak = []
    if len(hand_suites.keys()) == 1 and len(hand_values.keys()) == 5 and max(hand_values.keys()) == 14 and max(
            hand_values.keys()) - min(hand_values.keys()) == 4:
        # print("royal flush")
        return 10, tiebreak
    elif len(hand_suites.keys()) == 1 and len(hand_values.keys()) == 5 and max(hand_values.keys()) - min(
            hand_values.keys()) == 4:
        # print("Straight flush")
        tiebreak.append(max(hand_values.keys()))
        return 9, tiebreak
    elif 4 in hand_values.values():
        # print("Four of a Kind")
        four_value = []
        other_values = []
        for key in hand_values.keys():
            if hand_values[key] == 4:
                four_value.append(key)
            else:
                other_values.append(key)
        tiebreak = four_value + sorted(other_values, reverse=True)
        return 8, tiebreak
    elif 3 in hand_values.values() and 2 in hand_values.values():
        # print("Full House")
        three_value = []
        pair_value = []
        for key in hand_values.keys():
            if hand_values[key] == 3:
                three_value.append(key)
            elif hand_values[key] == 2:
                pair_value.append(key)
        tiebreak = three_value + pair_value
        return 7, tiebreak
    elif len(hand_suites.keys()) == 1:
        # print("Flush")
        return 6, tiebreak
    elif len(hand_values.keys()) == 5 and max(hand_values.keys()) - min(hand_values.keys()) == 4:
        # print("Straight")
        tiebreak.append(max(hand_values.keys()))
        return 5, tiebreak
    elif 3 in hand_values.values():
        # print("Three of a kind")
        three_values = []
        other_values = []
        for key in hand_values.keys():
            if hand_values[key] == 3:
                three_values.append(key)
            else:
                other_values.append(key)
        tiebreak = three_values + sorted(other_values, reverse=True)
        return 4, tiebreak
    elif 2 in hand_values.values() and len(hand_values.values()) == 3:
        # print("Two pairs")
        pair_values = []
        other_values = []
        for key in hand_values.keys():
            if hand_values[key] == 2:
                pair_values.append(key)
            else:
                other_values.append(key)
        tiebreak = sorted(pair_values, reverse=True) + sorted(other_values, reverse=True)
        return 3, tiebreak
    elif 2 in hand_values.values() and len(hand_values.values()) == 4:
        # print("One pair")
        pair_values = []
        other_values = []
        for key in hand_values.keys():
            if hand_values[key] == 2:
                pair_values.append(key)
            else:
                other_values.append(key)
        tiebreak = pair_values + sorted(other_values, reverse=True)
        return 2, tiebreak
    else:
        # print("High card")
        tiebreak = sorted(hand_values.keys(), reverse=True)
        return 1, tiebreak


with open("p054_poker.txt") as hands:
    player_one_win = 0
    player_two_win = 0
    draw = 0

    for line in hands:
        both_hand = line.strip().split(" ")
        player_one_hand = both_hand[:5]
        player_two_hand = both_hand[5:]

        player_one_hand_type, player_one_tiebreaks = hand_type(player_one_hand)
        player_two_hand_type, player_two_tiebreaks = hand_type(player_two_hand)

        if player_one_hand_type > player_two_hand_type:
            player_one_win += 1
        elif player_two_hand_type > player_one_hand_type:
            player_two_win += 1
        else:
            for i in range(len(player_one_tiebreaks)):
                if player_one_tiebreaks[i] > player_two_tiebreaks[i]:
                    player_one_win += 1
                    break
                elif player_two_tiebreaks[i] > player_one_tiebreaks[i]:
                    player_two_win += 1
                    break
            else:
                draw += 1
                print("draw hand", player_one_hand, player_two_hand)

    print("Player one wins : ", player_one_win)
    print("Player two wins : ", player_two_win)
    print("Draw            : ", draw)

# High Card: Highest value card - 1
# One Pair: Two cards of the same value - 2
# Two Pairs: Two different pairs - 3
# Three of a Kind: Three cards of the same value - 4
# Straight: All cards are consecutive values - 5
# Flush: All cards of the same suit - 6
# Full House: Three of a kind and a pair - 7
# Four of a Kind: Four cards of the same value - 8
# Straight Flush: All cards are consecutive values of same suit - 9
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit - 10
