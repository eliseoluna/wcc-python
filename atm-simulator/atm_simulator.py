class BankAccount:
    def __init__(self):
        self.balance = 0.0  # initialize the account with $0.00

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Depositing {amount:.2f} into your account")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error! Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawing {amount:.2f} from your account")
            
def main():
    print("Welcome to your local ATM")
    account = BankAccount()
    
    while True:
        print("\nPress b to see your balance")
        print("Press w to make a withdraw")
        print("Press d to make a deposit")
        print("Press q to quit")

        choice = input("Choice [b,w,d,q]:").lower()

        if choice == 'b':
            print(f"Your balance is $  {account.get_balance():.2f}")
            
        elif choice == 'w':
            while True:
                amount_str = input("How much do you want to withdraw?: ")
                try:
                    amount = float(amount_str)
                    if amount <= 0:
                        print("Please enter an amount greater than 0")
                    elif amount > account.get_balance():
                        print("Error! Insufficient funds!")
                        break
                    else:
                        account.withdraw(amount)
                        break
                except ValueError:
                    print(f"{amount_str} cannot be converted to a number")
                    amount_str = input("Please enter in a valid amount:")
                    try:
                        amount = float(amount_str)
                        if amount <= 0:
                            print("Please enter an amount greater than 0")
                        elif amount > account.get_balance():
                            print("Error! Insufficient funds!")
                        else:
                            account.withdraw(amount)
                        break
                    except ValueError:
                        print("Invalid input again - returning to main menu.")
                        break
                    
        elif choice == 'd':
            while True:
                amount_str = input("How much do you want to deposit?: ")
                try:
                    amount = float(amount_str)
                    if amount <= 0:
                        print("Please enter an amount greater than 0")
                    else:
                        account.deposit(amount)
                        break
                except ValueError:
                    print(f"{amount_str} cannot be converted to a number")
                    amount_str = input("Please enter in a valid ammount:")
                    try:
                        amount = float(amount_str)
                        if amount <=0:
                            print("Please enter an amount greater than 0")
                        else:
                            account.deposit(amount)
                        break
                    except ValueError:
                        print("Invalid input again - returning to main menu.")
                        break
                    
        elif choice == 'q':
            print("Thank you.. Have a nice day!")
            break
        
        else:
            print(f"Error, invalid option '{choice}', please enter b,w,d or q")
            
if __name__ == "__main__":
    main()
