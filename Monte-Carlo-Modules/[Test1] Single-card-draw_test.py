import random

a_suit = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

def draw_card(suit):
    rand = random.randint(0, 12)
    if suit:
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
        return target, emoji, suit
    else:
        r_r = random.randint(1, 4)
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
        return target, emoji, suit1


i = 1
n = 1
dict = {}
list_n = []
list_e = []
list_s = []
list_c = []
while i <= 1:
    list = draw_card("")
    list_n.append(list[0])
    list_e.append(list[1])
    list_s.append(list[2])
    list_c.append(list)
    i += 1

print(f"Numeral stats:")
while n <= 13:
    if n == 1:
        print(f"A: {list_n.count("A")}") 
    elif n == 11:
        print(f"J: {list_n.count("J")}") 
    elif n == 12:
        print(f"Q: {list_n.count("Q")}") 
    elif n == 13:
        print(f"K: {list_n.count("K")}")
    else:
        print(f"{n}: {list_n.count(n)}")
    n += 1
    

print("")
print(f"Suit stats:")
print(f"Spades♠️: {list_s.count("spade")}")
print(f"Club♣️: {list_s.count("club")}")
print(f"Heart♥️: {list_s.count("heart")}")
print(f"Diamond♦️: {list_s.count("diamond")}")
print("")
print(f"Overall stats:")
for item in list_c:
    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1
print(dict)

print(f"A total of {i - 1} cards are drawn.")







        

        

