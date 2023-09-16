class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount} into account {self.__account_number}")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount} from account {self.__account_number}")
        else:
            print("Withdrawal failed. Insufficient balance.")

    def display_balance(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self.__account_holder_name}")
        print(f"Account Balance: ${self.__account_balance}")


# Test the BankAccount class
if __name__ == "__main__":
    # Create an instance of BankAccount
    my_account = BankAccount("123456789", "John Doe", 1000)

    # Display initial balance
    my_account.display_balance()

    # Make a deposit
    my_account.deposit(500)

    # Display updated balance
    my_account.display_balance()

    # Make a withdrawal
    my_account.withdraw(200)

    # Display updated balance
    my_account.display_balance()

    # Attempt to withdraw more than the balance
    my_account.withdraw(10000)
  