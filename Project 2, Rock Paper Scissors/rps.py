"""
1 = rock
2 = paper
3 = scissor
"""
import random
computer = random.choice([1, 2, 3])
choice = input("Enter your choice: ")
youDict = {"r": 1, "p": 2, "s": 3}
reverseDict = {1: "Rock", 2: "Paper", 3: "Scissor"}

you = youDict[choice]
print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a draw, try again!")
    # we gonna write a nested for loop
else:
    if(computer ==1 and you == 2):
        print("you win")
    elif(computer == 1 and you == 3):
        print("you lose")
    elif(computer ==2 and you == 1):
        print("you lose")
    elif(computer ==2 and you == 3):
        print("you win")
    elif(computer ==3 and you == 1):
        print("you win")
    elif(computer ==3 and you == 2):
        print("you lose")
    else:
        print("Error")
