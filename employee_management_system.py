
class Employee:
    def __init__(self, employee_id, name, position , salary):
        self.employee_id = employee_id
        self.name = name 
        self.position = position 
        self.salary = salary 

    def display_employee_details(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, employee_id, name, position, salary, department):
        super().__init__(employee_id, name, position, salary)
        self.department = department

    def display_manager_details(self):
        self.display_employee_details()
        print(f"Department: {self.department}")


class Developer(Employee):
    def __init__(self, employee_id, name, position, salary, programming_language):
        super().__init__(employee_id, name, position, salary)
        self.programming_language = programming_language

    def display_developer_details(self):
        self.display_employee_details()
        print(f"Programming Language: {self.programming_language}")


class Designer(Employee):
    def __init__(self, employee_id, name, position, salary, design_tool):
        super().__init__(employee_id, name, position, salary)
        self.design_tool = design_tool

    def display_designer_details(self):
        self.display_employee_details()
        print(f"Design Tool: {self.design_tool}")



manager = Manager(1, "Alice", "Manager", 80000, "Sales")
developer = Developer(2, "Bob", "Developer", 60000, "Python")
designer = Designer(3, "Charlie", "Designer", 50000, "Adobe Photoshop")

manager.display_manager_details()
developer.display_developer_details()
designer.display_designer_details()
