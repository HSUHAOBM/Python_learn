'''
接口隔離原則 (Interface Segregation Principle)
是指一個實現應該只提供它真正使用的方法，而不是被強制依賴它不使用的接口。

這是通過限制客戶端對於那些他不需要的方法的依賴，來達到更高的封裝和更好的可重用性。
這樣可以降低接口的複雜性，使得代碼更容易實現和維護。
白話
物件只用它需要的,並不是全部

'''
# base
# 定義一個接口
class IWorker:
    def work(self):
        pass

# 定義一個實現該接口的工人類別
class Worker(IWorker):
    def work(self):
        print("I am a worker, I am working.")

# 定義一個客戶端類別
class Manager:
    def manage(self, worker):
        worker.work()

# 實例化實現接口的工人類別
worker = Worker()

# 實例化客戶端類別
manager = Manager()

# 使用客戶端類別管理工人類別
manager.manage(worker)

# 輸出結果：I am a worker, I am working.

'''
'''
class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError

# 接下來是不遵循接口隔離原則的示例
class MultiFunctionPrinter(Machine):
    def print(self, document):
        print(f'Printing document: {document}')

    def fax(self, document):
        print(f'Faxing document: {document}')

    def scan(self, document):
        print(f'Scanning document: {document}')

# 接下來是遵循接口隔離原則的示例 只用這個物件需要的
class OldFashionedPrinter(Machine):
    def print(self, document):
        print(f'Printing document: {document}')

class Photocopier(Machine):
    def print(self, document):
        print(f'Printing document: {document}')

    def scan(self, document):
        print(f'Scanning document: {document}')




'''
'''

# ex 2
class Document:
    def print(self):
        pass
    def fax(self):
        pass
    def scan(self):
        pass

# 簡易打印機 只用這個物件需要的
class SimplePrinter:
    def print(self, document):
        # 實作印表機的列印功能
        pass

# 多功能打印機 只用這個物件需要的
class MultiFunctionPrinter:
    def print(self, document):
        # 實作多功能印表機的列印功能
        pass
    def fax(self, document):
        # 實作多功能印表機的傳真功能
        pass
    def scan(self, document):
        # 實作多功能印表機的掃描功能
        pass


'''
# ex3
這裡有兩個接口：Engine 和 Vehicle，分別代表汽車和船的引擎和底盤。
而每一種引擎（ElectricEngine 和 PetrolEngine）都有自己的實作，
並且每一種載具（Car 和 Boat）都有將引擎實體化的方法。
'''
class Engine:
    def start(self):
        pass

class ElectricEngine(Engine):
    def start(self):
        print("Electric engine started")

class PetrolEngine(Engine):
    def start(self):
        print("Petrol engine started")

class Vehicle:
    def __init__(self, engine):
        self.engine = engine

class Car(Vehicle):
    def start(self):
        self.engine.start()

class Boat(Vehicle):
    def start(self):
        self.engine.start()

car = Car(ElectricEngine())
car.start() # Electric engine started

boat = Boat(PetrolEngine())
boat.start() # Petrol engine started