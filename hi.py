#bank program

def show_balance(balance):
    print(f"your balance is ${balance:.4f}")

def deposit(balance):
    amount = float(input("enter a amount to  be deposited: "))

    if amount<0:
        print("enter a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("enter amount to be withdrawn: "))

    if amount > balance:
        print("insufficent balance")
        return 0
    elif amount < 0:
        print("amount must be grater than 0")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True
    while is_running:
        print("######################")
        print("banking program")
        print("######################")

        print("1.show_balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.Exit")

        print("#######################")

        choice = input("enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)

        elif choice == '2':
            balance+=deposit(balance)

        elif choice == '3':
            balance-=withdraw(balance)

        elif choice == '4':
            is_running = False

        else:
            print("that is not a valid choice")
    print("Thank you ,have a nice day")


if __name__ == "__main__":
    main()