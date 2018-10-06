class Employee:

    raise_amt = 1.04

    # This is the common initialization method, so we can implicitly initialize an employee object by calling Employee('Corey', 'Schafer', 50000)
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # We define a method that prints out what we would use to initialize our employee object, i.e. returns something like Employee('Corey', 'Schafer', 50000)
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    # We define a method that does what we want to do when we print out the employee. This is the user friendly version of __repr__
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    # We define a method that does what we want + to do for our employee class. In this case it returns the combination of the salaries
    def __add__(self, other):
        return self.pay + other.pay

    # We defined a method that does what we want a length method to do for our employee class. In this case it returns the length of the fullname
    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1 + emp_2)

print(emp_1)
print(emp_1.__str__())

print(emp_1.__repr__())

print(len(emp_1))
