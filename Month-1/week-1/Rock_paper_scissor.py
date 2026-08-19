import random
from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock, paper, scissors]


#User Side
user_move=int(input("Enter your choice 0 for rock , 1 for paper , 2 for scissors \n"))
print(f"so the user choose "+game_images[user_move])

#computer side
computer_move=random.randint(0,2)
print(f"computer choose ")
print(game_images[computer_move])


if user_move ==0 and computer_move==2:
    print("User wins")
elif computer_move > user_move:
    print("You Loose")
elif computer_move ==0 and  user_move ==2:
    print("User wins")
elif computer_move < user_move:
    print("user wins")
else:
    print("Draw")




