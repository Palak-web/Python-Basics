with open('writefile.txt','r') as f:
    print(type(f))
    #move to the tenth byte in the file
    f.seek(54)

    # Read the next 5 bytes
    print(f.tell())
    data = f.read(6)
    print(data)


with open('sample.txt','w') as f:
    f.write('hello world!')
    f.truncate(5)
    

with open('writefile.txt','r') as f:
    print(f.read())