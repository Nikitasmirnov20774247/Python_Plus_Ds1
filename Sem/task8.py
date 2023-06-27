zv = "*"
prob = " "

hite = int(input("Введите высоту"))
shir = hite - 1
col_zv = 1

while hite > 0:
    for i in range(shir):
        print(prob, end="")
    for i in range(col_zv):
        print(zv, end="")
    
    shir -= 1
    col_zv += 2
    hite -= 1
    print()

# height = int(input("Введите высоту ёлки: "))

# for i in range(1, height + 1):
#     print(f"{' ' * (height - i)}{'*' * (i + (i - 1))}")