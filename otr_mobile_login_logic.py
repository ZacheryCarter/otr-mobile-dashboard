# Author: Zachery Carter
# Date: 3/17/2026
# Core Logic For Login in OTR Mobile Database


class User:
   all_users = [] # Empty list for collection of all users.

   def __init__(self, email, role): #Constructor used to allow for instances to be made automatically.
      self.email = email
      self.role = role

      User.all_users.append(self) # adds the entire user object to the (all_users) list

   def __str__(self): # Tells Python we want it to be a string. Rmbr Methods must be same indention as other methods like __init__ & __str__.
          return f"{self.email},{self.role}" # F-String to print one user object when accessed/called.
   
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
    print("Logged in")


elif login =="signup":

    while True:

        new_user_email = input("What is your email?  ").lower()

        if ("@" in new_user_email) and (new_user_email.endswith((".com", ".net", ".biz", ".org"))): # Email input Validation / In checks for @ in input, and .endswith to see if it ends in ".com" <or> other variations inside the tuple -> <and> to ensure both condtions are met.
            break
        else: print("Invalid Email, please try again.")


    roles_selection_menu = []

    for number_of_role, available_roles in enumerate(Role.role_permissions): # For loop for creating items for role_selection_menu, enumerate counts each instance iterated over and stores it (for i, variable in main variable)
        roles_selection_menu.append((number_of_role + 1, available_roles)) # Appends the for loop output to the empty list, uses double parathesis to make it one object as a tuple to be appendable. - added + 1 as Python defaults to 0.


    for selectable_roles_numbers, selectable_roles in roles_selection_menu:
        
        print (f"Available Roles:  {selectable_roles_numbers}. {selectable_roles}") # F string used here to unpack the tuple created by other for loop, as F strings only require "" at beginning and end - maintaining neatness.
        
        while True: # While loop used to ensure we get an expected & acceptable input.
            new_user_role = int(input("What is your role? ")) # Added Capitialze to avoid possible mismatches.

            if new_user_role == selectable_roles_numbers: # Makes sure input matches item from list.
                new_user_role = selectable_roles # If input matches it assigns it the corresponding role.
                break
            else: print("Please choice a number from the list.")





    logged_in_user = User(new_user_email, new_user_role)

    for users in User.all_users:  #Using for loop to iterate over and print each instance of (users in all_users) list.
     print(users)

    print(logged_in_user.get_permissions())