i = 0
while not i in range(1, 1000):
    try:
        i = int(input("Введите число: "))
    except ValueError:
        print("Неверное число")

if i / 10 < 1:
    print("1", i ** 2)
elif i / 100 < 1:
    print("2", i // 10 * i % 10)
elif i / 1000 < 1:
    print("3", f"{i % 10}{i // 10 % 10}{i // 100}")