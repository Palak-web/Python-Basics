import random

matrix = [
    ['D', 'W', 'L'],  # Snake row
    ['L', 'D', 'W'],  # Water row
    ['W', 'L', 'D']   # Gun row
]

index_to_choice = {0:"S", 1:"W", 2:"G"}
choice_to_index = {"S":0, "W":1,"G":2}

player = input("Enter The choice S/W/G: ").upper()

if player not in choice_to_index:
    print("Invaild Input")

else:
    player_choice = choice_to_index[player]
    computer = random.randint(0,2)
    comp_choice = index_to_choice[computer]

    result= matrix[player_choice][computer]  #access [row] [col]

    print(f"You have choosen: {player}")
    print(f"Agent choosen: {comp_choice}")

    if result == 'W':
        print("You win!!")

    elif result == 'L':
        print("Agent wins!!")

    else:
        print("draw")
