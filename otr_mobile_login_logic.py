# Author: Zachery Carter
# Date: 3/17/2026
# Core Logic For Login in OTR Mobile Database


class User:
   all_users = [] # Empty list for collection of all users.

   def __init__(self, email, password, role): #Constructor used to allow for instances to be made automatically.
      self.email = email
      self.password = password
      self.role = role

      User.all_users.append(self) # adds the entire user object to the (all_users) list

   def __str__(self): # Tells Python we want it to be a string. Rmbr Methods must be same indention as other methods like __init__ & __str__.
          return f"{self.email},{self.password}, {self.role}" # F-String to print one user object when accessed/called. # ***Added Password for now to begin working on data storage.
   
   def get_permissions(self):
        return Role.role_permissions.get(self.role, []) # Gets the permissions for the User's Role

class Role:
    def __init__ (self, role):
        self.role = role

    role_permissions = {"admin": ["view", "create", "edit", "delete"],} # Dictonary hosting Role Titles and their deisgniated permisions.



    def change_role(self, new_role):
            self.role = new_role


# End of Class defintions for Login Logic


#Existing User Login Logic


while True:
    login = input("Login or Signup: ").lower() # The While loop always runs, asking for an input until correct input is given. 
   
    if login == "login":
      break

    elif login == "signup":
        break

    else:
        print("Invalid Entry, please type Login or Signup")



if login == "login":
    with open("OTR Mobile Dashboard - Saved Logins.txt", "r") as file:
         lines = file.readlines()
         print(lines)






# New User Login Logic

elif login =="signup":

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


        logged_in_user = User(new_user_email, user_password, new_user_role) # Stores logged in user info (Password is just user_password for now, subject to change.)

                            
        for users in User.all_users:  #Using for loop to iterate over and print each instance of (users in all_users) list.
         print(users)

        print(logged_in_user.get_permissions())
        break  