'''
依賴反轉原則（Dependency Inversion Principle，DIP）
。它提出高層模組不應該依賴於低層模組，兩者都應該依賴於抽象，
並且抽象應該不依賴於細節。换句话说，抽象應該依賴於實現，而實現應該不依賴於抽象。
'''

# 抽象類別
class AbstractDataSource:
    def read_data(self):
        pass

    def write_data(self, data):
        pass

# 低階模組
class FileDataSource(AbstractDataSource):
    def read_data(self):
        with open("file.txt", "r") as f:
            return f.read()

    def write_data(self, data):
        with open("file.txt", "w") as f:
            f.write(data)

# 高階模組
class DataProcessor:
    def __init__(self, data_source: AbstractDataSource):
        self.data_source = data_source

    def process_data(self):
        data = self.data_source.read_data()
        # 其他數據處理
        self.data_source.write_data(data)

# 客戶端代碼
data_source = FileDataSource()
processor = DataProcessor(data_source)
processor.process_data()