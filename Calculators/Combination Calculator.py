

while True:
    C_up1_1 = int(input("Enter C_up1_1 "))
    C_up1_2 = int(input("Enter C_up1_2 "))
    C_up2_1 = int(input("Enter C_up2_1 "))
    C_up2_2 = int(input("Enter C_up2_2 "))

    C_down_1 = int(input("Enter C_down_1 "))
    C_down_2 = int(input("Enter C_down_2 "))

    def factorial(num):
        Res = 1
        while num != 1:
            Res = Res * num
            num -= 1
        return Res

    def C_func(num1, num2):
        num3 = num1 - num2
        Res = (factorial(num1)) / ((factorial(num2)) * factorial(num3))
        return Res



    C_down = int(C_func(C_down_1, C_down_2))

    if C_up2_2 == 0 or C_up2_2 == C_up2_1:
        C_up2 = 1
    else:
        C_up2 = int(C_func(C_up2_1, C_up2_2))

    if C_up1_2 == 0 or C_up1_2 == C_up1_1:
        C_up1 = 1
    else:
        C_up1 = int(C_func(C_up1_1, C_up1_2))

    Res = float(C_up1 * C_up2 / C_down)
    print(Res)

