class NewStudent:
    def __init__(self, sid = 123, name="Tom"):
        self.id = sid
        self.name = name

    def display(self):
        return self.__id, self.name

    def displayall(self):
        return self.__id, self.name

    def __repr__(self):
        return 'Test.__repr__, with %s, id %s' %  (self.name, self.__id)
    def __str__(self):
        return 'Test.__str__, with %s, id %s' %  (self.name, self.__id)
    def __del__(self):
        print('Destructor called, Student table deleted.')

news1 = NewStudent()
print(repr(news1))
# Test.__repr__, with Tom, id 123
print(str(news1))
# Test.__str__, with Tom, id 123