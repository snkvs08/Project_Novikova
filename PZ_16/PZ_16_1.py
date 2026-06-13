#Создайте класс "Товар" с атрибутами "название", "цена" и "количество".
#Напишите метод, который выводит информацию о товаре в формате "Название: название, Цена: цена, Количество: кол-во"

class Tovar:
    def init(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def show(self):
        print(f"Название: {self.name}, Цена: {self.price}, Количество: {self.quantity}")

product1 = Tovar("Ноутбук", 50000, 10)
product1.show()