
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def work(self):
      pass 

    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self._salary = salary

    def display_employee_details(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: {self._salary}")

    def get_salary(self):
        return self._salary

    def increase_salary(self, amount):
       self._salary += amount
       return self._salary

class Developer(Employee):
    def __init__(self, employee_id, name, position, salary, programming_language):
        super().__init__(employee_id, name, position, salary)
        self.programming_language = programming_language

    
    def work(self):
        print(f"{self.name} is writing code in {self.programming_language}")

class Manager(Employee):
    def __init__(self, employee_id, name, position , salary, team_size):
        super().__init__(employee_id, name, position, salary)
        self.team_size = team_size

    def work(self):
        print(f"{self.name} is managing a team of {self.team_size} members")

class Designer(Employee):
    def __init__(self, employee_id, name, position, salary, UI):
        super().__init__(employee_id, name, position, salary)
        self.UI = UI

    def work(self):
        print(f"{self.name} is designing {self.UI} for the application")


employees = [
    Developer(1, "vikas", "Developer", 80000, "Python"),
    Manager(2, "arvind", "Manager", 80000, 5),
    Designer(3, "pritam", "Designer", 50000, "UI/UX")
]

for employee in employees:
    employee.work()