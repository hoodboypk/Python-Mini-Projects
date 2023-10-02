print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("*********** Welcome to Treasure Island Adventure! ***********")

print("You have to reach the treasure island in order to find the treasure")

direction = input("You're at a crossroad. Which way would you go? 'left' or 'right'? : ")
if(direction == 'left'):
    move = input("You've reached the shore. Do you want to 'wait' for the boat or 'swim'? : ")
    if(move == 'wait'):
        door = input("You reached the island. There are 3 doors. Which one would you open? 'red', 'yellow', 'green' : ")
        if(door == 'yellow'):
            print("Congratulations, you found the Treasure!")
        else:
            print("Wrong door. You died.")
    else:
        print("You tried to swim but got eaten by a shark.")
else:
    print("Oops, you took a wrong turn and and got hit by a car.")    

print("Game Over! Thanks for playing.")