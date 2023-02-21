'''
開放封閉原則 (Open-Closed Principle)

系統的設計符合開放封閉原則，當我們需要新增功能時，只需要增加新的程式碼即可，
不需要修改現有的程式碼，這樣就可以保持原有的程式碼的穩定性，同時也可以提高軟體的可擴展性和可維護性。

如果需要增加新功能，不應更改已有代碼。所以，在以下範例這種情況下，您不應該修改class Shape類，
而是應該在其他地方添加新的類別或模塊來擴展代碼。這可以使程序的可維護性和可擴展性更高。
'''

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# 新增類別 Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height



