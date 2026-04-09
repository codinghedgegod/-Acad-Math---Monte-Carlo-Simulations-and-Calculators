# For holding the same suit hole cards:
import random
import math
a_suit = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

Suitemoji = {
    "spade": "♠️",
    "club": "♣️",
    "heart": "♥️",
    "diamond": "♦️",
}


def build_deck():
    deck = []
    for suit, emoji in Suitemoji.items():
        for num in a_suit:
            deck.append({"num": num, "emoji": emoji, "suit": suit})
    return deck


def draw_random_card(deck, suit=None, exclude_suit=None):
    potent = []
    for card in deck:
        if suit is not None and card["suit"] != suit:
            continue
        if exclude_suit is not None and card["suit"] == exclude_suit:
            continue
        potent.append(card)
    card = random.choice(potent)
    deck.remove(card)
    return card


def draw_hand(deck, suit, a_card):
    if a_card == "":
        if suit == "":
            my_card_1 = draw_random_card(deck)
            my_card_2 = draw_random_card(deck)
        else:
            my_card_1 = draw_random_card(deck, suit=suit)
            my_card_2 = draw_random_card(deck, suit=suit)
        return my_card_1, my_card_2
    else:
        while True:
            fixed_card = None
            for item in deck:
                if item["suit"] == suit and item["num"] == a_card:
                    fixed_card = item
                    break
            my_card_1 = fixed_card
            deck.remove(my_card_1)
            if my_card_1 is not None:
                break
        my_card_2 = draw_random_card(deck, suit=suit)
        return my_card_1, my_card_2


def draw_community_cards(deck, suit, amount):
    if suit != "" and amount != "":
        suited = []
        not_suited = []
        for item in deck:
            if item["suit"] == suit:
                suited.append(item)
            else:
                not_suited.append(item)
        remain = 5 - amount
        suited_cards = random.sample(suited, amount)
        off_suit_cards = random.sample(not_suited, remain)
        card_list = suited_cards + off_suit_cards
        for item in card_list:
            deck.remove(item)
        random.shuffle(card_list)
        return card_list
    else:
        card_list = []
        for _ in range(5):
            card_list.append(draw_random_card(deck))
        return card_list

# print(draw_hand_and_community_cards("heart"))
# ------------------------------------------------------------------------------
quads_counter = 0
fh_counter = 0
set_fh_counter = 0
set_counter = 0
flush_counter = 0

counter = int(input("How many rounds?"))   
i = 0
while counter > i:
    deck = build_deck()
    board_pair = 0
    my_card = draw_hand(deck, "heart", "A")
    opp_card = draw_hand(deck, "", "")
    community_card = draw_community_cards(deck, "heart", 3)
    com_targetc = 0
    opp_targetc = 0
    check_d = {}
    check_l = []
    opp_quads = False
    opp_set = False
    opp_fh = False
    opp_set_fh = False
    opp_flush = False
    repeat_n = None

    for item in community_card:
        if "heart" in item["suit"]:
            com_targetc+=1
        
        if item["num"] not in check_d:
            check_d[item["num"]] = 1
        else:
            check_d[item["num"]] += 1

    for item in opp_card:
        if "heart" in item["suit"]:
            opp_targetc+=1

    if com_targetc >= 3:
        my_flush = True
        if com_targetc == 3 and opp_targetc == 2:
            opp_flush = True
        elif com_targetc == 4 and opp_targetc >= 1:
            opp_flush = True
        elif com_targetc == 5:
            opp_flush = True
    else:
        my_flush = False
        opp_flush = False

    for key, value in check_d.items():
        if value >= 2:
            if value == 2:
                board_pair += 1
                if key == opp_card[0]["num"] or key == opp_card[1]["num"]:
                    if key == opp_card[0]["num"] and key == opp_card[1]["num"]:
                        opp_quads = True
                    else:
                        repeat_n = key
                    for item in community_card:
                        if item["num"] == opp_card[0]["num"] or item["num"] == opp_card[1]["num"]:
                            if repeat_n is not None and item["num"] != repeat_n:
                                opp_fh = True
    if opp_quads != True:
        if opp_card[0]["num"] == opp_card[1]["num"]:
            repeat_n = opp_card[0]["num"]
            for item in community_card:
                if item["num"] == repeat_n:
                    opp_set = True
                    if board_pair > 0:
                        opp_set_fh = True

    if opp_quads == True:
        quads_counter += 1
    if opp_flush == True:
        flush_counter += 1
    if opp_set_fh == True:
        set_fh_counter += 1
    elif opp_set == True:
        set_counter += 1
    if opp_fh == True:
        fh_counter += 1
    
    #print("--------my card-------")
    #print(my_card)
    #print("--------opp card---------")
    #print(f"{opp_card}")
    #print("--------community card--------")
    #print(f"{community_card}")
    #print("========================")

    i += 1

print("======================")
print("Presets: A player draws two hold hand, both of which hearts. The player has an opponent. There are exactly three hearts on the community board.")
print(f"A total of {counter} rounds of cards were drawn.")
print(f"Admist those rounds, opponents drew:")
print(f"{quads_counter} quads.")
print(f"{flush_counter} flushes.")
print(f"{set_fh_counter} set full houses.")
print(f"{fh_counter} full houses")
print(f"{set_counter} sets")