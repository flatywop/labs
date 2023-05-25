
from PIL import Image, ImageOps, ImageEnhance
def first():
    image = Image.open("../../../лабы/Laba 6/123.jpg")
    image.show()
    print(f"Размер изображения: {image.size}, Формат изображения: {image.format}, цветовая модель: {image.mode}")


def second():
    image = Image.open("../../../лабы/Laba 6/123.jpg")
    w, h = image.size
    image.thumbnail((w / 3, h / 3))
    image.save("small.jpg")
    img = ImageOps.mirror(image)
    img.save("mirror.jpg")
    img = ImageOps.flip(image)
    img.save("flip.jpg")

def third():
    files = ["1.jpg","2.jpg","3.jpg","4.jpg","5.jpg",]
    for file in files:
        image = Image.open(file)
        enhancer = ImageEnhance.Sharpness(image)
        img = enhancer.enhance(5)
        img.save("new" + file)


def ford():
    image1 = Image.open("../../../лабы/Laba 6/123.jpg")
    image2 = Image.open("../../../лабы/Laba 6/1234.jpg")
    image1.paste(image2)
    image1.save("Water.jpg")
third()