#!/usr/bin/env python3

# Define login screen for user.

yes = ["yes", "y", "correct"]
no = ["no", "n", "nah, dog!", "incorrect"]

def theloginscreen():
    bitchindragon()
    print("      Please select an option below:")
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

def bitchindragon():
    print("\n"*10)
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
         ( . `. ,'    \  '     .-------.  ` '--,                             
          \_) ,'  (_.  \      /         `-----<\\                             
          \'   ,'', `.  \   ,'                 `\\                            
         _/ _/',O)>   )  )_            ,'        >                          
     \\  (o /o) \` )  /  /'\\`   `------<___   ,   )                          
      \`-)| (/`,)\\`-'  /   `.          /   >-'    \\                         
       `-VvvV ,/( `---'\\     `       ,'   /`.      )                        
           / ,//\\  \\   `.    `          ' ,'`.   '\\                        
         (^^(//\     \\    `-\\   ` --------' ,' `.   )                       
          ``` ________>  ,'  \\     .        |    \\   \\                       
     ,-------'        `  )   /               |     \\   \\_                     
   ,'/ _,--,--,,,-,______>   )     \\,    (_. \\     \\   ),---.               
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


def account_retrieval():
    email_info = input("What is the email associated with your account? ")
    
def main():
    bitchindragon()
    theloginscreen()
    logincount = 0
    max_attempts = 3  # Define the maximum number of login attempts

    while logincount < max_attempts:
        loganswer = input("Choose option 1, 2, or 3: ").strip()

        if loganswer == "1":  # Login option
            bitchindragon()
            print("\n" * 3)
            name = input("Username: ").strip()

            with open("accounts.txt", "r") as accounts:
                account_lines = [line.strip().split(":") for line in accounts.readlines()]
                user_account = next((u for u in account_lines if u[0] == name), None)

            if user_account:  # If username exists
                bitchindragon()
                print("\n" * 2)
                print(f"Welcome, {name}!")
                logpassword = input("Password: ").strip()

                # Check if the password matches
                if logpassword == user_account[1].split(" | ")[0]:
                    bitchindragon()
                    print("\n")
                    print("You have successfully logged in.")
                    return  # Exit the function after successful login
                else:
                    print("Incorrect password. Try again.")
                    logincount += 1  # Increment attempts after incorrect password
            else:
                print("Username not found. Try again.")
                logincount += 1  # Increment attempts after incorrect username

            # Check if login attempts have been exceeded
            if logincount >= max_attempts:
                print("You've reached the maximum login attempts!")
                break  # Exit the loop after maximum attempts

        elif loganswer == "2":  # Create account option
            print("You selected: Create a user account")
            accountcreation()
            return  # Exit after account creation

        elif loganswer == "3":  # Exit option
            print("Exiting the program.")
            return  # Exit the program

        else:  # Invalid input handling
            print("Invalid option. Please try again.")
    
    # If max attempts are exceeded, end the program
    print("Exiting due to too many failed login attempts.")

# Make sure the script runs only when executed directly
if __name__ == "__main__":
    main()

