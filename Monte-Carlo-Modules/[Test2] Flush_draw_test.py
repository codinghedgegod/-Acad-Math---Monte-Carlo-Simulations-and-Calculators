# For holding the same suit hole cards:
import random
import math
drawn_cards = ["null"]
a_suit = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

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
            card = f"({target}, '{emoji}', '{suit}')"
            if card not in drawn_cards:
                drawn_cards.append(card)
                break
        return target, emoji, suit
        
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
            card = f"({target}, '{emoji}', '{suit1}')"
            if card not in drawn_cards:
                drawn_cards.append(card)
                break
        return target, emoji, suit1
    
def draw_hand(suit):
    while True:
        my_card_1 = draw_card(suit)
        my_card_2 = draw_card(suit)
        if my_card_1 != my_card_2:
            break
    return my_card_1, my_card_2

def draw_hand_and_community_cards(suit):
    global drawn_cards
    drawn_cards = ["null"]
    my_card_list = draw_hand(suit)
    flop1 = draw_card("")
    flop2 = draw_card("")
    flop3 = draw_card("")
    turn = draw_card("")
    river = draw_card("")
    return my_card_list[0], my_card_list[1], flop1, flop2, flop3, turn, river

# print(draw_hand_and_community_cards("heart"))
# ------------------------------------------------------------------------------
def suit_test(suit):
    testlist = draw_hand_and_community_cards(suit)
    hand = [testlist[0], testlist[1]]
    flop = [testlist[2], testlist[3], testlist[4]]
    turn = testlist[5]
    river = testlist[6]

    flush_ind = 0
    S_in_cc = 0
    for item in flop:
        if suit in item:
            S_in_cc += 1
    if suit in turn:
        S_in_cc += 1
    if suit in river:
        S_in_cc += 1
    
    if S_in_cc >= 3:
        flush_ind = 1
    else:
        flush_ind = 0
    return flush_ind, hand, flop, turn, river

rounds_to_draw = int(input("How many rounds? ")) - 1
n = 0
flush_counter = 0
while n <= rounds_to_draw:
    list1 = suit_test("heart")
    # print(f"{n+1}: {list1}\n")
    flush_counter = flush_counter + list1[0]
    n += 1

print(f"\nA total of {n} rounds of cards were drawn.")
print(f"Flush: {flush_counter}")
print(f"The TFP is {flush_counter/n}\n")

# 博努力：X~B(n, 0.0640) -> 0.0640為理論值
print(f"Refrence")
print(f"The mathematical EV is {n*0.0640}, SD is {math.sqrt(0.0640 * n * 0.9359)}")

#ai assistance:
def C_func(num1, num2):
    return (
        math.lgamma(num1 + 1)
        - math.lgamma(num2 + 1)
        - math.lgamma(num1 - num2 + 1)
    )

def binomial_pmf(num1, num2, p):
    log_res = C_func(num1, num2) + num2 * math.log(p) + (num1 - num2) * math.log1p(-p)
    if log_res < -745:
        return 0.0
    return math.exp(log_res)


print(f"The odds of getting {flush_counter} flushes is {binomial_pmf(n, flush_counter, 0.0640)}")
#end of ai assistance

champ_t = math.floor((n + 1) * 0.0640)
champ = binomial_pmf(n, champ_t, 0.0640)
print(f"The highest odds of flushes get is {champ_t}, which is {champ}")


