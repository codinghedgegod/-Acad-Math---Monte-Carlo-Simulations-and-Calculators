num1 = ""
result = float(0)
while num1 != "over":
    try:
        num1 = float(input("Enter the value. "))
    except ValueError:
        break
    num2 = float(input("Enter the odds. "))
    num3 = float(num1 * num2)
    result = float(result + num3)

print(f"The EV is {result}.")

