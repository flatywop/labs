from PIL import Image, ImageDraw, ImageFont
def lab1():
    image = Image.open("congrats.jpg.")
    width, height = image.size
    new_image = image.crop((100,100,width - 100,height-100))
    new_image.save("Cropped_image.jpg")
    new_image.show()



def lab2():
    holidays = {"день рождения": "hb.jpg", "новый год": "ng.jpg", "свадьба": "sv.jpg"}
    holiday = input("Какой праздник вам нужен? ")
    for day in holidays:
        if day == holiday:
            image = Image.open(holidays[day])
            image.show()


def lab3():
    name = str(input("Кого вы хотите поздравить? "))
    font = ImageFont.truetype('Roboto-Black.ttf', size=40)
    image = Image.open('congrats.jpg')
    width, height = image.size
    draw_text = ImageDraw.Draw(image)
    draw_text.text(
        (width / 2, height / 2),
        name,
        font=font,
        fill=("#000000")
    )
    font = ImageFont.truetype('Pacifico-Regular.ttf', size=40)
    draw_text = ImageDraw.Draw(image)
    draw_text.text(
        (width / 2 - 30, height / 2 + 50),
        ", поздравляю",
        font=font,
        fill=("#F64141")
    )
    image.show()
    image.save("congratulation.jpg")

lab3()
