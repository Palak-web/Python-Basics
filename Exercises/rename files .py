import os

folder_path = r"C:\Users\HP\OneDrive\Pictures\Screenshots"
png_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
png_files.sort()

print(f"total {len(png_files)} PNG files hain")  

counter = 1

for old_name in png_files:
    old_path = os.path.join(folder_path, old_name)
    new_name = f"{counter}.png"
    new_path = os.path.join(folder_path, new_name)

    os.rename(old_path, new_path)
    
    print(f"{old_name} --> {new_name}")
    counter += 1

print(f"\n total {counter - 1 } files rename ho gayi")
