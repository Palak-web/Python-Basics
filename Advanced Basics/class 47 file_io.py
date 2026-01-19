#READING A FILE
# f = open('myfile.txt','r')  # 'r' For reading only file if it will not exsiting it wil give error
# #print(f)
# text = f.read()
# print(text)
# f.close()

#WRITING A FILE
# l = open('myfile2.txt','w')
# l.write("hello, word!")
# l.close()

# APPENDING IN A FILE
# l = open('myfile2.txt','a')
# l.write("hello, word!")
# l.close()

with open('myfile2.txt','a')as l:
    l.write(" hey I am inside with")