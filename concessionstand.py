# concession stand program

menu = {
    "pizza" :3.00,
    "machos" : 4.50,
    "popcorn" : 6.00,
    "fries" : 2.50,
    "chips" : 1.00,
    "pretzel" : 3.50,
    "soda" :3.00,
    "lemonade" : 4.25
}

# keep track of the user's selected items
cart = []

total = 0

print("____________MENU________________")
for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")
print("__________________________________")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
# print(cart)        


print("_________YOUR ORDER__________")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")