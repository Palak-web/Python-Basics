'''kbc_ques = [ "Mahatma Gadhi ka janm kab hua tha ?\n","Bharat ke samudri raste ki khoj kisne ki thi?\n",]
option =["A.1859, B.1869\n,C.1887, D.1889" , "A. Kolambus, B.vasko-de-gama \n,C. max , D. tomus moor"]
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
            if answer== "A. Kolambus" or answer== "A." or answer== "option A" or answer == "a":
                print("Your answer is Right")
                print( "price win:",p1 + p1)
                break
            else:
                print("your answer is wrong")
                break'''


# KBC Style Quiz Game

# Questions list
kbc_ques = [
    "Mahatma Gandhi ka janm kab hua tha?",
    "Bharat ke samudri raste ki khoj kisne ki thi?"
]

# Options list (same index as questions)
options = [
    ["A. 1859", "B. 1869", "C. 1887", "D. 1889"],
    ["A. Kolambus", "B. Vasco-de-Gama", "C. Max", "D. Tomus Moor"]
]

# Correct answers list (store only option letter for simplicity)
correct_answers = ["B", "B"]

# Prize money for each question
prizes = [10000, 20000]

# Total winnings
total_amount = 0

print("🎉 Welcome to KBC 🎉\n")

# Loop through all questions
for i in range(len(kbc_ques)):
    print(f"Q{i+1}: {kbc_ques[i]}")
    for opt in options[i]:
        print(opt)
    
    # User answer input
    ans = input("Enter your answer (A/B/C/D): ").strip().upper()
    
    if ans == correct_answers[i]:
        print("✅ Correct Answer!")
        total_amount += prizes[i]
        print(f"You won ₹{prizes[i]} for this question.\n")
    else:
        print("❌ Wrong Answer!")
        print("Game Over!\n")
        break

print(f"🎁 Final Amount you take home: ₹{total_amount}")