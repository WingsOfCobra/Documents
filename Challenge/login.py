#We are creating a user login and registration

print("Welcome to room 847")

#An answer is being requested
answer = input("Do you already have a account (yes or no)\n")

#If the answer is "yes" you will be sent to the login
if(answer == "yes"):

    print("\nWelcome back")
    
    username = input("\nUsername: ")
    password = input("Password: ")

    print("\n" * 3 + "Welcome to room 847 " + username + "!")


    
#If the answer is no, you will be sent to the registration
elif(answer == "no"): 
    
    
    print("\nWelcome! Please create an account here!")

    email = input("\nEnter your e-mail adress: ")
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    print("\n" *5 +  "Welcome " + username + "! Your account with the e-mail " + email + ", has been succesfully created!")

#if the answer is not "yes" or "no" then it gives you a syntax error
else:
    print("Syntax error: try yes or no")

print("\nIf you want to see your account informations, type 'settings'")

command_input = input()

if command_input == "settings":
    print("\nHere is your account information:\n\nUsername: " + username + "\nPassword: " + password)