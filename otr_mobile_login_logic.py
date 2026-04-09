# Author: Zachery Carter
# Date: 3/17/2026
# Core Logic For Login in OTR Mobile Database


class User:
   all_users = [] # Empty list for collection of all users.

   def __init__(self, email, password, role, credentials): #Constructor used to allow for instances to be made automatically.
      self.email = email
      self.password = password
      self.role = role
      self.credentials = credentials  # Added credentials to add a list associsted with every class instance to be referenced later on - for login validation/verification purposes.

      self.credentials = [self.email, self.password, self.role]

      User.all_users.append(self) # adds the entire user object to the (all_users) list

   def __str__(self): # Tells Python we want it to be a string. Rmbr Methods must be same indention as other methods like __init__ & __str__.
          return f"{self.email},{self.password},{self.role}" # F-String to print one user object when accessed/called. # ***Added Password for now to begin working on data storage.
   
   def get_permissions(self):
        return Role.role_permissions.get(self.role, []) # Gets the permissions for the User's Role


class Role:
    def __init__ (self, role):
        self.role = role

    role_permissions = {"admin": ["view", "create", "edit", "delete"],} # Dictonary hosting Role Titles and their deisgniated permisions.



    def change_role(self, new_role):
            self.role = new_role


# End of Class defintions for Login Logic

def validate_login(login):
# Logic for Exisiting Login Or New Signup
        # Was running the function inside itself, leading to recursion, delted that
        login = login.strip().lower() # Removed console input logic to accept Input from GUI. 
   
        if login == "login":
                return login
        elif login == "signup":
                return login
        
        else: print("Invalid Entry, please type Login or Signup")
        


# Existing User Login Logic
def validate_existing_login(email, password, role): # Assigned Logic to Function for GUI.
    if login == "login":
            with open("OTR Mobile Dashboard - Saved Logins.txt", "r") as file: # Opens the text file with saved logins in <"r"> Read Only. ***STORES THEM AS A LIST ALREADY!
            
                existing_login= file.readlines() #Using readlines instead of read to read each line as a list of strings one per line. Will need to break up into 3 objects for User constructer
                
                                
                parsed_users = [] # Added a list outside the for as I was having issues with it iterating over every line due to nature of for
                # This for loop is indented on the same line as existing_user_list to allow it to use the full list.
                  # A for loop to iterate over every item in the first line.
                for existing_line_items in existing_login:  # A for loop to iterate over every item in the first line.
                        existing_login_info = existing_line_items.strip().split(",")    
                        

                        existing_user_email = existing_login_info[0].lower().strip()  # With the spilt above we can now assign variables to seperate parts of the list based on index. For the constructor to build a User class instance. - Using .lower() here to make sure there are no errors in the future based on case.                
                                     
                        
                        existing_user_password = existing_login_info[1].strip() # We use strip here to clean the data removing whitespace, so that it matches expected input containting no whitespaces. (helpful for the role where it only runs if it matches exact expected key).
                
                        
                        existing_user_role = existing_login_info[2].strip()
                
                        parsed_users.append([existing_user_email,existing_user_password,existing_user_role])
                
                      
                print(parsed_users)                   
# Deleted the <while loop> as it was hurting my attempts at running the program!!!
                matched_user = None
                existing_user_input_email =email.lower().strip() # User lower for cleaner data/avoid future errors. changed to email from <input> for GUI Refactor

                  # Removed email validation for ending in .com and containing @ as it's more for a new account signing up.  
                    
                matched_user = None # Attributed the matched login to a variable for user later in password authorization.
                for existing_user_line in parsed_users:  
                    if existing_user_input_email == existing_user_line[0]:
                                                    
                    
                        matched_user = existing_user_line
                        print("Account located")
                        print(matched_user)
                        existing_user_email = existing_user_input_email

                        # Nested Password inside email validation.
                        if matched_user: # If we find a user its the list, and if not it returns None.
                
                            existing_user_input_password = password #Changed from <input> to password element in function for GUI refactor.
                            # Removed the validation as it was more for creating a password.  
              
                            if existing_user_input_password == matched_user[1]:  # Added Secondary <if> instead of <elif> as these two conditions are independet of one another.
                             print("Login Success")
                             existing_user_password = existing_user_input_password  
                             break  

                            if existing_user_input_password != matched_user[1]:                                                    
                                print("Inncorrect Password")
                        
                                                       
                if matched_user is None: # Using none for my concise logic.
                    print("Invalid Email / Account not located, please try again, or create a new account.")
                   
                    
                  
                        
                                   


                                                                            
                                                                
                     






                # Made an if statement to resolve traceback issues
                if matched_user and existing_user_input_password == matched_user[1]:
                    login_credentials = [matched_user[0], matched_user[1], matched_user[2]]
                    existing_user_login = User(matched_user[0], matched_user[1], matched_user[2], login_credentials) # Builds the class instance, based on the varibales calling on certain indexes.
                    print (existing_user_login)
                    print(existing_user_login.get_permissions())
                    return existing_user_login # Replaced break with return here as it's a function.           
                                                                                                    

# New User Login Logic
def validate_new_signup_login(email, password, role): # Assigned Logic to Function for GUI.
    if validate_login =="signup":

        while True:

            new_user_email = input("What is your email?  ").lower()

            if ("@" in new_user_email) and (new_user_email.endswith((".com", ".net", ".biz", ".org"))): # Email input Validation / In checks for @ in input, and .endswith to see if it ends in ".com" <or> other variations inside the tuple -> <and> to ensure both condtions are met.
                break
            else: print("Invalid Email, please try again.")


# Password Creation/Validation Logic

        print("Welcome ", new_user_email)

        while True:
            password_creation = input("Create Password: ")

            accepted_password_symbols_list = ["@", "!", ".", "&", "$", "#", "?"]
            accepted_password_numbers_list = ["1", "2", "3", "4", "5", "6", "7","8", "9", "0"]
            accepted_password_uppletters_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"]
            accepted_password_lowletters_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y","Z"]


            password_creation_symbol_check = False  # Starting with the default value of the variable as False as we are looking for ANY possible match.
            for accepted_password_symbols in accepted_password_symbols_list:  # Due to the fact a list can not be used in the <in> method I am using these for loops to iterate over every item in the related list. 
                if accepted_password_symbols in password_creation: # If statement to check if any of the items in the list are found in the inputted password.
                 password_creation_symbol_check = True  # If they are found, this variable is marked true to be called on in the main check.
                  # Premature break here - was removed as it did not allow for variations to be saved outside of aA1@ as it break(ed) immeditaely before reitirating over the rest.
            

            password_creation_number_check = False
            for accepted_password_numbers in accepted_password_numbers_list: # Identical Flow/Methodology as above here.
                if accepted_password_numbers in password_creation:
                 password_creation_number_check = True
                 
            

            password_creation_uppletter_check = False
            for accepted_password_uppletters in accepted_password_uppletters_list:
             if accepted_password_uppletters in password_creation:
                 password_creation_uppletter_check = True
                 
            
            password_creation_lowletter_check = False
            for accepted_password_lowletters in accepted_password_lowletters_list:
                if accepted_password_lowletters in password_creation:
                      password_creation_lowletter_check = True
               
            

            if password_creation_symbol_check == True and password_creation_number_check == True and password_creation_uppletter_check == True and password_creation_lowletter_check == True:  # Main Password Check ensuring every requirement is met at once.
                user_password = password_creation
                print("Password saved: ", user_password)
                break

            else: print("Invalid Password, please try again and include one symbol, upper-case letter, lower-case letter, and number in your desired password.")
        
        
        

    
        while True: # While loop used to ensure we get an expected & acceptable input.
                
                    roles_selection_menu = [] # I moved the list and the for loops that result in the printing of the numbered list of roles insde this for loop to allow it to run without error.

                    for number_of_role, available_roles in enumerate(Role.role_permissions): # For loop for creating items for role_selection_menu, enumerate counts each instance iterated over and stores it (for i, variable in main variable)
                                            roles_selection_menu.append((number_of_role + 1, available_roles)) # Appends the for loop output to the empty list, uses double parathesis to make it one object as a tuple to be appendable. - added + 1 as Python defaults to 0.


                    for selectable_roles_numbers, selectable_roles in roles_selection_menu:
                                            
                        print (f"Available Roles:  {selectable_roles_numbers}. {selectable_roles}") # F string used here to unpack the tuple created by other for loop, as F strings only require "" at beginning and end - maintaining neatness.
                        

                    new_user_role = (input("What is your role? "))
                
                    if  int(new_user_role) == selectable_roles_numbers: # Makes sure input matches item from list. Used with int() to allow users to input the number asscioated with it from the list.
                        new_user_role = selectable_roles # If input matches it assigns it the corresponding role.
                                            
                    else: print("Please choice a number from the list.")

                    new_user_credentials = [new_user_email, user_password, new_user_role] # Added credentials as the class object was changed to inlcude it.

                    new_logged_in_user = User(new_user_email, user_password, new_user_role, new_user_credentials) # Stores logged in user info (Password is just user_password for now, subject to change.)

                                        
                    for users in User.all_users:  #Using for loop to iterate over and print each instance of (users in all_users) list.
                        print(users)

                    print(new_logged_in_user.get_permissions())
                    return new_logged_in_user # Replaced break with return here as it's a function.
                    


# Simulated input from GUI:


# Existing Login Simulation
login = validate_login("loGin")
user =validate_existing_login("zac@otrmobile.com","OtrRocks12!","admin")
print(user)