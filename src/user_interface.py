from abc import ABC, abstractmethod


class UserInterface(ABC):

    @abstractmethod
    def get_data(self):
        ...


class ConsoleUserInterface(UserInterface):

    def get_data(self):
        print("Введите стороны треугольника:")

        a = input("Сторона A: ")
        b = input("Сторона B: ")
        c = input("Сторона C: ")

        return a, b, c
