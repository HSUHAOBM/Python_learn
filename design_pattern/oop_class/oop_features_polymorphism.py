from abc import ABC, abstractmethod

# Python抽象方法(Abstract Method)
# 多型(Polymorphism)

class Pet(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def jumps(self):
        print("jump")

    def runs(self):
        print("run")

class Dog(Pet):
    def shout(self):
        print("my name is " + self.name + " bow-wow ")

class Cat(Pet):

    def shout(self):
        print("my name is " + self.name + " meow")

    def jumps(self):
        print('cat is jump')

# -------------------------------------------------------


# Python抽象方法(Abstract Method)
# pet = Pet('123')
# Error => 無法實體化含有抽象方法(Abstract Method)的抽象類別

mycat = Cat("May")
mycat.jumps()

mydog = Dog("Lucky")
mydog.jumps()
# Error => Cat 物件 必須要寫 jump()


# -------------------------------------------------------
# 多型 呼叫同名的方法,呈現不同結果
# ex 貓與狗 叫聲不同

# mycat.shout()
# mydog.shout()