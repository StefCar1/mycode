#!/usr/bin/env python3

# Define login screen for user.

yes = ["yes", "y", "correct"]
no = ["no", "n", "nah, dog!", "incorrect"]

def theloginscreen():
    print("   Welcome to Stefan's super cool project!\n      Please select an option below:")
    print("1. Enter Username.\n2. Create a user account.\n3. Exit.")

def accountcreation():
    usernamecount = 0
    while True:
        usernamecount = usernamecount + 1
        unacceptableentries = [str(i) for i in range(10)] + ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
        print("The username cannot contain numbers, symbols, or spaces. Please enter your preferred username here: ")
        newusername = input("")
        if any(item in newusername for item in unacceptableentries):
            print("The username contained a number, symbol, or space. Please try again.")
        elif any(item in newusername for item in unacceptableentries):
            print("That username is taken. Please try another.")
        elif usernamecount == 3:
            print("Please try again later")
        else:
            email = input("Enter your preferred email: ")
            emailverification = input(f'Is {email} correct? ') 
            if emailverification == yes:
                passwordcount = 0
                while true:
                    passwordcount = passwordcount + 1
                    password = input("Enter your preferred password: ")
                    if password == "":
                        print("You must enter a password.")
                    elif passwordcount == 3:
                        print("Please try again once you have decided on a password.\n Goodbye!") 
                    else:
                        password2 = input("Re-enter your password: ")
                        if password == password2:
                            print("You're account was successfully created!")
                            with open(accounts.txt, "a") as accounts:
                                accounts.write(newusername + "x" + email + "x" + password2)
                        else:
                            print("The passwords did not match. Please try again.")

def main():
    theloginscreen()  # Show the login screen
    loganswer = input("Choose an option (1, 2, or 3): ")
    logincount = 0

    while True:
        logincount += 1  # Increment the login attempt count
        
        # Check the user's input and respond accordingly
        if loganswer == "1":
            print("   Stefan's super cool project!")
            name = input("Username: ")

            if name == "stefan":
                print("Welcome father!")
                break  # Exit the loop after a successful login
            elif name == "":
                print("Please enter a valid username")
            elif logincount == 2:
                print("You're reaching the maximum login attempts, please consider creating an account if you do not already have one.")
                accountcreationanswer = input("Would you like to create one?(yes/no): ") 
                if accountcreationanswer.lower() == "yes":
                    print("Let's get you started!")
                    accountcreation()
                    break  # Exit after creating an account
                else:
                    print("Returning to login screen...")
                    continue  # Loop back to the login process
            elif logincount == 3:
                print("You've reached the maximum login attempts.\nGoodbye!")
                break  # Exit the loop after reaching max attempts

        elif loganswer == "2":
            print("You selected: Create a user account")
            accountcreation()
            break  # Exit after creating an account

        elif loganswer == "3":
            print("Exiting the program.")
            break  # Exit the program

        else:
            print("Invalid option. Please try again.")
            loganswer = input("Choose an option (1, 2, or 3): ")

# Make sure the script runs only when executed directly
if __name__ == "__main__":
    main()
