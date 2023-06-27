num = int(input("Введите год: "))

if (num < 1582):
    result = "Нет календаря"
elif (num % 4 != 0 or num % 100 == 0 and num % 400 != 0):
    result = "Не высокосный"
else:
    result = "Высокосный"

print(result)