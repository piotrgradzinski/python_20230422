"""
Implement an Employee class that allows you to record working time
and paying wages based on a preset hourly rate.

UML class diagram: https://yuml.me/70e8bff8.png
"""


class Employee:
    def __init__(self, first_name: str, last_name: str, rate: float):
        self.first_name = first_name
        self.last_name = last_name
        self.rate = rate
        self.work_time = 0

    def register_time(self, hours: int):
        self.work_time += hours

    def pay_salary(self) -> float:
        salary = self.work_time * self.rate
        self.work_time = 0
        return salary


employee = Employee(first_name='Jan', last_name='Nowak', rate=100.0)
employee.register_time(5)
employee.register_time(8)
employee.register_time(2)
salary = employee.pay_salary()
print(salary)  # 1 500
