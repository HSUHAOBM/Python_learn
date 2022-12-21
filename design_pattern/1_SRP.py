# Single Responsibility Principle (SRP) 單一職責原則
# The single responsibility principle (SRP) states that every class, method, and function should have only one job or one reason to change.
    # Create high cohesive and robust classes, methods, and functions.
    # Promote class composition
    # Avoid code duplication


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'

    @classmethod
    def save(cls, person):
        print(f'Save the {person} to the database')


if __name__ == '__main__':
    p = Person('John Doe')
    Person.save(p)



# Person 類負責管理人員的屬性。
# PersonDB 類負責將人員存儲在數據庫中。


class PersonDB:
    def save(self, person):
        print(f'Save the {person} to the database')


class Person:
    def __init__(self, name):
        self.name = name
        self.db = PersonDB()

    def __repr__(self):
        return f'Person(name={self.name})'

    def save(self):
        self.db.save(person=self)


if __name__ == '__main__':
    p = Person('John Doe')
    p.save()