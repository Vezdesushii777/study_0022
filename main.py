string = input("Введите строку:\n")
k = 0

for i in range(0, len(string)):
    if string[i] == "с" or string[i] == "c":
        k += 1
    if i == 2:
        continue
    print(string[i])

print("")

if k >> 0:
    print("В строке есть символ <с>\n")

print("Длина строки: ", len(string))
print("")

for i in range(0, len(string)):
    if i == len(string) -1 :
        continue
    print(string[i])