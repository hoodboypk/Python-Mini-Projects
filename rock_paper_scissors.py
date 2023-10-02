import random

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

player_lst = [rock,paper,scissors]

choose = int(input("What do you choos? Type 0 for Rock, 1 for Paper, 2 for Scissors:\n"))

if(choose == 0):
    print(rock)
elif(choose == 1):
    print(paper)
elif(choose == 2):
    print(scissors)

print("Computer Chose:")
print(random.choice(player_lst))

if(choose == random.choice(player_lst)):
    print("You won!")
else:
    print("You lost!")
