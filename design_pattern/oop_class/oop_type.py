# class tpye
# StaticMethods、ClassMethods、AbstractMethods、property

# ===========================================================

# StaticMethods 靜態方法
# 可直接呼叫 ; add @staticmethod , not self
class People_StaticMethods:
    def __init__(self):
        pass

    def sleep(self, sleep_hour):
        print('Sleeping hours :', sleep_hour)

    @staticmethod
    def work(work_hour):
        print('Working hours :', work_hour)

m = People_StaticMethods()
m.sleep(3)
People_StaticMethods.work(4)
# Sleeping hours : 3
# Working hours : 4


# ClassMethods 類方法
# 可直接呼叫 ; add @classmethod , use cls
class People_ClassMethods:
    def __init__(self):
        pass

    def sleep(self, sleep_hour):
        print('Sleeping hours :', sleep_hour)

    @classmethod
    def work(cls, work_hour):
        print('Working hours :', work_hour)
        cls().sleep(6)
People_ClassMethods.work(5)
# Sleeping hours : 3
# Working hours : 4

# ===========================================================

# AbstractMethods 抽象方法
# 不能實例化 ,只能被繼承 ; add @abstractmethod ,被繼承都要有abstractmethod funtion

import abc

class Employee(abc.ABC):
    @abc.abstractmethod
    def work(self):
        return NotImplemented

class Andy(Employee):
    def work(self):
        print('work')


class Max(Employee):
    def sleep(self):
        print('sleep')


Andy().work()
# >>> work

Max().sleep()
# >>> Traceback (most recent call last):
#   File "/Users/max/Desktop/python_learning/methods.py", line 77, in <module>
#     Max().sleep()
# TypeError: Can't instantiate abstractclass Max with abstract methods work


# ===========================================================

# 封裝(Encapsulation) 不可改
class Product():
    @property
    def price(self):
        return 100
Product().price
Product().price = 150
# error AttributeError: can't set attribute