import tkinter as tk             
from otr_mobile_login_logic import validate_existing_login # Imports function from login logic file (seperate file)
from otr_mobile_login_logic import validate_new_signup_login
from otr_mobile_login_logic import Role

root = tk.Tk()  # Defines main (or root) window


root.title("OTR Mobile Database")
root.configure(background= "black")
root.minsize(500, 500)
root.maxsize(1920, 1080)

main_window_h1= tk.Label(root, text="Dashboard").pack()

main_window_heroimage= tk.PhotoImage(file= "assests/OTR_Social_Sharing_Logo.PNG")  # Added assets to the file directory here as it was not loading due to that.
tk.Label(root, image= main_window_heroimage).pack()


def login_click():  #This function opens a new window when activated
    
    # Start Of Code for Toplevel "login window" ///////////////////
    
    login_window= tk.Toplevel(root)
    login_window.title("Login Required")  #Changed the title of the new_window which is a variable that opens a new window.
    login_window_h1 = tk.Label(login_window, text = "Login Required").pack() #used <new_window> instead of root as that is where it is being placed.




    login_window_email_entry = tk.Entry(login_window) # The contained variable in this instance the word in () is where it placed.
    login_window_email_entry.pack()
    

    login_window_pass_entry = tk.Entry(login_window)
    login_window_pass_entry.pack()

    def submit_login(): # Function for getting the input from Entry and running the validation function storing it in user from push of the login button.
     email = login_window_email_entry.get()  # This is <get>ing and storing the input into a variable "email"
     password = login_window_pass_entry.get()

     user = validate_existing_login(email, password)

     for widget in root.winfo_children():  # Destorys all widgets in root, so the dashboard can show with successful login.
            widget.destroy()

     if user:  # Destroys the login window when a user is found/exists.
         login_window.destroy()

        
    login_window_login_button = tk.Button(login_window, text = "Login", command = submit_login)
    login_window_login_button.pack()

    def create_click():
          for widget in login_window.winfo_children():  # For loop grabbing all of the listed window's widgets (its childern).
           widget.destroy()   #Destroys them, so we can rebuild it to show diffrent items.

          login_window_new_email_entry = tk.Entry(login_window) # Creates new Entry box for email signup.
          login_window_new_email_entry.pack()

          login_window_new_pass_entry = tk.Entry(login_window) # Creates new Entry box for Password signup.
          login_window_new_pass_entry.pack()

          login_role_textbox = tk.Label(login_window, text = "Select your role:")
          login_role_textbox.pack()


          # Listbox - code inside submit_new account function to avoid breaking indentation for buttons following it.
          login_window_role_selection_box = tk.Listbox(login_window, height = 4) # listbox (dropdown) of availble roles excluding admin (for now).
          login_window_role_selection_box.pack()

          # \\\\\Code for Role Selection Listbox//////
          for role in Role.role_permissions: # for loop to itreate over all roles and their permissions from logic code.
             login_window_role_selection_box.insert(tk.END, role) # Inserts roles from list, tk.END puts the next instance of role last "at the end", so after it adds "admin" then "shipper" would be added after it or "at the end".

             selected_role_index = login_window_role_selection_box.curselection() # curselection shows/gives what the user selected. By giving the index (or position) of whatever was selected. So if admin was first in the list it would be 0.
             # Created the selected_role_index variable to host the selected tuple.

             if not selected_role_index:
                print("Please Select a role")
                return
             
             
             new_user_role = login_window_role_selection_box.get[selected_role_index[0]]
             return
             # Using the created variable selected_role_index that fetches the tuple and the item at index 0 (the number assciaoted) to return the item at that location from the listbox (dropdown.)
             
             # \\\\\ END Of Role Selection Listbox Code////////


          def submit_new_account():         

           email = login_window_new_email_entry.get()  
           password = login_window_new_pass_entry.get()
           role = new_user_role

           user = validate_new_signup_login(email, password, role)

           for widget in root.winfo_children():  # ////!!!! Change this to reprompt login - later
                        widget.destroy()
                        
           if user:  # Destroys the login window when a user is found/exists.
                login_window.destroy()
                return
 

          login_window_existing_login_button = tk.Button(login_window, text = "Signup", command = submit_new_account)
          login_window_existing_login_button.pack()

          
          login_window_existing_account_button = tk.Button(login_window, text = "Already Have an account? Click Here", command = "none")
          login_window_existing_account_button.pack()

          


    login_window_new_account_button = tk.Button(login_window, text = "Create a new account", command = create_click)
    login_window_new_account_button.pack()

    # End Of Code for Toplevel "login window" ///////////////////


main_window_button1 = tk.Button(root, bg= "Blue", fg= "white", text= "Login", command = login_click)  #Edited how the main login button is displated (bg = background/ fg = foreground so think the text.)
main_window_button1.pack() 

root.mainloop()