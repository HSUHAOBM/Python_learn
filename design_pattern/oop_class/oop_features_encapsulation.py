# 參考
# https://blog.twshop.asia/python%E8%88%87%E7%89%A9%E4%BB%B6%E5%B0%8E%E5%90%91%E4%B8%89%E5%A4%A7%E7%89%B9%E6%80%A7/
# https://www.learncodewithmike.com/2020/01/python-encapsulation.html

# 封裝 同一類或者同一物的資料與運算打包起來
# 設定部份屬性是否公開
# Python封裝(Encapsulation)
# 私有屬性(Private Attribute)
# 私有方法(Private Method)

# Python封裝(Encapsulation)
# ex Rectangle'sarea,perimeter 計算
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("area = ", self.length*self.width)

    def perimeter(self):
        print("perimeter = ", 2*(self.width+self.length))

# 私有屬性(Private Attribute) & # 私有方法(Private Method)
class NewStudent:
    def __init__(self, sid = 123, name="Tom"):
        # 私有屬性
        self.__id = sid
        self.name = name

    def display(self):
        return self.__id, self.name

    # 私有方法
    def __modify_name(self,new_name):
        self.name = new_name



# 私有屬性
# print(news1.name,news1.__id)
# # error
# print(news1.name,news1._NewStudent__id)
# # ok

fs = NewStudent()
# fs.__displayall()
# error

# print(fs._NewStudent.__displayall)
print(fs.__dict__)

fs._NewStudent__modify_name("Python")
print(fs.__dict__)
print(fs.name)

# -------------------------------------------------------

# # 繼承 父親的屬性
# # 多個類別的相似處設為一個基礎類別,
# # 各類別再針對個別特性從基礎類別去做延伸,
# class Pet:
#     def __init__(self, name):
#         self.name = name

#     def jumps(self):
#         print("jump")

#     def runs(self):
#         print("run")

# class Dog(Pet):
#     def shout(self):
#         print("my name is " + self.name + " bow-wow ")

# class Cat(Pet):
#     def shout(self):
#         print("my name is " + self.name + " meow")

# # -------------------------------------------------------

# # 多型 呼叫同名的方法,呈現不同結果
# # ex 貓與狗 叫聲不同
# mycat = Cat("May")
# mydog = Dog("Lucky")

# mycat.shout()
# mydog.shout()