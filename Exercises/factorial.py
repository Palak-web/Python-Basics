# Step 1: User se input lo
n = int(input("Enter your number: "))

# Step 2: Check karo num kisse less hai (ya kitne tak multiply karna)
# num se 1 tak jaana hai

# Step 3: Loop lagao aur 1 tak multiply karo
result = 1  # Empty variable jo change hoga

for i in range(n, 0, -1):  # num se 1 tak (reverse)

    print(f"Factorial: {result} x {i} =", end=" ")
    
    result = result*i # Multiply karte jao
    # Process repeat hoga until 1 na ho jaye

    # Step 4: Print
    print(f"{result}")
    
