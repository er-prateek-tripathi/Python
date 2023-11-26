class Atm:

    # init is a special method whose contents gets executed
    # as soon as the class's object is created

    def __init__(self):  # constructor
        self.pin = "000"  # default value
        self.balance = 0

        self.menu()

    def menu(self):

        while self.check_pin():

            user_input = input("""
Hello,
    
How would you like to proceed?
    
1. Enter 1 to create PIN.
2. Enter 2 to make a Deposit.
3. Enter 3 to Withdraw.
4. Enter 4 to Check Balance.
5. Enter 5 to Exit.
: """)

            if user_input == '1':
                self.create_pin()
            elif user_input == '2':
                self.deposit()
            elif user_input == '3':
                self.withdrawal()
            elif user_input == '4':
                self.check_balance()
            elif user_input == '5':
                print("Bye!!")
                break
            else:
                print("Invalid!!")

    def create_pin(self):
        self.pin = input("Enter your PIN: ")
        print("PIN set Successfully!!")

    def deposit(self):

        if self.check_pin():
            amount = int(input("Enter the amount: "))
            self.balance = self.balance + amount
            print("Deposited Successfully.")
        else:
            print("Wrong PIN!!")

    def withdrawal(self):

        if self.check_pin():
            amount = int(input("Enter the Withdrawal Amount: "))
            if amount < self.balance:
                self.balance = self.balance - amount
                print("Amount Withdrawn: ", amount)
            else:
                print("Insufficient Account Balance.")
        else:
            print("Invalid PIN!!")

    def check_balance(self):

        if self.check_pin():
            print("Account Balance: ", self.balance)
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
