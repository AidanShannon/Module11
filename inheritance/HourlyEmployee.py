"""
Author: Aidan Shannon
Program: HourlyEmployee.py

takes Employee inherited class and creates its own class with display
"""
from inheritance.Employee import Employee
from datetime import date


class HourlyEmployee(Employee):
    def __init__(self, lname, fname, start_date, hourly_pay):
        super().__init__(lname, fname)
        self.start_date = start_date
        self.hourly_pay = hourly_pay

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @property
    def hourly_pay(self):
        return self._hourly_pay

    @hourly_pay.setter
    def hourly_pay(self, value):
        if not isinstance(value, float):
            raise ValueError("Not a valid float value.")
        self._hourly_pay = value

    def give_raise(self, value):
        if value <= self.hourly_pay:
            raise ValueError("Pay rate needs to be greater than current pay rate!")
        self.hourly_pay = value

    def display(self):
        return Employee.display(self) + ", " + str(self.start_date) + ", $" + str(self.hourly_pay) + "/hr"


# Driver
try:
    h_employee = HourlyEmployee("Shannon", "Aidan", date.today(), 10.00)
    print(h_employee.display())
    h_employee.give_raise(9.00)
    print(h_employee.display())
except ValueError as err:
    print(err)
finally:
    print(h_employee.display())
    del h_employee
