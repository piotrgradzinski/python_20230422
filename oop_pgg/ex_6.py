"""
Implement the `PremiumEmployee` class, which will be a derived class of `Employee`.
This class should also allow employee bonuses.

employee = PremiumEmployee('Jan', 'Nowak', 100.0)
employee.register_time(5)
employee.give_bonus(1000.0)
employee.pay_salary()
1500.0

Plan
- create a new class and inherits from Employee
- in new class, add bonus attribute in __init__ method
- add give_bonus method
- override pay_salary method to add bonus to the calculations
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


