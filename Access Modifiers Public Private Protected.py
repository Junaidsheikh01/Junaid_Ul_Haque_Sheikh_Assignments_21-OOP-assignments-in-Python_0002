class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name            # Public
        self._salary = salary       # Protected
        self.__ssn = ssn            # Private

e = Employee("John", 50000, "123-45-6789")
print(e.name)           # Accessible
print(e._salary)        # Accessible (not recommended)
# print(e.__ssn)        # Error
print(e._Employee__ssn) # Accessing private using name mangling
