from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont
import json
from pathlib import Path
import os, csv
import tkinter as tk

def zad12_1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, work_time, location):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.work_time = work_time
            self.location = location

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")
            print(f'Время работы: {self.work_time}')
            print(f'Локация: {self.location}')

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, work_time, location, flavors):
            super().__init__(restaurant_name, cuisine_type, work_time, location)
            self.flavors = flavors

        def showing_flavors(self):
            print("Список доступных вкусов:")
            for flavor in self.flavors:
                print(f"- {flavor}")




    myIceCreamStand = IceCreamStand('ICE', "Кафе-мороженое", 'Пн-Пт, 8:00-00:00', 'Saint-Petersburg', ['mint', 'chocolate', 'vanilla'])
    myIceCreamStand.describe_restaurant()
    myIceCreamStand.showing_flavors()




def zad12_2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, work_time, location):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.work_time = work_time
            self.location = location

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")
            print(f'Время работы: {self.work_time}')
            print(f'Локация: {self.location}')

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, work_time, location, flavors):
            super().__init__(restaurant_name, cuisine_type, work_time, location)
            self.flavors = flavors

        def showing_flavors(self):
            print("Список доступных вкусов:")
            for flavor in self.flavors:
                print(f"- {flavor}")
    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, work_time, location, flavors):
            super().__init__(restaurant_name, cuisine_type, work_time, location)
            self.flavors = flavors

        def showing_flavors(self):
            print("Список доступных вкусов:")
            for flavor in self.flavors:
                print(f"- {flavor}")

        def add_flavor(self, flavor):
            self.flavors.append(flavor)
            print(f"Вкус {flavor} добавлен в список")

        def remove_flavor(self, flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
                print(f"Вкус {flavor} удален из списка")
            else:
                print(f"Вкус {flavor} не найден в списке")

        def check_flavor(self, flavor):
            if flavor in self.flavors:
                print(f"Вкус {flavor} есть в списке")
            else:
                print(f"Вкус {flavor} отсутствует в списке")

    class StickIceCream(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, work_time, location, flavors, stick_type):
            super().__init__(restaurant_name, cuisine_type, work_time, location, flavors)
            self.stick_type = stick_type

        def describe_stick_type(self):
            print(f"Тип палочки: {self.stick_type}")

    class SoftIceCream(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, work_time, location, flavors, cone_type):
            super().__init__(restaurant_name, cuisine_type, work_time, location, flavors)
            self.cone_type = cone_type

        def describe_cone_type(self):
            print(f"Тип рожка: {self.cone_type}")

    myIceCreamStand = IceCreamStand('Баскин-Роббинс', "Кафе-мороженое", 'Пн-Пт, 10:00-22:00', 'Saint-P', ['banana', 'cherry', 'vanilla'])
    myIceCreamStand.describe_restaurant()
    myIceCreamStand.showing_flavors()
    myIceCreamStand.add_flavor('strawberry')
    myIceCreamStand.remove_flavor('banana')
    myIceCreamStand.check_flavor('cherry')



def zad12_3():
    class IceCreamStand:
        def __init__(self, flavors):
            self.flavors = flavors
            self.selected_flavors = []

            self.root = tk.Tk()
            self.root.title("Ice Cream Stand")

            self.flavors_label = tk.Label(self.root, text="Available Flavors:")
            self.flavors_label.grid(row=1)



            self.flavors_listbox = tk.Listbox(self.root)
            for flavor in self.flavors:
                self.flavors_listbox.insert(tk.END, flavor)
            self.flavors_listbox.grid(row=2)

            self.selected_flavors_listbox = tk.Listbox(self.root)
            self.selected_flavors_listbox.grid(row=3)



            self.root.mainloop()

        def add_flavors(self):
            selected_indices = self.flavors_listbox.curselection()
            for index in selected_indices:
                flavor = self.flavors_listbox.get(index)
                if flavor not in self.selected_flavors:
                    self.selected_flavors.append(flavor)
                    self.selected_flavors_listbox.insert(tk.END, flavor)

        def remove_flavors(self):
            selected_indices = self.selected_flavors_listbox.curselection()
            for index in selected_indices:
                flavor = self.selected_flavors_listbox.get(index)
                self.selected_flavors.remove(flavor)
                self.selected_flavors_listbox.delete(index)

    if __name__ == "__main__":
        flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint"]
        ice_cream_stand = IceCreamStand(flavors)
