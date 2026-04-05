# For holding the same suit hole cards:
import random
import math
drawn_cards = ["null"]
a_suit = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
n_dict= {"A": 1, "K": 2, "Q": 3, "J": 4, "10": 5, "9": 6, "8": 7, "7": 8, "6": 9, "5": 10, "4": 11, "3": 12, "2": 13}

def draw_card(suit):
    card = "null"
    if suit:
        while card in drawn_cards:
            rand = random.randint(0, 12)
            if suit == "spade" or suit == "club" or suit == "heart" or suit == "diamond":
                target = a_suit[rand]

            if suit == "spade":
                emoji = "♠️"
            elif suit == "club":
                emoji = "♣️"
            elif suit == "heart":
                emoji = "♥️"
            elif suit == "diamond":
                emoji = "♦️"
            card = {"num": target, "emoji": emoji, "suit": suit}
            if card not in drawn_cards:
                drawn_cards.append(card)
                break
        return card
        
    else:
        while card in drawn_cards:
            r_r = random.randint(1, 4)
            rand = random.randint(0, 12)
            target = a_suit[rand]
            if r_r == 1:
                suit1 = "spade"
                emoji = "♠️"
            if r_r == 2:
                suit1 = "club"
                emoji = "♣️"
            if r_r == 3:
                suit1 = "heart"
                emoji = "♥️"
            if r_r == 4:
                suit1 = "diamond"
                emoji = "♦️"
            card = {"num": target, "emoji": emoji, "suit": suit1}
            if card not in drawn_cards:
                drawn_cards.append(card)
                break
        return card
    
def draw_hand(suit, a_card):
    if a_card == "":
        while True:
            my_card_1 = draw_card(suit)
            my_card_2 = draw_card(suit)
            if my_card_1 != my_card_2:
                break
        return my_card_1, my_card_2
    else:
        while True:
            my_card_1 = {"num": a_card, "emoji": "♥️", "suit": suit}
            if my_card_1 not in drawn_cards:
                drawn_cards.append(my_card_1)
                break
        while True:
            my_card_2 = draw_card(suit)
            if my_card_2["num"] != my_card_1["num"] or my_card_2["emoji"] != my_card_1["emoji"]:
                break
        return my_card_1, my_card_2

def draw_card_ex1s(ex_suit):
    suits = ["heart", "club", "diamond", "spade"]
    suits.remove(ex_suit)
    order = random.randint(0, 2)
    card = draw_card(suits[order])
    return card



def draw_community_cards(suit, amount):
    dicti = {}
    card_list = []
    if suit != "" and amount != "":
        i = 1
        while i <= amount:
            temp = draw_card(suit)
            dicti[f"card{i}"] = temp
            i+=1
        n = 1
        if amount <= 5:
            remaining = 5 - amount
            while n <= remaining:
                tempex = draw_card_ex1s(suit)
                dicti[f"card{n+amount}"] = tempex
                n += 1
   
        for key, value in dicti.items():
            card_list.append(value)

        # card_list = [dicti["card1"], dicti["card2"], dicti["card3"], dicti["card4"], dicti["card5"]]
        random.shuffle(card_list)
        return card_list
    else:
        flop1 = draw_card("")
        flop2 = draw_card("")
        flop3 = draw_card("")
        turn = draw_card("")
        river = draw_card("")
        return flop1, flop2, flop3, turn, river

# print(draw_hand_and_community_cards("heart"))
# ------------------------------------------------------------------------------
counter = int(input("\nHow many rounds?"))   
one_card = input("force the hero to draw a card? enter here: ")
k = 1
repeat = int(input("How many times do you want to run the entire thing?"))
print("\nPresets: A player draws two hold hand, both of which hearts. The player has an opponent. There are exactly three hearts on the community board.\n")
print(f"Running {repeat} times......")
while k <= repeat:
    
    i = 0
    quads_counter = 0
    fh_counter = 0
    set_fh_counter = 0
    set_counter = 0
    flush_counter = 0
    flush_and_win_counter = 0
    flush_and_lose_counter = 0
    single_paired_board_counter = 0
    two_paired_board_counter = 0
    zero_paired_board_counter = 0
    board_trip_counter = 0


    while counter > i:
        drawn_cards = ["null"]
        board_pair = 0
        board_trip = False
        my_card = draw_hand("heart", one_card)
        community_card = draw_community_cards("heart", 3)
        opp_card = draw_hand("", "")
        com_targetc = 0
        opp_targetc = 0
        check_d = {}
        check_l = []
        opp_quads = False
        opp_set = False
        opp_fh = False
        opp_set_fh = False
        opp_flush = False
        i_have_bigger_flush = False
        opp_have_bigger_flush = False


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

        for key, value in check_d.items(): #check if board is paired
            if value == 2:
                board_pair += 1
                if key == opp_card[0]["num"] or key == opp_card[1]["num"]:
                    if key == opp_card[0]["num"] and key == opp_card[1]["num"]:
                        opp_quads = True
                    else:
                        repeat_n = key
                        for item in community_card:
                            if item["num"] == opp_card[0]["num"] or item["num"] == opp_card[1]["num"]:
                                    if item["num"] != repeat_n:
                                        opp_fh = True
            elif value == 3:
                board_trip = True
                if key == opp_card[0]["num"] or key == opp_card[1]["num"]:
                    opp_quads = True
                else:
                    repeat_n0 = key
                    if opp_card[0]["num"] == opp_card[1]["num"]:
                        opp_fh = True
                    else:
                        for item in community_card:
                            if item["num"] == opp_card[0]["num"] or item["num"] == opp_card[1]["num"]:
                                if item["num"] != repeat_n0:
                                    opp_fh = True

                                
        if opp_quads != True and opp_fh != True:
            if opp_card[0]["num"] == opp_card[1]["num"]:
                repeat_n1 = opp_card[0]["num"]
                for item in community_card:
                    if item["num"] == repeat_n1:
                        opp_set = True
                        if board_pair > 0:
                            opp_set_fh = True

        if opp_flush == True:
            onum1 = n_dict[opp_card[0]["num"]]
            onum2 = n_dict[opp_card[1]["num"]]
            mnum1 = n_dict[my_card[0]["num"]]
            mnum2 = n_dict[my_card[1]["num"]]
            if onum1 > onum2:
                obig = onum2
            else:
                obig = onum1
            if mnum1 > mnum2:
                mbig = mnum2
            else:
                mbig = mnum1
            
            if mbig < obig:
                i_have_bigger_flush = True
            else:
                opp_have_bigger_flush = True

        #print(check_d)
        if board_pair == 1:
            single_paired_board_counter += 1
        elif board_pair == 2:
            two_paired_board_counter += 1

                
        if board_trip == True:
            board_trip_counter += 1    

        if board_pair == 0 and board_trip == False:
            zero_paired_board_counter += 1    

        if opp_quads == True:
            quads_counter += 1
        if opp_flush == True:
            flush_counter += 1
            if i_have_bigger_flush == True:
                flush_and_win_counter += 1
            elif opp_have_bigger_flush == True:
                flush_and_lose_counter += 1
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



    win_count = counter - fh_counter - quads_counter - set_fh_counter - flush_and_lose_counter
    win_rate = win_count / counter
    fh_rate = fh_counter / counter
    quads_rate = quads_counter / counter
    flush_rate = flush_counter / counter
    try:
        mfaw_rate = flush_and_win_counter / flush_counter
    except ZeroDivisionError:
        mfaw_rate = 0
    sfh_rate = set_fh_counter / counter
    print("\n======================\n")
    print(f"--Run #{k}--")
    print(f"A total of {counter} rounds of cards were drawn.")
    print(f"There are {zero_paired_board_counter} no-paired board, that is { zero_paired_board_counter*100/counter }%.")
    print(f"There are {single_paired_board_counter} single-paired board, that is { single_paired_board_counter*100/counter }%.")
    print(f"There are {two_paired_board_counter} two-paired board, that is { two_paired_board_counter*100/counter }%.")
    print(f"There are {board_trip_counter} board trips, that is { board_trip_counter*100/counter}%.")
    print(f"---Admist those rounds, opponents drew---")
    print(f"{quads_counter} quads.")
    print(f"{flush_counter} flushes.")
    print(f"-> admist those, hero wins {flush_and_win_counter}, opponent wins {flush_and_lose_counter}.")
    print(f"{set_fh_counter} set full houses.")
    print(f"{fh_counter} full houses")
    print(f"{set_counter} sets")
    print(f"You win {win_count} rounds.")
    print(f"----Rates----")
    print(f"Opponent full house rate: {fh_rate*100}%.")
    print(f"Opponent set full house rate: {sfh_rate*100}%.")
    print(f"Opponent quads rate: {quads_rate*100}%.")
    print(f"Opponent flush rate: {flush_rate*100}%.")
    print(f"When opponent has flush, My flush_and_win rate: {mfaw_rate*100}%")
    print(f"Total win rate: {win_rate*100}%.\n")
    k += 1

print("-----over-----")
    
