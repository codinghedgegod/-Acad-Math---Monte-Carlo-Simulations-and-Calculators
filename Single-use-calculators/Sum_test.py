import math
n_dict= {"K": 2, "Q": 3, "J": 4, "10": 5, "9": 6, "8": 7, "7": 8, "6": 9, "5": 10, "4": 11, "3": 12}
def p(n):
    i = 0
    res = 0
    if n in range(2, 6):
        while i <= n-1:
            t1 = math.comb((n-1), i) * math.comb((12-n), (5-n+i)) * (7-i) / (math.comb(11, 4)  * 7)
            res += t1
            i+=1
    elif n in range(6, 9):
        while i <= 4:
            t2 = math.comb((n-1), (4-i)) * math.comb((12-n), i) * (12-n-i) / (math.comb(11, 4)  * 7)
            res += t2
            i+=1
    elif n in range(9, 13):
        while i <= (12-n):
            t3 = math.comb((n-1), (4-i)) * math.comb((12-n), i) * (12-n-i) / (math.comb(11, 4)  * 7)
            res += t3
            i+=1
    return res

for key, value in n_dict.items():
    res = p(value)
    print(f"{key}: {res}")


