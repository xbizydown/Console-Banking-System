from db import create_table, add_account, get_account, update_balance
from utils import is_number, is_valid_account_number

create_table()


def create_account():
    account_number = input("Enter account number (10 digits): ")
    if not is_valid_account_number(account_number):
        print("Invalid account number. It must be 10 digits.")
        return

    name = input("Enter account holder's name: ")
    initial_balance = input("Enter initial balance: ")

    if not is_number(initial_balance):
        print("Invalid initial balance. Please enter a number.")
        return

    initial_balance = float(initial_balance)
    add_account(account_number, name, initial_balance)
    print("Account created successfully!")


def login_account():
    account_number = input("Enter account number: ")
    account = get_account(account_number)
    if account:
        print(f"Welcome, {account[1]}!")
        account_menu(account_number)
    else:
        print("Account not found.")


def account_menu(account_number):
    while True:
        print("\n1. Deposit money")
        print("2. Withdraw money")
        print("3. Check balance")
        print("4. Logout")

        choice = input("Choose an option: ")

        if choice == '1':
            deposit_money(account_number)
        elif choice == '2':
            withdraw_money(account_number)
        elif choice == '3':
            check_balance(account_number)
        elif choice == '4':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")


def deposit_money(account_number):
    amount = input("Enter amount to deposit: ")
    if not is_number(amount):
        print("Invalid amount. Please enter a number.")
        return

    amount = float(amount)
    account = get_account(account_number)
    new_balance = account[2] + amount
    update_balance(account_number, new_balance)
    print(f"Deposited {amount}. New balance: {new_balance}")


def withdraw_money(account_number):
    amount = input("Enter amount to withdraw: ")
    if not is_number(amount):
        print("Invalid amount. Please enter a number.")
        return

    amount = float(amount)
    account = get_account(account_number)

    if amount <= account[2]:
        new_balance = account[2] - amount
        update_balance(account_number, new_balance)
        print(f"Withdrew {amount}. New balance: {new_balance}")
    else:
        print("Insufficient funds.")


def check_balance(account_number):
    account = get_account(account_number)
    print(f"Current balance: {account[2]}")