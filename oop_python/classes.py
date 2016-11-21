class Employee:

    raisePercent = 1.04
    employeeCount = 0

    def __init__(self, firstName, lastName, salary, company='company'):
        self.firstName = firstName
        self.lastName = lastName
        self.email = str(firstName + '.' + lastName + '@' + company + '.com').lower()
        self.salary = salary

        Employee.employeeCount += 1

    def fullName(self):
        return self.firstName + ' ' + self.lastName
        # return '{} {}'.format(self.firstName, self.lastName)

    def applyRaise(self):
        self.salary = float(self.salary * self.raisePercent)


joe = Employee("Joe", "Schmoe", 55000, "compuserve")
bill = Employee("Bill", "Lumburgh", 155000, "inatek")

# joe.firstName   = "Joe"
# joe.lastName    = "Schmoe"
# joe.email       = "jschmoe69@compuserve.com"
# joe.salary      = 55000
#
# bill.firstName   = "Bill"
# bill.lastName    = "Lumburgh"
# bill.email       = "billyboy@inatek.com"
# bill.salary      = 155000

print(joe.email)
print(joe.fullName())
print(bill.email)


print(joe.__dict__)

print(Employee.raisePercent)
print(joe.raisePercent)
print(bill.raisePercent)

joe.raisePercent = 1.6
print(joe.__dict__)
