import tkinter as tk
from otr_mobile_login_logic import validate_existing_login

root = tk.Tk()  # Defines main (or root) window



def main_login():
   login= input("Login Required: ")
   if login == "Zac":
        print("Login Success!")



root.title("OTR Mobile Database")
root.configure(background= "black")
root.minsize(500, 500)
root.maxsize(1920, 1080)

main_window_h1= tk.Label(root, text="Dashboard").pack()

main_window_heroimage= tk.PhotoImage(file= "assests/OTR_Social_Sharing_Logo.PNG")  # Added assets to the file directory here as it was not loading due to that.
tk.Label(root, image= main_window_heroimage).pack()


def login_click():  #This function opens a new window when activated
    login_window= tk.Toplevel(root)
    login_window.title("Login Required")  #Changed the title of the new_window which is a variable that opens a new window.
    login_window_h1 = tk.Label(login_window, text = "Login Required").pack() #used <new_window> instead of root as that is where it is being placed.




    login_window_email_entry = tk.Entry(login_window) # The contained variable in this instance the word in () is where it placed.
    login_window_email_entry.pack()
    

    login_window_pass_entry = tk.Entry(login_window)
    login_window_pass_entry.pack()

    def submit_login():
     email = login_window_email_entry.get()  # This is <get>ing and storing the input into a variable "email"
     password = login_window_pass_entry.get()

     user = validate_existing_login(email, password) 

    login_window_login_button = tk.Button(login_window, text = "Login", command = submit_login) #Temp no command for now.
    login_window_login_button.pack()

main_window_button1 = tk.Button(root, bg= "Blue", fg= "white", text= "Login", command = login_click)  #Edited how the main login button is displated (bg = background/ fg = foreground so think the text.)
main_window_button1.pack() 

root.mainloop()