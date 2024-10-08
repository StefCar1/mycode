#!/usr/bin/env python3

# Define login screen for user.

yes = ["yes", "y", "correct"]
no = ["no", "n", "nah, dog!", "incorrect"]

def theloginscreen():
    bitchindragon()
    print("                       Please select an option below:")
    print("1. Enter Username.\n2. Create a user account.\n3. Exit.")

def accountcreation():
    bitchindragon()
    usernamecount = 0
    unacceptableentries = [str(i) for i in range(10)] + [
        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/'
    ]

    while usernamecount < 3:
        usernamecount += 1
        newusername = input("The username cannot contain numbers, symbols, or spaces.\nPlease enter your preferred username here: ")
        
        # Check if username contains any unacceptable characters
        if any(item in newusername for item in unacceptableentries):
            print("The username contains a number, symbol, or space. Please try again.")
            continue
        
        # Check if the username already exists in the file
        with open("accounts.txt", "r") as accounts:
            if any(newusername in line for line in accounts):
                print("That username is taken. Please try another.")
                continue
        
        # Email input and confirmation
        email = input("Enter your preferred email: ")
        emailverification = input(f'Is {email} correct? (yes/no): ').lower()
        if emailverification != 'yes':
            print("Email verification failed. Try again.")
            continue
        
        # Password creation
        passwordcount = 0
        while passwordcount < 3:
            passwordcount += 1
            password = input("Enter your preferred password: ")
            if not password:
                print("You must enter a password.")
                continue
            
            # Confirm password
            password2 = input("Re-enter your password: ")

            if password == password2:
                print("Your account was successfully created!")
                
                # Create a dictionary with the user data
                user_account = {
                    "username": newusername,
                    "password": password2,
                    "email": email
                }
                
                # Write the account to the file
                with open("accounts.txt", "a") as accounts:
                    accounts.write(f"{newusername}:{password2} | {email}\n")
                
                # Return the dictionary with the account details
                main()
            else:
                print("The passwords did not match. Please try again.")
        if passwordcount == 3:
            print("Please try again later once you've decided on a password.")
            return
    if usernamecount == 3:
        print("Please try again later.")
        return

def account_retrieval():
    email_retrieval_count = 0
    max_attempts = 3
    while email_retrieval_count < max_attempts:
        email_info = input("What is the email associated with your account? ").strip()
    
        # Open accounts.txt to check for the email
        with open("accounts.txt", "r") as accounts:
            account_lines = [line.strip().split(":") for line in accounts.readlines()]
        
            # Filter lines that are properly formatted with "username:password | email"
            for line in account_lines:
                if len(line) > 1 and " | " in line[1]:
                    username, user_info = line
                    password, email = user_info.split(" | ")
                    if email == email_info:
                        print(f"An email containing your username ({username}) has been sent!")
                        retrieval_menu_answer = input("Would you like to return to the main menu? ")
                        if retrieval_menu_answer == "yes":
                            main()
                        else:
                            Print("Goodbye!")
        if email_retrieval_count == max_attempts:
            bitchindragon()
            print("You've reached the maximum attempts to provide a valid email address.")
            retrieval_account_creation = input("Would you like to create an account? ")
            if retrieval_account_creation == "yes":
                accountcreation()
            else:
                exit

        else:
            email_retrieval_count += 1
            print("Email not found. Please try again.")


def bitchindragon():
    print("\n"*25)
    print(r"""                                   <`--._<`--.____________________________ 
                                     ) ,..-) ,..------------------------,-' 
                                   ,','  >','  \\                  ,        
                                 ,','  ,','     \\            ,             
                               ,','  ,','        \\       ,                  
                             ,' /  ,' /           \\  ,                     
                            /  /  /  /             \`<                      
                           /  /,-/  /,--------------\/                      
                          /__'--/  (/--.                                    
          .-.     ____, '<.  / '   '   '----.                                
         ( . `. ,'    \  '                 ` '--,                             
          \_) ,'  (_.  \      /                \\                             
          \'   ,'', `.  \   ,'                 `\\                            
         _/ _/',O)>   )  )_            ,'        >                          
     \\  (o /o) \` )  /  /'\\`   `------<___   ,   )                          
      \`-)| (/`,)\\`-'  /   `.          /   >-'    \\                         
       `-VvvV ,/( `---'\\     `       ,'   /`.      )                        
           / ,//\\  \\   `.    `          ' ,'`.   '\\                        
         (^^(//\     \\    `-\\   ` --------' ,' `.   )                       
          ``` ________>  ,'  \\     .        |    \\   \\                       
     ,-------'        `  )   /               \     \\   \\_                     
   ,'/ _,--,--,,,-,______>   )     \\,        \\     \\   ),---.               
  / ,\\ )                   ,'     ,'          \\ .--.\\,  .__, \\-.            
 /_/ /\\)                  /      /             / )-.    /--`--) \\           
( )\\ ) `                 .      /             (-'   `--'      `--)          
 \\' \\'                 /      .               )                          
                        ,     ,                ,'                           
                         `._ .               ,'`.                           
                             |              /-.  `.                         
                             |              \\ \\   `._                      
                              \\            \\  \\     \\.                    
                               \\         ,\\`-  \\  ,'  )                   
                                `--,--,-')   /    \\'   /                    
                                       ,'   /      \\\\,'                     
                                     ,'    /                            
                                    /     /           
                                   (      >                           
                                  /`-,---'\\                            
                                  `-^-------
                        Stefan's Super Cool Project!""")


def login():
    """Handles the login process"""
    logincount = 0
    max_attempts = 3

    while logincount < max_attempts:
        name = input("Username: ").strip()

        # Open accounts.txt to check for username
        with open("accounts.txt", "r") as accounts:
            account_lines = [line.strip().split(":") for line in accounts.readlines()]
            user_account = next((u for u in account_lines if u[0] == name), None)

        if user_account:  # Username found
            bitchindragon()
            password = input("Password: ").strip()

            # Check if password matches
            if password == user_account[1].split(" | ")[0]:
                print("\nYou have successfully logged in.\n")
                return True  # Successful login, exit login process
            else:
                print("Incorrect password. Try again.")
                logincount += 1
        else:
            bitchindragon()
            print("Username not found. Try again.")
            logincount += 1

        if logincount >= max_attempts:
            account_retrieve_answer = input("Maximum login attmepts reached. Would you like to request your username via email? ")
            if account_retrieve_answer == "yes":
                account_retrieval()
            else:
                main()


def main():
    bitchindragon()
    theloginscreen()

    while True:
        loganswer = input("Choose option 1, 2, or 3: ").strip()

        if loganswer == "1":  # Login option
            success = login()  # Call the login function
            if success:
                break  # Exit if login is successful
            else:
                break  # Exit after failed login attempts

        elif loganswer == "2":  # Create account option
            print("You selected: Create a user account")
            accountcreation()
            break  # Exit after account creation

        elif loganswer == "3":  # Exit option
            print("Exiting the program.")
            break  # Exit the program

        else:  # Invalid input handling
            print("Invalid option. Please try again.")

# Make sure the script runs only when executed directly
if __name__ == "__main__":
    main()

