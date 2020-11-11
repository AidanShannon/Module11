"""
Author: Aidan Shannon
Program: SalariedEmployee.py

takes Employee inherited class and creates its own class with display
"""
from inheritance.Employee import Employee
from datetime import date


class HourlyEmployee(Employee):
    def __init__(self, lname, fname, start_date, salary):
        super().__init__(lname, fname)
        self.start_date = start_date
        self.salary = salary

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, int):
            raise ValueError("Not a valid int value.")
        self._salary = value

    def give_raise(self, value):
        if value <= self.salary:
            raise ValueError("Salary needs to be greater than current pay rate!")
        self.salary = value

    def display(self):
        return Employee.display(self) + ", " + str(self.start_date) + ", $" + str(self.salary)


# Driver
try:
    h_employee = HourlyEmployee("Shannon", "Aidan", date.today(), 40000)
    print(h_employee.display())
    h_employee.give_raise(45000)
    print(h_employee.display())
except ValueError as err:
    print(err)
finally:
    print(h_employee.display())
    del h_employee
