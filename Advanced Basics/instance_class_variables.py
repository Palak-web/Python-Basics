class Employee:
    companyName = 'Apple'  #Class Variables
    no_of_emp= 0
    def __init__(self, name):
        self.name = name
        self.raise_amt = 0.02
        Employee.no_of_emp +=1

    def showDetails(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.companyName} is {self.raise_amt}\n The number of employee: {self.no_of_emp}")
        

emp1 = Employee("Harry")
emp1.showDetails()

emp2 = Employee("Rohan")
emp2.companyName = "Nestle"  #Instance Variables
emp2.showDetails()

emp3 = Employee("Princy")
emp3.raise_amt = 0.05
emp3.companyName = "Google"
emp3.showDetails()  
