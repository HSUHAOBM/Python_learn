'''
Single-responsibility principle (SRP) = 單一職責原則
個類別(角色)應該只有一個對其責任的改變的原因。也就是說，一個類別應該只負責一項任務。
這樣可以使程式碼更容易理解、修改和維護，也更容易進行單元測試和模組化開發。
如果一個類別或模組負責太多不同的功能，那麼它的耦合度會變得非常高，而且很難擴展和重用。
'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class EmployeeDB:
    def __init__(self):
        self.employees = []

    def fetch_employees(self):
        # Connect to the database and retrieve the employee data
        conn = psycopg2.connect(
            host="localhost",
            database="employeedb",
            user="user",
            password="password"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()
        return employees

    def add_employee(self, employee):
        # Connect to the database and insert the employee data
        conn = psycopg2.connect(
            host="localhost",
            database="employeedb",
            user="user",
            password="password"
        )
        cursor = conn.cursor()
        cursor.execute("INSERT INTO employees (name, salary) VALUES (%s, %s)", (employee.name, employee.salary))
        conn.commit()
        print("Employee added to the database: ", employee.name)

# 使用範例
# 讀取員工信息
employee_db = EmployeeDB()
employee_data = employee_db.fetch_employees()
for data in employee_data:
    employee = Employee(data['name'], data['salary'])
    # do something with the employee object

# 新增員工
employee_db = EmployeeDB()
employee = Employee("John Doe", 1000)
employee_db.add_employee(employee)