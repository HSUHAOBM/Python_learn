# 參考

# 繼承 父親的屬性
# 多個類別的相似處設為一個基礎類別,
# 各類別再針對個別特性從基礎類別去做延伸,
class Pet:
    def __init__(self, name):
        self.name = name

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

    # 方法複寫
    def runs(self):
        print("cat run")
    # 方法繼承
    def jumps(self):
        super().jumps()
        print("this is cat jump")

# -------------------------------------------------------

mycat = Cat("May")
mydog = Dog("Lucky")

mycat.runs()
mycat.jumps()

print("------------------------------------")

# -------------------------------------------------------#
#
# 多層繼承(Multi-Level Inheritance)
# 動物類別
class Animal:
    pass
# 鳥類類別
class Bird(Animal):
    # 飛行方法
    def fly(self):
        print("fly")
# 鴨子類別
class Duck(Bird):
    pass
duck = Duck()
duck.fly()

print("------------------------------------")

# -------------------------------------------------------#
# 多重繼承(Multiple Inheritance)

# 動物類別
class Animal:
    def eat(self):
        print("Animal eat method is called.")
# 鳥類類別
class Bird:
    def eat(self):
        print("Bird fly method is called.")
# 鴨子類別
class Duck(Animal, Bird):
    pass
duck = Duck()
duck.eat()