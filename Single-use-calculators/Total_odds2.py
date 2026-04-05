
a = [0.9784, 0.9926, 1]
k = [0.9728, 0.9503, 0.8182]
q = [0.9683, 0.9085, 0.6545]
j = [0.9645, 0.8670, 0.5091]
ten = [0.9609, 0.8260, 0.3818]
nine = [0.9578, 0.7853, 0.2727]
eight = [0.9552, 0.7449, 0.1818]
seven = [0.9532, 0.7050, 0.1091]
six = [0.9516, 0.7039, 0.0545]
five = [0.9506, 0.7031, 0.0182]
four = [0.9501, 0.7027, 0]
three = [0.9501, 0.7027, 0]

dict = {"a": a, "k": k, "q": q,"j": j, "10": ten, "9": nine, "8": eight, "7": seven,
        "6": six, "5": five, "4": four, "3": three}

def sum_of_all(valpha, vbeta, vgamma):
    value1 = 0.4159*0.2090*0.1990*valpha
    value2 = 0.1094*0.1915*0.1739*vbeta
    value3 = 0.1094*0.1915*0.8261*valpha
    value4 = 0.1094*0.8085*0.1990*valpha
    value5 = 0.0084*0.1702*0.1522*vgamma
    value6 = 0.0084*0.1702*0.8478*vbeta
    value7 = 0.0084*0.7298*0.1739*vbeta
    value8 = 0.0084*0.7298*0.8261*valpha
    result = value1 + value2 + value3 + value4 + value5 + value6 + value7 + value8
    return result

print(sum_of_all(0.9784, 0.9926, 1))
print(sum_of_all(1, 1, 1))
print(sum_of_all(a[0], a[1], a[2]))
print("\n")
for key, value in dict.items():
    print(f"{key} is {sum_of_all(value[0], value[1], value[2])}")