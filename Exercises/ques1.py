"""Write a function that takes a full name as input 
from the user and returns its initials in capital 
letters separated by dot.

Example:
Input:  "riya sharma"
Output: "R.S."

Input:  "john doe"
Output: 'J.D.'"""

# Step 1: User se naam lo
name = input("Apna naam likho: ")

# Step 2: Split karo
words = name.split()

# Step 3: Har word ka pehla letter lo + uppercase karo
initials = ""
for word in words:
    initials += word[0].upper() + "."

# Step 4: Print karo
print(initials)