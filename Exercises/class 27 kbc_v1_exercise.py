kbc_ques = [ "Mahatma Gadhi ka janm kab hua tha ?\n","Bharat ke samudri raste ki khoj kisne ki thi?\n",]
option =["A.1859, B.1869\n,C.1887, D.1889" , "A. Kolambus, B.vasco-de-gama \n,C. max , D. tomus moor"]
p1 = 10000
ques_no = int(input("enter the question no:"))
if 1 <= ques_no <= len(kbc_ques):
    print (kbc_ques[ques_no -1], option[ques_no -1] )
else:
    print("Invalid ques")

for answer in kbc_ques:
     if 1 <= ques_no <= len(kbc_ques):
        if ques_no == 1:
            answer = input("enter the ans no: ")
            if answer== "B.1869" or answer== "B." or answer== "B" or answer == "b":
                print("Your answer is Right")
                print( "price win:",p1)
                
                break
            else:
                print("your answer is wrong")
                break
        if ques_no == 2:
            answer = input("enter the ans no: ")
            if answer== "B. vasco-de-gama" or answer== "B." or answer== "option B" or answer == "b":
                print("Your answer is Right")
                print( "price win:",p1 + p1)
                break
            else:
                print("your answer is wrong")
                break
