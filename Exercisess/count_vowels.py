sent = (input("Enter any Santence or word: "))
count = 0
for ch in sent:
    if ch in "aeiouAEIOU":
        count += 1
print(count, "Number of vowels")