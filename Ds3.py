num = int(input('Введите число от 0 до 100000: '))
flag = True

if (100000 >= num >= 0):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            # print(i)
            flag = False
    if flag == True:
        print(f'Число {num} - простое')
    else:
        print(f"Число {num} - cоставное")
else:
    print('Число может быть только в диапазоне от 0 до 100000')