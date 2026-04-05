dic = {"ele": 0.007659, "ten": 0.056167, "nin": 0.168501, "eig": 0.272194, 
       "sev": 0.262113, "six": 0.157268, "fiv": 0.059653, "fou": 0.014203,
       "thr": 0.002061, "two": 0.000172, "one": 0.000000729, "zer": 0.00000117}
result = float(0)
counter = 11
v_list = list(dic.values())
while counter > -1:
    value = float(input(f"Enter value for {counter}: "))
    result = result + value * v_list[11 - counter]
    counter -= 1
print(f"The EV is {result}.")