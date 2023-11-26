class Atm:  # This defines a class called 'Atm'
    # The 'Atm' class is like a blueprint for creating ATM objects.
    # Each ATM object will have its own pin and balance attributes.

    def __init__(self):  # This is the constructor method.
        # It is called automatically when an ATM object is created.
        self.pin = "000"  # This sets the default PIN to "000".
        self.balance = 0  # This sets the initial balance to 0.

        self.menu()  # This calls the 'menu' method to start the ATM program.

    def menu(self):  # This method displays the ATM menu and handles user input.

        while True:  # This infinite loop keeps the ATM program running until the user exits.
            if self.check_pin():  # This checks if the user entered the correct PIN.
                user_input = input("""
                Hello,

                How would you like to proceed?

                1. Enter 1 to create PIN.
                2. Enter 2 to make a Deposit.
                3. Enter 3 to Withdraw.
                4. Enter 4 to Check Balance.
                5. Enter 5 to Exit.
                : """)

                # This if-elif-else block handles the user's menu selection.
                if user_input == '1':
                    self.create_pin()  # This calls the 'create_pin' method to change the PIN.
                elif user_input == '2':
                    self.deposit()  # This calls the 'deposit' method to make a deposit.
                elif user_input == '3':
                    self.withdrawal()  # This calls the 'withdrawal' method to make a withdrawal.
                elif user_input == '4':
                    self.check_balance()  # This calls the 'check_balance' method to check the balance.
                elif user_input == '5':
                    print("Bye!!")  # This exits the program.
                    break  # This breaks out of the infinite loop.
                else:
                    print("Invalid!!")  # This prompts the user to enter a valid option.
            else:
                # This prompts the user to restart the program if they enter the wrong PIN.
                print("Invalid PIN!!")
                print("Restart")
                exit()

    def create_pin(self):  # This method allows the user to change their PIN.

        self.pin = input("Enter your PIN: ")  # This prompts the user to enter a new PIN.
        print("PIN set Successfully!!")  # This confirms that the PIN has been changed.

    def deposit(self):  # This method allows the user to make a deposit.

        if self.check_pin():  # This checks if the user entered the correct PIN.
            amount = int(input("Enter the amount: "))  # This prompts the user to enter the deposit amount.
            self.balance = self.balance + amount  # This adds the deposit amount to the balance.
            print("Deposited Successfully.")  # This confirms that the deposit has been made.
        else:
            print("Wrong PIN!!")  # This prompts the user to enter the correct PIN.

    def withdrawal(self):  # This method allows the user to make a withdrawal.

        if self.check_pin():  # This checks if the user entered the correct PIN.
            amount = int(input("Enter the Withdrawal Amount: "))  # This prompts the user to enter the withdrawal
            # amount.

            if amount < self.balance:  # This checks if the withdrawal amount is less than the balance.
                self.balance = self.balance - amount  # This deducts the withdrawal amount from the balance.
                print("Amount Withdrawn: ", amount)  # This confirms that the withdrawal has been made.
            else:
                print("Insufficient Account Balance.")  # This prompts the user if the withdrawal amount exceeds the
                # balance.
        else:
            print("Invalid PIN!!")  # This prompts the user to enter the correct PIN.

    def check_balance(self):  # This method displays the user's current account balance.

        if self.check_pin():  # This checks if the user entered the correct PIN.
            print("Account Balance: ", self.balance)  # This displays the user's account balance.
        else:
            print("Invalid PIN!!")

    def check_pin(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            flag = True
        else:
            print("Invalid PIN!!")
            print("Restart")
            exit()
        return flag


pnb = Atm()
