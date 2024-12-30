#calculator app
operator = input("Enter an operator (+ - * /): ")

# typecast the input into their respective values to do mathematics
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

# check the user input operator
if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print(f"{operator} operator is not valid")