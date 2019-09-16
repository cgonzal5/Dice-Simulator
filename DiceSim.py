import random
print("My Dice Simulator")
play = "y"
min = 1
max = 20
roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the Dice!!!")
    print("The Die Shows...")
    print(random.randint(min,max))
    
    roll_again = input("Would you like to roll again?")