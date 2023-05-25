from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont
import json
from pathlib import Path
import os, csv
import tkinter as tk


def zad11_11():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name} специализируется на кухне {self.cuisine_type}.")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")

    newRestaurant = Restaurant("Victor", "Итальянская")
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)

    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()



def zad11_1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"название ресторана: {self.restaurant_name}")
            print(f"тип кухни: {self.cuisine_type}")

        def open_restaurant(self):
            print("ресторан открыт")

    newRestaurant = Restaurant(input(), "Многонациональная")

    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)
zad11_11()



def zad11_2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"название ресторана: {self.restaurant_name}")
            print(f"тип кухни: {self.cuisine_type}")

    res_1 = Restaurant("Victor", "Итальянская")
    res_2 = Restaurant("Макдональдс", "Фастфуд")
    res_3 = Restaurant("Якудза", "Азиатская")

    res_1.describe_restaurant()
    res_2.describe_restaurant()
    res_3.describe_restaurant()



def zad11_3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating=0):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f"название ресторана: {self.restaurant_name}")
            print(f"тип кухни: {self.cuisine_type}")

        def open_restaurant(self):
            print(f"ресторан открыт!")

        def old_rating(self, rating):
            self.rating = rating
            print(f"рейтинг: {self.rating}")

        def new_rating(rate):
            rate.rating = float(input('новый рейтинг: '))
            print()
            newRestaurant = Restaurant("Victor", "Итальянская")
            newRestaurant.describe_restaurant()
            newRestaurant.open_restaurant()
            print(f"рейтинг обновлён: {rate.rating}")

    newRestaurant = Restaurant("Victor", "Итальянская")
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()
    newRestaurant.old_rating(4.7)
    print()
    newRestaurant.new_rating()