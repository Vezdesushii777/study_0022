# Овощи
firstName = input("Введите название первого овоща: ")
secondName = input("Введите название второго овоща: ")
thirdName = input("Введите навзание третьего овоща: ")

print(firstName.lower(), secondName.lower(), thirdName.lower())
print(firstName.upper(), secondName.upper(), thirdName.upper())
print(firstName.capitalize(), secondName.capitalize(), thirdName.capitalize())

firstQuantity = int(input("Введите количество первого овоща: "))
secondQuantity = int(input("Введите количество второго овоща: "))
thirdQuantity = int(input("Введите количество третьего овоща: "))

print("      Овощ            Количество  ")
print("{0:^17} {1:^20}" .format(firstName, firstQuantity))
print("{0:^17} {1:^20}" .format(secondName, secondQuantity))
print("{0:^17} {1:^20}" .format(thirdName, thirdQuantity))
