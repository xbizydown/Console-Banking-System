from bank import create_account, login_account

def main():
    try:
        while True:
            print("\nWelcome to the Console Banking System")
            print("1. Create an account")
            print("2. Login to your account")
            print("3. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                create_account()
            elif choice == '2':
                login_account()
            elif choice == '3':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nExiting the system. Goodbye!")

if __name__ == "__main__":
    main()