def check_div_3(number):
    try:
        if int(number) % 3 == 0:
            print("Делится")
        else:
            print("Не делится")
    except:
        print("Вы ввели что-то не то")

check_div_3(input("Введите число, которое я разделю на 3: "))

def div_100(number):
    try:
        answer = 100/int(number)
    except ValueError:
        print("Вы ввели не число")
    except ZeroDivisionError:
        print("На 0 делить нельзя")
    else:
        print(100 / int(number))

div_100(input("Введите делитель для 100: "))
def check_magic_date(date):
    try:
        if int(date.split(".")[0]) > 12 or int(date.split(".")[1]) > 12 or int(date.split(".")[1]) < 1 or int(date.split(".")[0]) < 1:
            return "Вы неправльно ввели дату или месяц"
        else:
            if int(date.split(".")[0]) * int(date.split(".")[1]) == int(date.split(".")[2][2:]):
                return True
            else:
                return False
    except:
        return "Вы ввели дату неправильно"
print(check_magic_date(input("Введите дату: ")))

def check_happy(num):
    try:
        sum1 = 0
        sum2 = 0
        for i in num[:int(len(num) / 2)]:
            sum1 += int(i)
        for j in num[int(len(num) / 2):]:
            sum2 += int(j)
        if sum1 == sum2:
            print("У вас счастливый билетик")
        else:
            print("У вас не счастливый билетик")
    except:
        print("Вы ввели что-то не то")

check_happy(input("Введите номер билетика: "))
