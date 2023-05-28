"""
Implement an Employee class that allows you to record working time
and paying wages based on a preset hourly rate.

UML class diagram: https://yuml.me/70e8bff8.png
"""

class Employee:
    pass


employee = Employee(first_name='Jan', last_name='Nowak', rate=100.0)
employee.register_time(5)
employee.register_time(8)
employee.register_time(2)
salary = employee.pay_salary()
print(salary)  # 1 500
