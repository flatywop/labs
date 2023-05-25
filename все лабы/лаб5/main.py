def check_in_list():
    list = [1, 2, 3, 4, 5]
    num = int(input("Напишите ваше число: "))
    if num in list:
        print(f"Исходный список: {list}. Ваше число: {num}. Поздравляю! Вы угадали число!")
    else:
        print(f"Исходный список: {list}. Ваше число: {num}. Нет такого числа!")

def check_repeat():
    list = [1, 2, 3, 4, 3, 2, 3, 5]
    list2 = []
    for i in list:
        if list.count(i) > 1:
            list2.append(i)
    print(f"Повторяющиеся числа: {set(list2)}")

def check_days():
    hol = []
    work = []
    tuple = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресение")
    num = int(input("Сколько вы хотите выходных? "))
    for i in range(len(tuple) - num, len(tuple)):
        hol.append(tuple[i])
    for i in range(len(tuple) - num):
        work.append(tuple[i])
    print(f"Ваши выходные дни: {hol}. Ваши рабочие дни: {work}")

def students():
    import random
    list1 = ["Петров", "Иванов", "Логунов", "Мышов", "Сыроваров"]
    list2 = ["Хорьков", "Ежов", "Ляпинов", "Ригунов", "Сашунов"]
    sport = []
    for i in range(3):
        sport.append(random.choice(list1))
        sport.append(random.choice(list2))
    sorted = sport
    sorted.sort()
    sport = tuple(sport)
    print(f"Первый список: {list1}, второй список: {list2}. Ваша спортивная команда: {sport}")
    print(f"Длинна кортежа: {len(sport)}")
    print(f"Кортеж, отсортированный по алфавитному порядку: {sorted}")
    if "Иванов" in sport:
        print(f"Фамилия Иванов встречается {sport.count('Иванов')}")

check_repeat()

