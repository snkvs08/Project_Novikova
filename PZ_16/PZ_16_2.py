#Создайте базовый класс "Фигура" со свойствами "ширина" и "высота". От этого класса
#унаследуйте классы "Прямоугольник" и "Квадрат". Для класса "Квадрат" переопределите методы,
#связанные с вычислением площади и периметра.

class Figure:
    def init(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Figure):
    pass

class Square(Figure):
    def init(self, side):
        super().init(side, side)
    def area(self):
        return self.width ** 2
    def perimeter(self):
        return 4 * self.width

s = Square(5)
print("Площадь квадрата:", s.area())
print("Периметр квадрата:", s.perimeter())