def zad1():
    a = input()
    if len(a) < 6:
        print('пароль короткий')
    elif len(a) > 6:
        b = input()
        if a == b:
            print('пароли совпадают')
        else:
            print('пароли не совпадают')

def zad2():
    a = int(input())
    if a >= 38 and a <= 53:
        print('боковое место')
    elif (a >= 1 and a <= 37) and (a % 2 == 0):
        print('верхнее место в купе')
    elif (a >= 1 and a <= 37) and (a % 2 == 0):
        print('нижнее место в купе')

def zad3():
    a = int(input())
    if a % 4 == 0 or a % 400 == 0:
        print('год', a, 'високосный')
    else:
        print('этот год не високосный')

def zad4():
    a = input()
    b = input()
    if a != "красный" and a != "желтый" and a != "синий":
        print("ошибка цвета")
    elif b != "красный" and b != "желтый" and b != "синий":
        print("ошибка цвета")
    elif (a == "красный " and b == "желтый") or (a == "желтый" and b == "красный"):
        print("оранжевый")
    elif (a == "красный" and b == "синий") or (a == "синий" and b == "красный"):
        print("фиолетовый")
    elif (a == "синий" and b == "желтый") or (a == "желтый" and b == "синий"):
        print("зеленый")
    elif (a == "красный" and b == "красный"):
        print("красный")
    elif (a == "синий" and b == "синий"):
        print("синий")
    elif (a == "желтый" and b == "желтый"):
        print("желтый")

def zad5():
    n = int(input())
    l = []
    for i in range(n):
        slov = input()
        l.append(slov)
    print(l)
