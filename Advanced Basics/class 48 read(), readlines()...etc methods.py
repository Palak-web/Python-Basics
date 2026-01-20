f =open('marksfile.txt','r')

while True:
    line = f.readline()
    print(line)
    if not line:
        print(line, type(line))
        break

f =open('marksfile.txt','r')
i = 0
while True:
    i = i+1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks of student {i} in chem is: {m1 * 1}")
    print(f"Marks of student {i} in physics is: {m2 *1}")
    print(f"Marks of student {i} in bio is: {m3*1}")
    print(line)

f = open('writefile.txt','w')
lines = ["line 1\n" , "line 2\n" , "line 3"]
f.writelines(lines)
f.close()