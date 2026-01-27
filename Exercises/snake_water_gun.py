import random

matrix = [
    ['D', 'W', 'L'],  # Snake row
    ['L', 'D', 'W'],  # Water row
    ['W', 'L', 'D']   # Gun row
]
# Access: matrix[row][col]

choice_to_index = {'S': 0, 'W': 1, 'G': 2}
index_to_choice = {0: 'S', 1: 'W', 2: 'G'}

player = input("Enter S/W/G: ").upper()
if player not in choice_to_index:
    print("Invalid choice!")
else:
    player_index = choice_to_index[player]  #is line ka matlab pata karna hai mereko
    computer_index = random.randint(0, 2)
    result = matrix[computer_index][player_index]
    print(f"Computer chose: {index_to_choice[computer_index]}")
    print(f"You chose: {player}")
    if result == 'W':
        print("Computer wins!")
    elif result == 'L':
        print("You win!")
    else:
        print("Draw!")




