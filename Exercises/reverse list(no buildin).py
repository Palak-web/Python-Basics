inpu = input("Enter the numbers: ").split()

for i in range(len(inpu)):
    inpu[i] = int(inpu[i])

rev_inpu = []
for i in range(len(inpu)-1, -1, -1):
    rev_inpu.append(inpu[i])

print("Reversed:", rev_inpu)