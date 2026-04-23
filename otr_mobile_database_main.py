# Tkinter Import
import tkinter as tk

#Tkinter Tools Import
from tkinter import ttk  #Importing ttk from tkinter (newer tools like Combobox)
from tkinter import messagebox # Importing messagebox (a tool that shows "pop-up" windows)

# Login Logic File Imports
from otr_mobile_login_logic import validate_existing_login # Imports function from login logic file (seperate file)
from otr_mobile_login_logic import validate_new_signup_login
from otr_mobile_login_logic import Role

root = tk.Tk()  # Defines main (or root) window


root.title("Welcome")
root.configure(background= "black")
root.minsize(500, 500)
root.maxsize(1920, 1080)

main_window_h1= tk.Label(root, text="Dashboard").pack()

main_window_heroimage= tk.PhotoImage(file= "assests/OTR_Social_Sharing_Logo.PNG")  # Added assets to the file directory here as it was not loading due to that.
tk.Label(root, image= main_window_heroimage).pack()

# Code to Open Dashboard Window
def dashboard_open(): 
 
 dashboard_window = tk.Toplevel(root)
 dashboard_window.title("OTR Mobile Dashboard")

 dashboard_window_h1 = tk.Label(dashboard_window, text = " DASHBOARD IS WIP")
 dashboard_window_h1.pack()


def login_click():  #This function opens a new window when activated
    
    # Start Of Code for Toplevel "login window" ///////////////////

    root.withdraw() # Hides the main root upon login click to avoid a thousand windows.
    login_window= tk.Toplevel(root)
    login_window.title("Login Required")  #Changed the title of the new_window which is a variable that opens a new window.

    login_window_h1 = tk.Label(login_window, text = "Login Required") #used <new_window> instead of root as that is where it is being placed.
    login_window_h1.pack()




    login_window_email_entry = tk.Entry(login_window) # The contained variable in this instance the word in () is where it placed.
    login_window_email_entry.pack()
    

    login_window_pass_entry = tk.Entry(login_window)
    login_window_pass_entry.pack()

    def submit_login(): # Function for getting the input from Entry and running the validation function storing it in user from push of the login button.
     email = login_window_email_entry.get()  # This is <get>ing and storing the input into a variable "email"
     password = login_window_pass_entry.get()

     user = validate_existing_login(email, password)

    # \\\ Start of messagebox (pop-up) user validation code ///
     signup_function_result = validate_existing_login(email, password)

     if signup_function_result == "success":
        messagebox.showinfo("Success", "Login Successful")

                        
        login_window.destroy() # Destroys the login window on succesful account creation.
        dashboard_open() # Opens Dashboard
        return
                
     else:
        messagebox.showerror("Error", signup_function_result)

     # \\\ End of Messagebox Code ///


        
    login_window_login_button = tk.Button(login_window, text = "Login", command = submit_login)
    login_window_login_button.pack()

    def create_click():
          for widget in login_window.winfo_children():  # For loop grabbing all of the listed window's widgets (its childern).
           widget.destroy()   #Destroys them, so we can rebuild it to show diffrent items.

          login_window_new_email_entry = tk.Entry(login_window) # Creates new Entry box for email signup.
          login_window_new_email_entry.pack()

          login_window_new_pass_entry = tk.Entry(login_window) # Creates new Entry box for Password signup.
          login_window_new_pass_entry.pack()

         
          # Switched to Combobox from Listbox for better longevity, and using <ttk> instead of <tk> as Combobox does not exist in <tk>
          login_window_role_selection_box = ttk.Combobox(login_window, values=[list(Role.role_permissions.keys())], state= "readonly")
          # Using list() to avoid dict_keys(['admin']) as its a special object & changed the state to read only to avoid allowing for input.
          # Using Role.role_permissions to have it fill all avialbe Roles (and their permisisons). Using .keys() to pull the key - example (admin: 01), pulling "admin" as it is the key.

          login_window_role_selection_box.pack()
          login_window_role_selection_box.set("Select a Role")


          def submit_new_account():         

           email = login_window_new_email_entry.get()  
           password = login_window_new_pass_entry.get()
           role = login_window_role_selection_box.get()

           user = validate_new_signup_login(email, password, role)


           # \\\ Start of messagebox (pop-up) user validation code ///
           signup_function_result = validate_new_signup_login(email, password, role)

           if signup_function_result == "success":
                messagebox.showinfo("Success", "Account created")

                        
                login_window.destroy() # Destroys the login window on succesful account creation.
                dashboard_open() # Opens Dashboard
                return
                
           else:
                messagebox.showerror("Error", signup_function_result)

           # \\\ End of Messagebox Code ///

 

          login_window_existing_login_button = tk.Button(login_window, text = "Signup", command = submit_new_account)
          login_window_existing_login_button.pack()

          def return_to_existing_login():
             login_window.destroy() # Destorys old login window.
             login_click()          # Creates new login window.
          
          login_window_existing_account_button = tk.Button(login_window, text = "Already Have an account? Click Here", command = return_to_existing_login)
          login_window_existing_account_button.pack()
          

          


    login_window_new_account_button = tk.Button(login_window, text = "Create a new account", command = create_click)
    login_window_new_account_button.pack()

    # End Of Code for Toplevel "login window" ///////////////////


main_window_button1 = tk.Button(root, bg= "Blue", fg= "white", text= "Login", command = login_click)  #Edited how the main login button is displated (bg = background/ fg = foreground so think the text.)
main_window_button1.pack() 

root.mainloop()