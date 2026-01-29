class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of the empolyee: {self.id} is {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print("the defult language is Python")

e1 = Employee("rohan das", 420)
e1.showDetails()
e2 = Employee("kavya ", 421)
e2.showDetails()
e3 = Programmer("shiv ", 422)
e3.showDetails()
e3.showLanguage()