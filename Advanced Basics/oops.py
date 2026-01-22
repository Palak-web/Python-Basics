class person:
    name = "Harry"
    occupation= "software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person()
b = person()

a.name = "Subhi"
a.occupation = "Accountant"

# print(a.name, a.occupation)


b.name = "Radhe"
b.occupation = "HR"

b.info()
