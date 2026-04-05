import random
card_list = []
a_suit = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
n_dict= {"A": 1, "K": 2, "Q": 3, "J": 4, "10": 5, "9": 6, "8": 7, "7": 8, "6": 9, "5": 10, "4": 11, "3": 12, "2": 13}
suits = ["♥️", "♦️", "♣️", "♠️"]


def numfy(input):
    if type(input) == str:
        new_str = input.replace("♥️", "").replace("♦️", "").replace("♣️", "").replace("♠️", "")
        return new_str
    elif type(input) == list:
        new_list = []
        for item in input:
            new_item = numfy(item)
            new_list.append(new_item)
        return new_list

def drawcards():
    card_list = []
    for item in a_suit:
        card_list.append(f"{suits[0]}{item}")
        card_list.append(f"{suits[1]}{item}")
        card_list.append(f"{suits[2]}{item}")
        card_list.append(f"{suits[3]}{item}")

    hearts_l = []
    for item in card_list:
        if "♥️" in item:
            hearts_l.append(item)
    
    non_hearts_l = []
    for item in card_list:
        if "♥️" not in item:
            non_hearts_l.append(item)
   
    def remove(card):
        card_list.remove(card)
        if card in hearts_l:
            hearts_l.remove(card)
        if card in non_hearts_l:
            non_hearts_l.remove(card)

   
    #--draw hero's cards--

    if one_card == "":
        hero_card_1 = random.choice(hearts_l)
        remove(hero_card_1)
        hero_card_2 = random.choice(hearts_l)
        remove(hero_card_2)
    else:
        hero_card_1 = f"♥️{one_card}"
        remove(hero_card_1)

        draw_list = [
            item for item in hearts_l
            if n_dict[numfy(item)] >= n_dict[one_card]
        ]
        if not draw_list:
            draw_list = hearts_l.copy()
        #print(draw_list)
        hero_card_2 = random.choice(draw_list)
        remove(hero_card_2)

    hero_card = [hero_card_1, hero_card_2]

    # --draw community cards--

    com_card_heart1 = random.choice(hearts_l)
    remove(com_card_heart1)
    com_card_heart2 = random.choice(hearts_l)
    remove(com_card_heart2)
    com_card_heart3 = random.choice(hearts_l)
    remove(com_card_heart3)
    com_card_4 = random.choice(non_hearts_l)
    remove(com_card_4)
    com_card_5 = random.choice(non_hearts_l)
    remove(com_card_5)
    community_card = [com_card_heart1, com_card_heart2, com_card_heart3, com_card_4, com_card_5]
    
    # --draw opponent cards--

    opp_card_1 = random.choice(card_list)
    remove(opp_card_1)
    opp_card_2 = random.choice(card_list)
    remove(opp_card_2)
    opp_card = [opp_card_1, opp_card_2]

    # ------------------------
    return hero_card, community_card, opp_card

round = int(input("how many rounds? "))
one_card = input("force the hero to draw a card? enter here: ").strip().upper()
time = int(input("how many times do you want to run the entire thing?"))

print(f"Running {time} times......")
k = 1
while k <= time:
    
    i = 0
    flush_counter = 0
    fh_counter = 0
    quads_counter = 0
    opp_flush_and_hero_win_counter = 0
    opp_flush_and_opp_win_counter = 0
    opp_round_win_counter = 0
    zero_paired_board_counter = 0
    single_paired_board_counter = 0
    two_paired_board_counter = 0
    board_trip_total_counter = 0

    #================================================================================
    while i < round:
        opp_flush = False
        opp_flush_and_hero_win = False
        opp_flush_and_opp_win = False
        opp_fh = False
        opp_quads = False
        board_trip = False
        board_pair_counter = 0
        #----------------
        d_cards = drawcards()
        hero_card = d_cards[0]
        community_cards = d_cards[1]
        opp_card = d_cards[2]

        # Determine if opp has flush and whose flush is bigger

        hero_7_cards = hero_card + community_cards
        opp_7_cards = opp_card + community_cards


        def flush(list):
            res1 = False
            heart_counter = 0
            heart_list = []
            clean_list = []
            flush_key = None
            for item in list:
                if "♥️" in item:
                    heart_counter += 1
                    heart_list.append(item)

            if heart_counter >= 5:
                res1 = True
                for item in heart_list:
                    num_n = n_dict[numfy(item)]
                    clean_list.append(num_n)
                flush_key = tuple(sorted(clean_list)[:5])
            return res1, flush_key

        def fh_quads(list):
            quads = False
            fh = False
            trip_count = 0
            pair_count = 0
            counter = {}
            for item in list:
                card_num = numfy(item)
                if card_num in counter:
                    counter[card_num] += 1
                else:
                    counter[card_num] = 1
            for key, value in counter.items():
                if value == 4:
                    quads = True
                elif value == 3:
                    trip_count += 1
                elif value == 2:
                    pair_count += 1
            if trip_count >= 1 and (pair_count >= 1 or trip_count >= 2):
                fh = True
            return quads, fh

        hero_flush = flush(hero_7_cards)
        opp_flush = flush(opp_7_cards)
        if opp_flush[0] == True:
            flush_counter += 1
            if hero_flush[0] == True:
                if hero_flush[1] < opp_flush[1]:
                    opp_flush_and_hero_win = True
                    opp_flush_and_hero_win_counter += 1
                elif hero_flush[1] > opp_flush[1]:
                    opp_flush_and_opp_win = True
                    opp_flush_and_opp_win_counter += 1
            else:
                opp_flush_and_opp_win = True
                opp_flush_and_opp_win_counter += 1
        
        opp_quads, opp_fh = fh_quads(opp_7_cards)
        if opp_quads == True:
            quads_counter += 1
        if opp_fh == True:
            fh_counter += 1

        if opp_flush_and_opp_win or opp_fh or opp_quads:
            opp_round_win_counter += 1
        
        com_board_num = numfy(community_cards)
        new_dict = {}
        for item in com_board_num:
            if item in new_dict:
                new_dict[item] += 1
            else:
                new_dict[item] = 1
        for key, value in new_dict.items():
            if value == 2:
                board_pair_counter += 1
            if value == 3:
                board_trip = True
        

        if board_trip == False:
            if board_pair_counter == 0:
                zero_paired_board_counter += 1
            elif board_pair_counter == 1:
                single_paired_board_counter += 1
            elif board_pair_counter == 2:
                two_paired_board_counter += 1
        else:
            board_trip_total_counter += 1

        #print(f"{hero_card}\n")
        #print(f"{opp_card}\n")
        #print(f"{community_cards}\n")

        i+= 1

    print(f"Run {k}")
    print("\n======================\n")
    print(f"A total of {round} rounds of cards were drawn.")
    print(f"There are {zero_paired_board_counter} no-paired board, that is { zero_paired_board_counter*100/round }%.")
    print(f"There are {single_paired_board_counter} single-paired board, that is { single_paired_board_counter*100/round }%.")
    print(f"There are {two_paired_board_counter} two-paired board, that is { two_paired_board_counter*100/round }%.")
    print(f"There are {board_trip_total_counter} board trips, that is { board_trip_total_counter*100/round}%.")
    print(f"---Admist those rounds, opponents drew---")
    print(f"{quads_counter} quads.")
    print(f"{fh_counter} full houses")
    print(f"{flush_counter} flushes.")
    print(f"-> admist those, hero wins {opp_flush_and_hero_win_counter}, opponent wins {opp_flush_and_opp_win_counter}.")
    print(f"You win {round-opp_round_win_counter} rounds.")
    print(f"----Rates----")
    print(f"Opponent full house rate: {fh_counter/round*100}%.")
    print(f"Opponent quads rate: {quads_counter/round*100}%.")
    print(f"Opponent flush rate: {flush_counter/round*100}%.")
    if flush_counter > 0:
        print(f"When opponent has flush, My flush_and_win rate: {opp_flush_and_hero_win_counter/flush_counter*100}%")
    else:
        print("When opponent has flush, My flush_and_win rate: 0%")
    print(f"Total win rate: {(round-opp_round_win_counter)/round*100}%.\n")

    k += 1

print("-----over-----")

   