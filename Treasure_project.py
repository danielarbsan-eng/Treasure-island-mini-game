print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first_choice = input("You are escaping from some mercenaries and you reach "
                     "a dead end, are you going left or right ?\n").lower()
if first_choice == "right":
    print("You ran into a swamp full of crocs, Game Over!")
elif first_choice == "left":
    print("You reached the end of the cliffs")
    second_choice = input('Type "search" to try to look for '
                          'shelter in the island or type "jump" '
                          'to jump directly into the water\n').lower()
    if second_choice == "search":
        last_choice = input("You found a small village. "
                            "You spot a church, a shack and a barn\n "
                            "Type 'church' or ' shack' or 'barn' "
                            "to pick your shelter\n").lower()
        if last_choice == "church":
            print("The church is full of deadly spiders, Game over!")
        elif last_choice == "shack":
            print("You found shelter "
                  ",and in there you find a hidden treasure, You win!")
        elif last_choice == "barn":
            print("As soon as you opened the door "
                  "the structure collapsed, Game over!")
        else:
            print("Game over!")
    else:
        print("You hit a rock and died, Game over!")
else:
    print("Sorry, wrong input.")




