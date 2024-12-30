# validate user input
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")


if len(username) > 12:
    print("Your username cant be more than 12 characters")
elif not username.find(" ") == -1:
    # meaning the space was found
    print("Your username cant contain spaces")
elif not username.isalpha():
    print("Your username cant contain numbers")
else:
    print(f"Welcome {username}")