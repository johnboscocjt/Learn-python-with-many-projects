import random

# creating asciiate by utilizing unicode characters
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# output
# ● ┌ ─ ┐ │ └ ┘


# create some die, each die will be made up fo five lines
"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"




# create the dice dictionary, key-value pair,value will be a tuple made up of strings
dice_art = {
    1: ("┌─────────┐", 
        "│         │", 
        "│    ●    │", 
        "│         │", 
        "└─────────┘"),
    
    2: ("┌─────────┐", 
        "│ ●       │", 
        "│         │", 
        "│       ● │", 
        "└─────────┘"),
    
    3: ("┌─────────┐", 
        "│ ●       │", 
        "│    ●    │", 
        "│       ● │", 
        "└─────────┘"),
    
    4: ("┌─────────┐", 
        "│ ●     ● │", 
        "│         │", 
        "│ ●     ● │", 
        "└─────────┘"),
    
    5: ("┌─────────┐", 
        "│ ●     ● │", 
        "│    ●    │", 
        "│ ●     ● │", 
        "└─────────┘"),
    
    6: ("┌─────────┐", 
        "│ ●     ● │", 
        "│ ●     ● │", 
        "│ ●     ● │", 
        "└─────────┘")
}


# list of dice
dice = []

total = 0

num_of_dice = int(input("How many dice?: "))


for die in range(num_of_dice):
    # append the number to the dice
    dice.append(random.randint(1,6))
# print(dice)


# in charge for die
# for die in range(num_of_dice):
#     # in charge of prnting every tuple
#     for line in dice_art.get(dice[die]):
#         print(line)
    
# printing the dice horizontally
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()
    
    
    
    
    
for die in dice:
    total += die
print(f"Total: {total}")