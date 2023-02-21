'''
# 里氏替换原則 (Liskov Substitution Principle, LSP)
# 即為 "子類別應可以替換父類別"。
# 這個原則要求程式中的類別關係要符合一個重要的性質，
# 就是在使用父類別的地方都可以替換成它的子類別，
# 而不會影響整體程式的正確性。


在這個範例中，我們定義了一個父類別 Rectangle 和一個子類別 Square。
Square 繼承了 Rectangle，但因為他的邊長都相等，
所以我們定義了一個特殊的 __init__ 方法使得實體化的時候更方便。
最後我們在 process_shapes 函數中把一組形狀處理，
因為這個函數是基於 Rectangle 類別寫的，
所以我們可以用 Square 類別的實例來替換 Rectangle 類別的實例，而不影響程式的正確性。
'''

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

def process_shapes(shapes):
    total_area = 0
    for shape in shapes:
        total_area += shape.area()
    return total_area


# shapes = [Rectangle(2, 3), Rectangle (2,2), Rectangle (3,3), Rectangle(2, 4)] =>
# shapes = [Rectangle(2, 3), Square(2), Square(3), Rectangle(2, 4)]
result = process_shapes(shapes)
print(result)


# =============================================
# 遵守
class Animal:
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        print('Meow')

class Dog(Animal):
    def make_sound(self):
        print('Woof')


def make_animal_sounds(animal):
    animal.make_sound()

make_animal_sounds(Cat()) # 输出 Meow
make_animal_sounds(Dog()) # 输出 Woof

# 沒遵守

class Animal:
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        print('Meow')

class Dog(Animal):
    def make_sound(self):
        print('Woof')

class RobotDog(Dog):
    def make_sound(self):
        print('Beep')

dog = Dog()
robot_dog = RobotDog()

dog.make_sound()       # prints 'Woof'
robot_dog.make_sound() # prints 'Beep'

'''
在這個例子中，RobotDog 繼承自 Dog，而 Dog 又繼承自 Animal，
所以 RobotDog 也被視為是 Animal 的子類別。
但是，RobotDog 中的 make_sound 方法的行為與其父類別 Dog 中的 make_sound 方法不同，
這違反了 LSP 原則。當應用程序在需要使用 Dog 或 Animal 的地方使用 RobotDog 時，
它可能會無法正確地工作，因為 RobotDog 的行為與期望的不同。
'''