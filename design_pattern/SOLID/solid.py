#s 單一職責

class User():
    def __init__(self, name='No setting'):
        self.name = name
    def show_level(self):
        pass
class UserDB:
    def save(self,user):
        print('把',user.name,'存進DB')


# Ian = User('Ian5')
# DB = UserDB()
# DB.save(Ian)

# 開放封閉
class UserMin(User):
    def show_level(self):
        print('Min level')


class UserMax(User):
    def show_level(self):
        print('Man level')

#里式替換

class Rectangle():
    def __init__(self, hight=None, weight=None):
        self.hight = hight
        self.weight = weight

    def area(self):
        area = self.hight * self.weight
        return area

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

box = Square(8)
box1 = Rectangle(8,8)
print(box.area())
print(box1.area())

# 接口封閉

class Doc():
    def take():
        pass
    def read():
        pass
    def infomation():
        pass

class Man():
    def read_doc(self,doc):
        doc.read()
    def take_doc(self,doc):
        doc.take()


# D 反轉依賴
# 應由 抽象模組衍伸