from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance
def lab1():
    i = 0
    directory = "img"
    p = Path("../../../лабы/lab99/Lib/new_img")
    if not p.is_dir():
        p.mkdir(parents=True)
    pathlist = Path(directory).glob("*.jpg")
    for path in pathlist:
        image = Image.open(path)
        enhancer = ImageEnhance.Sharpness(image)
        img = enhancer.enhance(5)
        i += 1
        img.save(Path(p, str(i) + ".jpg"))


def lab2():
    with open("123.csv") as file:
        for s in file:
            print(s)


import csv
def lab3():
    with open('123.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        total_cost = 0
        products = []
        for row in reader:
            product = row['Produkti']
            quantity = int(row['Kolichestvo'])
            price = int(row['Cost'])
            cost = quantity * price
            total_cost += cost
            products.append(f"{product} - {quantity} шт. за {cost} руб.")

        print("Нужно купить:")
        print('\n'.join(products))
        print(f"Итоговая сумма: {total_cost} руб.")
lab3()