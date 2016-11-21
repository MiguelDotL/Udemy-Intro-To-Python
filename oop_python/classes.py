class Employee:

    raise_percent = 1.04
    employee_count = 0

    def __init__(self, first_name, last_name, salary, company='company'):
        self.first_name = first_name
        self.last_name = last_name
        self.email = str(first_name + '.' + last_name + '@' + company + '.com').lower()
        self.salary = salary

        Employee.employee_count += 1

    def full_name(self):
        return self.first_name + ' ' + self.last_name
        # return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.salary = float(self.salary * self.raise_percent)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_percent = amount

    @classmethod
    def from_string(cls,empl_str):
        first_name, last_name, salary = empl_str.split('-')
        return cls(first_name, last_name, salary)

    @staticmethod
    def is_workday(day):
        return False if day.weekday() >= 5 else True



joe = Employee("Joe", "Schmoe", 55000, "compuserve")
bill = Employee("Bill", "Lumburgh", 155000, "inatek")

empl_str_1 = 'Jon-Doe-70000'
empl_str_2 = 'Mark-Sklar-90000'
empl_str_3 = 'Mr-Potato-40000'

print("--- MAKING A NEW EMPLOYEE --- ")
new_employee1 = Employee.from_string(empl_str_1)
print(new_employee1.first_name)

# joe.first_name   = "Joe"
# joe.last_name    = "Schmoe"
# joe.email       = "jschmoe69@compuserve.com"
# joe.salary      = 55000
#
# bill.first_name   = "Bill"
# bill.last_name    = "Lumburgh"
# bill.email       = "billyboy@inatek.com"
# bill.salary      = 155000

print(joe.email)
print(joe.full_name())
print(bill.email)


print(joe.__dict__)

Employee.set_raise_amount(1.05)

print(Employee.raise_percent)
print(joe.raise_percent)
print(bill.raise_percent)

joe.raise_percent = 1.06
print(joe.__dict__)



# ---- static methods ----

import datetime
my_date = datetime.date(2016, 7 ,10)

print('Today s a weekday:')
print (Employee.is_workday(my_date))
