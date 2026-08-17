
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
move=input("Where do you want to move \n")
if move == "right":
    print("Fall into a hole Game Over!")
elif move == "left":
    left=input("What do you want to choose swim or wait?\n")
    if left == "swim":
        print("Attacked by trout Game over!")
    elif left == "wait":
        print("You are sucessfully in your last step !")
        door = input("which door you want to choose?\n")
        if door== "red":
            print("Burned by fire Game over!")
        elif door=="blue":
            print("Eaten by beasts Game Over!")
        elif door=="yellow":
            print("you win!")
