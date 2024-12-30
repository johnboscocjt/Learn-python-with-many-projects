# python banking program

# function to show the user the balance
def show_balance(balance):
    print("****************************")
    print(f"Your balance is ${balance:.2f}")
    print("****************************")
            
def deposit():
    print("****************************")
    amount = float(input("Enter an amount to be deposited: "))
    print("****************************")

    
    if amount < 0:
        print("****************************")
        print("Thats not a valid amount")
        print("****************************")
        return 0
    else:
        return amount;
    
def withdraw(balance):
    print("****************************")
    amount = float(input("Enter amount to be withdrawn: "))
    print("****************************")
    
    if amount > balance:
        print("****************************")
        print("Insufficient funds")
        print("****************************")
        
        # need to return something for program to work
        return 0
    elif amount < 0:
        print("****************************")
        print("Amount must be greater than 0")
        print("****************************")
        
        return 0
    else:
        return amount


# main function of the code
def main():
    # these variables are enclosed in this local scope, cant be accessed outside
    balance = 0

    # when is_running is set to be False we will exit the program
    is_running = True

    while is_running:
        print("****************************")
        print("   Banking program   ")
        print("****************************")

        
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        print("****************************")

        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)    
        elif choice == '4':
            # exit the loop by setting is_running false
            is_running = False
        else:
            print("****************************")
            print("That is not a valid choice")
            print("****************************")
          
    print("****************************")        
    print("Thank you!, have a nice day")
    print("****************************")

    
    
# call the main function to run it
# that means  the program can be imported, using if __
# if we are running this program directly execute the main function
if __name__ == '__main__':
    main()