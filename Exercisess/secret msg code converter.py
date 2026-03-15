"""Write a python program to translate a message into secret codes language.
Use the rules below to translate normal english Into secret code language"""

"""Coding rules:
if
 the word contains at least 3 characters, remove the first letter and append it at the end
 now open 3 random characters at the starting and the end.
else
 As simply reverse, the string 
decoding rules:
 If 
the word contains <3 characters reverse, it
 else
remove 3 random characters from starting and end. Now remove the last letter and  Append it to the beginning.
You program should ask whenever you want to code or Decode"""

import random
import string
def coding(message):
    words = message.split()
    coded_words = []

    for word in words:
        if len(word)<3:
            coded_word = word[::-1]
            
        else:
            new_word = word[1:] + word[0]
            random_start=''.join(random.choice(string.ascii_lowercase) for _ in range(3))
            random_end = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
            coded_word = random_start+ new_word +random_end
        coded_words.append(coded_word)
    return' '.join(coded_words)

def decoding(message):
    original_words = message.split()
    decoded_words= []
    for word in original_words:
        if len(word)<3:
            decoded_word = word[::-1]
        else:
            word = word[3:]
            word = word[:-3]
            decoded_word = word[-1] + word[:-1]
        decoded_words.append(decoded_word)
    return' '.join(decoded_words)


while True:
    print("What you wants to do")
    print("1.Code - Message ko secret code mein convert karo")
    print("2.Decode - Secret code ko normal message mein convert karo")
    print("Exit -Program band karo")
    choice = input("apni choice enter kariye (1/2/3): ")
    if choice == "1":
        message = input("Write your message please: ")
        coded_msg = coding(message)
        print(f"Apka coded message : {coded_msg}")
    elif choice == "2":
        message = input("Write your coded message: ")
        decoded_msg = decoding(message)
        print(f"Apka decoded message : {decoded_msg}")
    elif choice == "3" :
        ans= input("Are you really want to exit?(Yes/No)")
        if ans =="Yes":
            print("Okay byee👋")
        else:
            print("Okayy continue please...")
    else:
        print("You choose wrong options! please choose :1 , 2 or 3")