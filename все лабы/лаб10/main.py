from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont
import json
from pathlib import Path
import os, csv
def zad1():
    with open('продукты.json', encoding='UTF-8') as file:
        a = json.load(file)

    for item in a['products']:
        print('название:', item['name'])
        print('цена:', item['price'])
        print('вес:', item['weight'])
        if item['available']:
            print('в наличии')
        else:
            print('нет в наличии!')
        print()


def zad2():
    with open('продукты.json', encoding='UTF-8') as file:
        a = json.load(file)

    products = a["products"]

    for item in products:
        print(f"название: {item['name']}")
        print(f"цена: {item['price']}")
        print(f"вес: {item['weight']}")
        if item['available']:
            print("в наличии")
        else:
            print("нет в наличии!")
        print()

    name = input("название : ")
    price = int(input("цена: "))
    available = input("продукт есть в наличии?: ")
    if available == "да":
        available = True
    else:
        available = False

    weight = int(input("вес: "))

    new_item = {
        "name": name,
        "price": price,
        "available": available,
        "weight": weight
    }

    products.append(new_item)

    with open('продукты.json', 'w', encoding='UTF-8') as file:
        json.dump(a, file)

    products = a["products"]

    for item in products:
        print(f"название: {item['name']}")
        print(f"цена: {item['price']}")
        print(f"вес: {item['weight']}")
        if item['available']:
            print("в наличии")
        else:
            print("нет в наличии!")
        print()


def zad3():
    with open("en-ru.txt", "r") as file:
        l = file.readlines()

    d = {}

    for line in l:
        eng = line.split(" - ")[0].strip()
        ru = line.split(" - ")[1].strip().split(', ')
        for word in ru:
            if word not in d:
                d[word] = [eng]
            else:
                d[word].append(eng)
    with open("ru-en.txt", "w") as file:
        for ru, eng in sorted(d.items()):
            file.write(f"{ru} - {', '.join(eng)}\n")

zad3()