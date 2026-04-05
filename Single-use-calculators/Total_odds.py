LR = {"A": 0, "K": 0.1818, "Q": 0.3455, "J": 0.4909, 
      "10": 0.6182, "9": 0.7273, "8": 0.8182, 
      "7": 0.8909, "6": 0.9455, "5": 0.9818, "4": 1, "3": 1}

DC = {"A": 0.1538, "K": 0.1410, "Q": 0.1282, "J": 0.1154, 
      "10": 0.1026, "9": 0.0897, "8": 0.0769, 
      "7": 0.0641, "6": 0.0513, "5": 0.0385, "4": 0.0256, "3": 0.0128}


dict = {}
for key, value in LR.items():
    p_LWR1F = 0.0283*value+0.0134
    print(f"{key}: {p_LWR1F*100}%\n")
    dict[key] = p_LWR1F

print(dict)
tot = 0
for key, value in DC.items():
    num = (1-dict[key])*value
    tot = tot+num

print(tot)


